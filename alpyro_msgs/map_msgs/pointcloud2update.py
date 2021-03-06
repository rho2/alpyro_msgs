from typing import List
from typing_extensions import Annotated
from typing import Final
from alpyro_msgs import RosMessage, uint32
from alpyro_msgs.sensor_msgs.pointcloud2 import PointCloud2
from alpyro_msgs.std_msgs.header import Header


class PointCloud2Update(RosMessage):
  __msg_typ__ = "map_msgs/PointCloud2Update"
  __msg_def__ = "dWludDMyIEFERD0wCnVpbnQzMiBERUxFVEU9MQpzdGRfbXNncy9IZWFkZXIgaGVhZGVyCiAgdWludDMyIHNlcQogIHRpbWUgc3RhbXAKICBzdHJpbmcgZnJhbWVfaWQKdWludDMyIHR5cGUKc2Vuc29yX21zZ3MvUG9pbnRDbG91ZDIgcG9pbnRzCiAgc3RkX21zZ3MvSGVhZGVyIGhlYWRlcgogICAgdWludDMyIHNlcQogICAgdGltZSBzdGFtcAogICAgc3RyaW5nIGZyYW1lX2lkCiAgdWludDMyIGhlaWdodAogIHVpbnQzMiB3aWR0aAogIHNlbnNvcl9tc2dzL1BvaW50RmllbGRbXSBmaWVsZHMKICAgIHVpbnQ4IElOVDg9MQogICAgdWludDggVUlOVDg9MgogICAgdWludDggSU5UMTY9MwogICAgdWludDggVUlOVDE2PTQKICAgIHVpbnQ4IElOVDMyPTUKICAgIHVpbnQ4IFVJTlQzMj02CiAgICB1aW50OCBGTE9BVDMyPTcKICAgIHVpbnQ4IEZMT0FUNjQ9OAogICAgc3RyaW5nIG5hbWUKICAgIHVpbnQzMiBvZmZzZXQKICAgIHVpbnQ4IGRhdGF0eXBlCiAgICB1aW50MzIgY291bnQKICBib29sIGlzX2JpZ2VuZGlhbgogIHVpbnQzMiBwb2ludF9zdGVwCiAgdWludDMyIHJvd19zdGVwCiAgdWludDhbXSBkYXRhCiAgYm9vbCBpc19kZW5zZQoK"
  __md5_sum__ = "6c58e4f249ae9cd2b24fb1ee0f99195e"

  ADD: Final[uint32] = 0
  DELETE: Final[uint32] = 1
  header: Header
  type: uint32
  points: PointCloud2
