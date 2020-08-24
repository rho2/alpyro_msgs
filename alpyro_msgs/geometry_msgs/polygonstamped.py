from typing import List
from typing_extensions import Annotated
from alpyro_msgs import RosMessage
from alpyro_msgs.geometry_msgs.polygon import Polygon
from alpyro_msgs.std_msgs.header import Header


class PolygonStamped(RosMessage):
  __msg_typ__ = "geometry_msgs/PolygonStamped"
  __msg_def__ = "c3RkX21zZ3MvSGVhZGVyIGhlYWRlcgogIHVpbnQzMiBzZXEKICB0aW1lIHN0YW1wCiAgc3RyaW5nIGZyYW1lX2lkCmdlb21ldHJ5X21zZ3MvUG9seWdvbiBwb2x5Z29uCiAgZ2VvbWV0cnlfbXNncy9Qb2ludDMyW10gcG9pbnRzCiAgICBmbG9hdDMyIHgKICAgIGZsb2F0MzIgeQogICAgZmxvYXQzMiB6Cgo="
  __md5_sum__ = "c6be8f7dc3bee7fe9e8d296070f53340"

  header: Header
  polygon: Polygon
