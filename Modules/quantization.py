import statistics
import math
import Modules.ideal_offset as ido

'''양자화 예측'''
def quantization(confident_pitch_values_hz, ideal_offset) :
    def quantize_predictions(group, ideal_offset):
      '''그룹의 값은 0 또는 Hz 단위의 pitch입니다.'''
      non_zero_values = [v for v in group if v != 0]
      zero_values_count = len(group) - len(non_zero_values)

      '''80%가 묵음(소리없음)이면 쉼표를 만들고, 그렇지 않으면 음표를 만듭니다.'''
      if zero_values_count > 0.8 * len(group):
        '''휴식으로 해석합니다. 떨어진 각 음표를 오류로 계산하고 약간의 가중치를 부여합니다.'''
        return 0.51 * len(non_zero_values), "Rest"
      else:
        '''휴식이 없는 예측 값의 평균으로 추정'''
        h = round(statistics.mean([12 * math.log2(freq / ido.C0) - ideal_offset for freq in non_zero_values]))
        octave = h // 12
        n = h % 12
        note = ido.note_names[n] + str(octave) #음표 값
        '''양자화 오류는 양자화된 음표와의 총 차이입니다.'''
        error = sum([
            abs(12 * math.log2(freq / ido.C0) - ideal_offset - h)
            for freq in non_zero_values
        ])
        return error, note    #에러 값과 음표 반환

    '''양자화된 음표와 에러 값 얻기'''
    def get_quantization_and_error(pitch_outputs_and_rests, predictions_per_eighth,
                                   prediction_start_offset, ideal_offset):
      '''시작 간격 띄우기 - 간격 띄우기를 휴식으로 처리할 수 있습니다.'''
      pitch_outputs_and_rests = [0] * prediction_start_offset + \
                                pitch_outputs_and_rests
      '''음표를 예측하기 위해 수집합니다.'''
      groups = [
          pitch_outputs_and_rests[i:i + predictions_per_eighth]
          for i in range(0, len(pitch_outputs_and_rests), predictions_per_eighth)
      ]

      quantization_error = 0

      notes_and_rests = []
      for group in groups:
        error, note_or_rest = quantize_predictions(group, ideal_offset)
        quantization_error += error
        notes_and_rests.append(note_or_rest)

      return quantization_error, notes_and_rests


    best_error = float("inf")
    best_notes_and_rests = None
    best_predictions_per_note = None

    for predictions_per_note in range(20, 65, 1):
      for prediction_start_offset in range(predictions_per_note):

        error, notes_and_rests = get_quantization_and_error(
            confident_pitch_values_hz, predictions_per_note,
            prediction_start_offset, ideal_offset)

        if error < best_error:
          best_error = error
          best_notes_and_rests = notes_and_rests
          best_predictions_per_note = predictions_per_note

    '''
    최상의 양자화가 포함된 best_note_and_rests
    처음에는 휴식을 취할 필요가 없으니, 초반 부분을 제거합니다.
    '''
    while best_notes_and_rests[0] == 'Rest':
      best_notes_and_rests = best_notes_and_rests[1:]

    '''마지막 구간에 있는 휴식 부분도 지웁니다.'''
    while best_notes_and_rests[-1] == 'Rest':
      best_notes_and_rests = best_notes_and_rests[:-1]

    return best_notes_and_rests, best_predictions_per_note
