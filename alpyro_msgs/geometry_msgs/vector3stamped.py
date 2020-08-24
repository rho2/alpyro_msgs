from alpyro_msgs import RosMessage
from alpyro_msgs.geometry_msgs.vector3 import Vector3
from alpyro_msgs.std_msgs.header import Header


class Vector3Stamped(RosMessage):
  __msg_typ__ = "geometry_msgs/Vector3Stamped"
  __msg_def__ = "c3RkX21zZ3MvSGVhZGVyIGhlYWRlcgogIHVpbnQzMiBzZXEKICB0aW1lIHN0YW1wCiAgc3RyaW5nIGZyYW1lX2lkCmdlb21ldHJ5X21zZ3MvVmVjdG9yMyB2ZWN0b3IKICBmbG9hdDY0IHgKICBmbG9hdDY0IHkKICBmbG9hdDY0IHoKCg=="
  __md5_sum__ = "7b324c7325e683bf02a9b14b01090ec7"

  header: Header
  vector: Vector3
