import tensorflow as tf
import tensorflow_hub as hub

'''
SPICE 모델 사용
uncertainties: 구간 [0, 1]의 값 목록으로, 각 값은 정확한 피치 예측을 얻을 때 모델의 불확실성에 해당합니다
(1 - 불확실성을 사용하여 피치를 올바르게 식별했다는 모델의 신뢰도를 얻을 수 있습니다.)
pitches: 입력 오디오의 피치에 해당하는 간격 [0, 1]의 값 목록입니다.
SPICE 모델을 사용하기 위해 샘플링 속도를 512로 맞춰서 진행해줍니다.
'''

model = hub.load("https://tfhub.dev/google/spice/2")
def tensorflow_hub_model(data) :

  model_output = model.signatures["serving_default"](tf.constant(data, tf.float32))
  #pitch 값
  pitch_outputs = model_output["pitch"]

  #불확실한 pitch값
  uncertainty_outputs = model_output["uncertainty"]

  #신뢰도 높은 값
  confidence_outputs = 1.0 - uncertainty_outputs

  confidence_outputs = list(confidence_outputs)

  pitch_outputs = [float(x) for x in pitch_outputs]

  indices = range(len(pitch_outputs))
  confident_pitch_outputs = [(i, p)
                               for i, p, c in zip(indices, pitch_outputs, confidence_outputs) if c >= 0.9]
  confident_pitch_outputs_x, confident_pitch_outputs_y = zip(*confident_pitch_outputs)

  return indices, pitch_outputs, confidence_outputs


# Ts_hub_model(cv.audio_samples)

