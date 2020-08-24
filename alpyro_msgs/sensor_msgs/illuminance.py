from alpyro_msgs import RosMessage, float64
from alpyro_msgs.std_msgs.header import Header


class Illuminance(RosMessage):
  __msg_typ__ = "sensor_msgs/Illuminance"
  __msg_def__ = "c3RkX21zZ3MvSGVhZGVyIGhlYWRlcgogIHVpbnQzMiBzZXEKICB0aW1lIHN0YW1wCiAgc3RyaW5nIGZyYW1lX2lkCmZsb2F0NjQgaWxsdW1pbmFuY2UKZmxvYXQ2NCB2YXJpYW5jZQoK"
  __md5_sum__ = "8cf5febb0952fca9d650c3d11a81a188"

  header: Header
  illuminance: float64
  variance: float64
