import math

'''음표 오프셋 추출하는 함수입니다.'''
A4 = 440
C0 = A4 * pow(2, -4.75)
''' C(도) C#(도#) D(레) D#(레#) E(미) F(파) F(파#) G(솔) G#(솔#) A(라) A#(라#) B(시) '''
note_names = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]

def hz_offset(freq):
  ''' 단일 음에 대한 양자화 오류를 측정합니다. 값이 0 일 때 None 값 반환 '''
  if freq == 0:
    return None
  '''양자화된 음표'''
  h = round(12 * math.log2(freq / C0))
  # print("12 * {0} - {1} = {2}".format(math.log2(freq / C0), h, 12 * math.log2(freq / C0) - h))
  return 12 * math.log2(freq / C0) - h

