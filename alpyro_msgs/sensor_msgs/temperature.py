from alpyro_msgs import RosMessage, float64
from alpyro_msgs.std_msgs.header import Header


class Temperature(RosMessage):
  __msg_typ__ = "sensor_msgs/Temperature"
  __msg_def__ = "c3RkX21zZ3MvSGVhZGVyIGhlYWRlcgogIHVpbnQzMiBzZXEKICB0aW1lIHN0YW1wCiAgc3RyaW5nIGZyYW1lX2lkCmZsb2F0NjQgdGVtcGVyYXR1cmUKZmxvYXQ2NCB2YXJpYW5jZQoK"
  __md5_sum__ = "ff71b307acdbe7c871a5a6d7ed359100"

  header: Header
  temperature: float64
  variance: float64
