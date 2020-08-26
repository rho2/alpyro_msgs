from typing import List
from typing_extensions import Annotated
from alpyro_msgs import RosMessage
from alpyro_msgs.geometry_msgs.pose import Pose
from alpyro_msgs.std_msgs.header import Header


class PoseArray(RosMessage):
  __msg_typ__ = "geometry_msgs/PoseArray"
  __msg_def__ = "c3RkX21zZ3MvSGVhZGVyIGhlYWRlcgogIHVpbnQzMiBzZXEKICB0aW1lIHN0YW1wCiAgc3RyaW5nIGZyYW1lX2lkCmdlb21ldHJ5X21zZ3MvUG9zZVtdIHBvc2VzCiAgZ2VvbWV0cnlfbXNncy9Qb2ludCBwb3NpdGlvbgogICAgZmxvYXQ2NCB4CiAgICBmbG9hdDY0IHkKICAgIGZsb2F0NjQgegogIGdlb21ldHJ5X21zZ3MvUXVhdGVybmlvbiBvcmllbnRhdGlvbgogICAgZmxvYXQ2NCB4CiAgICBmbG9hdDY0IHkKICAgIGZsb2F0NjQgegogICAgZmxvYXQ2NCB3Cgo="
  __md5_sum__ = "916c28c5764443f268b296bb671b9d97"

  header: Header
  poses: Annotated[List[Pose], 0, 0]
