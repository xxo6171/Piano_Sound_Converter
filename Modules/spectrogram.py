import numpy as np
import matplotlib.pyplot as plt
import librosa
from librosa import display as librosadisplay

'''스펙트로그램 그래프 출력 함수입니다.'''
'''오디오 샘플 int16'''
MAX_ABS_INT16 = 32768.0

def spectrogram_plot_stft(x, sample_rate, show_black_and_white=False):
  x_stft = np.abs(librosa.stft(x, n_fft=2048))
  fig, ax = plt.subplots()
  fig.set_size_inches(10, 5)
  x_stft_db = librosa.amplitude_to_db(x_stft, ref=np.max)
  if(show_black_and_white):
    librosadisplay.specshow(data=x_stft_db, y_axis='log',
                             sr=sample_rate, cmap='gray_r')
  else:
    librosadisplay.specshow(data=x_stft_db, y_axis='log', sr=sample_rate)

  plt.xlabel('Time')
  plt.ylabel('Frequency')
  plt.colorbar(format='%+2.0f dB')
  plt.show()


