from alpyro_msgs import RosMessage
from alpyro_msgs.std_msgs.header import Header
from alpyro_msgs.geometry_msgs.pose import Pose


class PoseStamped(RosMessage):
  __msg_typ__ = "geometry_msgs/PoseStamped"
  __msg_def__ = "c3RkX21zZ3MvSGVhZGVyIGhlYWRlcgogIHVpbnQzMiBzZXEKICB0aW1lIHN0YW1wCiAgc3RyaW5nIGZyYW1lX2lkCmdlb21ldHJ5X21zZ3MvUG9zZSBwb3NlCiAgZ2VvbWV0cnlfbXNncy9Qb2ludCBwb3NpdGlvbgogICAgZmxvYXQ2NCB4CiAgICBmbG9hdDY0IHkKICAgIGZsb2F0NjQgegogIGdlb21ldHJ5X21zZ3MvUXVhdGVybmlvbiBvcmllbnRhdGlvbgogICAgZmxvYXQ2NCB4CiAgICBmbG9hdDY0IHkKICAgIGZsb2F0NjQgegogICAgZmxvYXQ2NCB3Cgo="
  __md5_sum__ = "d3812c3cbc69362b77dc0b19b345f8f5"

  header: Header
  pose: Pose