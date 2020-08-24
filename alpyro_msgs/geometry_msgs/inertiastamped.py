from alpyro_msgs import RosMessage
from alpyro_msgs.std_msgs.header import Header
from alpyro_msgs.geometry_msgs.inertia import Inertia


class InertiaStamped(RosMessage):
  __msg_typ__ = "geometry_msgs/InertiaStamped"
  __msg_def__ = "c3RkX21zZ3MvSGVhZGVyIGhlYWRlcgogIHVpbnQzMiBzZXEKICB0aW1lIHN0YW1wCiAgc3RyaW5nIGZyYW1lX2lkCmdlb21ldHJ5X21zZ3MvSW5lcnRpYSBpbmVydGlhCiAgZmxvYXQ2NCBtCiAgZ2VvbWV0cnlfbXNncy9WZWN0b3IzIGNvbQogICAgZmxvYXQ2NCB4CiAgICBmbG9hdDY0IHkKICAgIGZsb2F0NjQgegogIGZsb2F0NjQgaXh4CiAgZmxvYXQ2NCBpeHkKICBmbG9hdDY0IGl4egogIGZsb2F0NjQgaXl5CiAgZmxvYXQ2NCBpeXoKICBmbG9hdDY0IGl6egoK"
  __md5_sum__ = "ddee48caeab5a966c5e8d166654a9ac7"

  header: Header
  inertia: Inertia
