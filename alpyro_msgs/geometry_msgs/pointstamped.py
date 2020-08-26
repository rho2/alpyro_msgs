from alpyro_msgs import RosMessage
from alpyro_msgs.geometry_msgs.point import Point
from alpyro_msgs.std_msgs.header import Header


class PointStamped(RosMessage):
  __msg_typ__ = "geometry_msgs/PointStamped"
  __msg_def__ = "c3RkX21zZ3MvSGVhZGVyIGhlYWRlcgogIHVpbnQzMiBzZXEKICB0aW1lIHN0YW1wCiAgc3RyaW5nIGZyYW1lX2lkCmdlb21ldHJ5X21zZ3MvUG9pbnQgcG9pbnQKICBmbG9hdDY0IHgKICBmbG9hdDY0IHkKICBmbG9hdDY0IHoKCg=="
  __md5_sum__ = "c63aecb41bfdfd6b7e1fac37c7cbe7bf"

  header: Header
  point: Point
