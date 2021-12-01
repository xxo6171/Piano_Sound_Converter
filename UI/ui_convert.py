from Modules.convert_16kHz_mono import convert_16kHz_mono
from Modules.tensorflow_hub_model import tensorflow_hub_model
from Modules.output_hz import output_hz
from Modules.ideal_offset import hz_offset
from Modules.quantization import quantization
from output_midi import mk_score
import statistics

'''
Piano Sound Converter UI
'''

def UI_PSC(data) :
    MAX_ABS_INT16 = 32768.0
    '''1. 모노 오디오 변환'''
    convert_mono_output, converted_mono_audio = convert_16kHz_mono(data,output_file='../Audios/converted_audio_mono.wav')
    converted_mono_audio = converted_mono_audio / float(MAX_ABS_INT16)

    '''2. SPICE 모델을 사용해 추정 pitch값 반환'''
    indices, pitch_outputs, confidence_outputs = tensorflow_hub_model(converted_mono_audio)

    '''3. 반환 받은 pitch값을 절대 pitch값으로 변환, confidence 값이 0.9보다 크면 절대 피치 값 배열에 저장 그 외 0 저장'''
    confident_pitch_values_hz = [output_hz(p) if c >= 0.9 else 0 for i, p, c in zip(indices, pitch_outputs, confidence_outputs)]

    '''텀이 있는 부분(0의 값)은 제외합니다.'''
    offsets = [hz_offset(p) for p in confident_pitch_values_hz if p != 0]

    '''idel offset'''
    ideal_offset = statistics.mean(offsets) #데이터의 산술 평균
    print("ideal offset: ", ideal_offset)

    '''4. 반환 받은 절대 pitch값을 양자화시켜 음표 값 반환'''
    quantized_note, predictions_per_note = quantization(confident_pitch_values_hz, ideal_offset)
    print(quantized_note)

    return quantized_note, predictions_per_note

def return_score(quantized_note, predictions_per_note) :
    stream_score = mk_score(quantized_note, predictions_per_note)
    return stream_score

