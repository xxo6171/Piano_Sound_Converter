import numpy as np
import matplotlib.pyplot as plt

#주파수 영역 그래프
def freDomain_plot(data) :
    fft = np.fft.fft(data)
    magnitude = np.abs(fft)
    f = np.linspace(0, 16000, len(magnitude))
    left_spectrum = magnitude[:int(len(magnitude)/2)]
    left_f = f[:int(len(magnitude)/2)]
    plt.figure(figsize=(10,5))
    plt.plot(left_f, left_spectrum)
    plt.xlabel("Frequency")
    plt.ylabel("Magnitude")
    plt.title("Power spectrum")
    plt.show()