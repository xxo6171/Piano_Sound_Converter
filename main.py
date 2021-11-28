from convert_16kHz_mono import convert_16kHz_mono
from time_domain import timeDomain_plot
from frequency_domin import freDomain_plot

def PSC(data) :
    convert_mono_output, converted_mono_audio = convert_16kHz_mono(data)
    timeDomain_plot(16000, converted_mono_audio)
PSC('Audios/input_audio.wav')