from alpyro_msgs import RosMessage, duration, float64
from alpyro_msgs.std_msgs.header import Header


class PidState(RosMessage):
  __msg_typ__ = "control_msgs/PidState"
  __msg_def__ = "c3RkX21zZ3MvSGVhZGVyIGhlYWRlcgogIHVpbnQzMiBzZXEKICB0aW1lIHN0YW1wCiAgc3RyaW5nIGZyYW1lX2lkCmR1cmF0aW9uIHRpbWVzdGVwCmZsb2F0NjQgZXJyb3IKZmxvYXQ2NCBlcnJvcl9kb3QKZmxvYXQ2NCBwX2Vycm9yCmZsb2F0NjQgaV9lcnJvcgpmbG9hdDY0IGRfZXJyb3IKZmxvYXQ2NCBwX3Rlcm0KZmxvYXQ2NCBpX3Rlcm0KZmxvYXQ2NCBkX3Rlcm0KZmxvYXQ2NCBpX21heApmbG9hdDY0IGlfbWluCmZsb2F0NjQgb3V0cHV0Cgo="
  __md5_sum__ = "b138ec00e886c10e73f27e8712252ea6"

  header: Header
  timestep: duration
  error: float64
  error_dot: float64
  p_error: float64
  i_error: float64
  d_error: float64
  p_term: float64
  i_term: float64
  d_term: float64
  i_max: float64
  i_min: float64
  output: float64
