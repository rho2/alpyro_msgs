from typing import List
from typing_extensions import Annotated
from alpyro_msgs import RosMessage
from alpyro_msgs.std_msgs.header import Header
from alpyro_msgs.geometry_msgs.posewithcovariance import PoseWithCovariance


class PoseWithCovarianceStamped(RosMessage):
  __msg_typ__ = "geometry_msgs/PoseWithCovarianceStamped"
  __msg_def__ = "c3RkX21zZ3MvSGVhZGVyIGhlYWRlcgogIHVpbnQzMiBzZXEKICB0aW1lIHN0YW1wCiAgc3RyaW5nIGZyYW1lX2lkCmdlb21ldHJ5X21zZ3MvUG9zZVdpdGhDb3ZhcmlhbmNlIHBvc2UKICBnZW9tZXRyeV9tc2dzL1Bvc2UgcG9zZQogICAgZ2VvbWV0cnlfbXNncy9Qb2ludCBwb3NpdGlvbgogICAgICBmbG9hdDY0IHgKICAgICAgZmxvYXQ2NCB5CiAgICAgIGZsb2F0NjQgegogICAgZ2VvbWV0cnlfbXNncy9RdWF0ZXJuaW9uIG9yaWVudGF0aW9uCiAgICAgIGZsb2F0NjQgeAogICAgICBmbG9hdDY0IHkKICAgICAgZmxvYXQ2NCB6CiAgICAgIGZsb2F0NjQgdwogIGZsb2F0NjRbMzZdIGNvdmFyaWFuY2UKCg=="
  __md5_sum__ = "953b798c0f514ff060a53a3498ce6246"

  header: Header
  pose: PoseWithCovariance
