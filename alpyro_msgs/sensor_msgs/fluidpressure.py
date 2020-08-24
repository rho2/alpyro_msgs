from alpyro_msgs import RosMessage, float64
from alpyro_msgs.std_msgs.header import Header


class FluidPressure(RosMessage):
  __msg_typ__ = "sensor_msgs/FluidPressure"
  __msg_def__ = "c3RkX21zZ3MvSGVhZGVyIGhlYWRlcgogIHVpbnQzMiBzZXEKICB0aW1lIHN0YW1wCiAgc3RyaW5nIGZyYW1lX2lkCmZsb2F0NjQgZmx1aWRfcHJlc3N1cmUKZmxvYXQ2NCB2YXJpYW5jZQoK"
  __md5_sum__ = "804dc5cea1c5306d6a2eb80b9833befe"

  header: Header
  fluid_pressure: float64
  variance: float64
