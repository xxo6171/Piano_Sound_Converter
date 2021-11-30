import numpy as np
import matplotlib.pyplot as plt

'''시간 영역 그래프 출력 함수입니다.'''
def timeDomain_plot(x, data) :
    x = np.linspace(0, len(data)/16000, len(data))
    plt.plot(x, data)
    plt.xlabel("Time")
    plt.ylabel("Amplitude")
    plt.title("Time domain")
    plt.show()