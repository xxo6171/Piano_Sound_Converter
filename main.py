from convert_16kHz_mono import convert_16kHz_mono

def PSC(data) :
    convert_mono_output, converted_mono_audio = convert_16kHz_mono(data)

PSC('Audios/input_audio.wav')