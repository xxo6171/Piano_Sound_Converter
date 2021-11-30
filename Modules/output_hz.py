
'''SPICE가 반환하는 pitch 값은 0에서 1사이의 범위에 있기에 절대 피치 값(hz)로 변환'''

def output_hz(pitch_output):
  PT_OFFSET = 25.58
  PT_SLOPE = 63.07
  FMIN = 10.0;
  BINS_PER_OCTAVE = 12.0;
  cqt_bin = pitch_output * PT_SLOPE + PT_OFFSET;
  return FMIN * 2.0 ** (1.0 * cqt_bin / BINS_PER_OCTAVE)
