from convert_16kHz_mono import convert_16kHz_mono
from spectrogram import spectrogram_plot_stft
from time_domain import timeDomain_plot
from frequency_domain import freDomain_plot
from tensorflow_hub_model import tensorflow_hub_model

def PSC(data) :
    convert_mono_output, converted_mono_audio = convert_16kHz_mono(data)
    # timeDomain_plot(16000, converted_mono_audio)
    # freDomain_plot(converted_mono_audio)
    #spectrogram_plot_stft(converted_mono_audio / 32768.0, sample_rate=16000)
    tensorflow_hub_model(converted_mono_audio)
PSC('Audios/input_audio.wav')