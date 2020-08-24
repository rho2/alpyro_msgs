from alpyro_msgs import RosMessage, string, time
from alpyro_msgs.std_msgs.header import Header


class TimeReference(RosMessage):
  __msg_typ__ = "sensor_msgs/TimeReference"
  __msg_def__ = "c3RkX21zZ3MvSGVhZGVyIGhlYWRlcgogIHVpbnQzMiBzZXEKICB0aW1lIHN0YW1wCiAgc3RyaW5nIGZyYW1lX2lkCnRpbWUgdGltZV9yZWYKc3RyaW5nIHNvdXJjZQoK"
  __md5_sum__ = "fded64a0265108ba86c3d38fb11c0c16"

  header: Header
  time_ref: time
  source: string
