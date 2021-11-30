from pydub import AudioSegment
from scipy.io import wavfile

'''모노 오디오 파일로 변환하는 함수입니다.'''
EXPECTED_SAMPLE_RATE = 16000

def convert_16kHz_mono(user_file, output_file='Audios/converted_audio_mono.wav'):
  audio = AudioSegment.from_file(user_file)
  audio = audio.set_frame_rate(EXPECTED_SAMPLE_RATE).set_channels(1)
  audio.export(output_file, format="wav")
  sample_rate, audio_samples = wavfile.read(output_file, 'rb')
  duration = len(audio_samples) / sample_rate
  print(f'Sample rate: {sample_rate} Hz')
  print(f'Total duration: {duration:.2f}s')
  print(f'Size of the input: {len(audio_samples)}')
  return output_file, audio_samples



