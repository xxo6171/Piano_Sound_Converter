from convert_16kHz_mono import convert_16kHz_mono
from tensorflow_hub_model import tensorflow_hub_model
from output_hz import output_hz
# from spectrogram import spectrogram_plot_stft
# from time_domain import timeDomain_plot
# from frequency_domain import freDomain_plot
'''
Piano Sound Converter
pycharm 환경에서는 함수를 한번에 실행시켜 바로 변환하는 방법으로 진행, 각각의 기능을 모듈화
'''
MAX_ABS_INT16 = 32768.0

def PSC(data) :
    '''1. 모노 오디오 변환'''
    convert_mono_output, converted_mono_audio = convert_16kHz_mono(data)
    converted_mono_audio = converted_mono_audio / float(MAX_ABS_INT16)

    '''2. SPICE 모델을 사용해 추정 pitch값 반환'''
    indices, pitch_outputs, confidence_outputs = tensorflow_hub_model(converted_mono_audio)

    '''3. 반환 받은 pitch값을 절대 pitch값으로 변환, confidence 값이 0.9보다 크면 절대 피치 값 배열에 저장 그 외 0 저장'''
    confident_pitch_values_hz = [output_hz(p) if c >= 0.9 else 0 for i, p, c in zip(indices, pitch_outputs, confidence_outputs)]
    # print(confident_pitch_values_hz)
PSC('Audios/input_audio.wav')




'''데이터 시각화, PSC 메소드 안에 넣어서 사용'''
#timeDomain_plot(16000, converted_mono_audio)
#freDomain_plot(converted_mono_audio)
#spectrogram_plot_stft(converted_mono_audio / 32768.0, sample_rate=16000)