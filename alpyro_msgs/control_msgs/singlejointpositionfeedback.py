from alpyro_msgs import RosMessage, float64
from alpyro_msgs.std_msgs.header import Header


class SingleJointPositionFeedback(RosMessage):
  __msg_typ__ = "control_msgs/SingleJointPositionFeedback"
  __msg_def__ = "c3RkX21zZ3MvSGVhZGVyIGhlYWRlcgogIHVpbnQzMiBzZXEKICB0aW1lIHN0YW1wCiAgc3RyaW5nIGZyYW1lX2lkCmZsb2F0NjQgcG9zaXRpb24KZmxvYXQ2NCB2ZWxvY2l0eQpmbG9hdDY0IGVycm9yCgo="
  __md5_sum__ = "8cee65610a3d08e0a1bded82f146f1fd"

  header: Header
  position: float64
  velocity: float64
  error: float64
