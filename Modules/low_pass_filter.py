from scipy import signal
'''low pass filter 함수입니다'''
def lowpassfilter(data) :
    b = signal.firwin(101, cutoff=1000, fs=16000, pass_zero='lowpass')
    fil_data  = signal.lfilter(b, [1.0], data)
    return fil_data