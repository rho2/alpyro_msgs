from alpyro_msgs import RosMessage, float32


class Pose(RosMessage):
  __msg_typ__ = "turtlesim/Pose"
  __msg_def__ = "ZmxvYXQzMiB4CmZsb2F0MzIgeQpmbG9hdDMyIHRoZXRhCmZsb2F0MzIgbGluZWFyX3ZlbG9jaXR5CmZsb2F0MzIgYW5ndWxhcl92ZWxvY2l0eQoK"
  __md5_sum__ = "863b248d5016ca62ea2e895ae5265cf9"

  x: float32
  y: float32
  theta: float32
  linear_velocity: float32
  angular_velocity: float32
