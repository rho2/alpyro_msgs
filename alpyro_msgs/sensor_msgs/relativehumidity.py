from alpyro_msgs import RosMessage, float64
from alpyro_msgs.std_msgs.header import Header


class RelativeHumidity(RosMessage):
  __msg_typ__ = "sensor_msgs/RelativeHumidity"
  __msg_def__ = "c3RkX21zZ3MvSGVhZGVyIGhlYWRlcgogIHVpbnQzMiBzZXEKICB0aW1lIHN0YW1wCiAgc3RyaW5nIGZyYW1lX2lkCmZsb2F0NjQgcmVsYXRpdmVfaHVtaWRpdHkKZmxvYXQ2NCB2YXJpYW5jZQoK"
  __md5_sum__ = "8730015b05955b7e992ce29a2678d90f"

  header: Header
  relative_humidity: float64
  variance: float64
