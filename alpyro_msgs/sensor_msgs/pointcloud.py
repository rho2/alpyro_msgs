from typing import List
from typing_extensions import Annotated
from alpyro_msgs import RosMessage
from alpyro_msgs.geometry_msgs.point32 import Point32
from alpyro_msgs.sensor_msgs.channelfloat32 import ChannelFloat32
from alpyro_msgs.std_msgs.header import Header


class PointCloud(RosMessage):
  __msg_typ__ = "sensor_msgs/PointCloud"
  __msg_def__ = "c3RkX21zZ3MvSGVhZGVyIGhlYWRlcgogIHVpbnQzMiBzZXEKICB0aW1lIHN0YW1wCiAgc3RyaW5nIGZyYW1lX2lkCmdlb21ldHJ5X21zZ3MvUG9pbnQzMltdIHBvaW50cwogIGZsb2F0MzIgeAogIGZsb2F0MzIgeQogIGZsb2F0MzIgegpzZW5zb3JfbXNncy9DaGFubmVsRmxvYXQzMltdIGNoYW5uZWxzCiAgc3RyaW5nIG5hbWUKICBmbG9hdDMyW10gdmFsdWVzCgo="
  __md5_sum__ = "d8e9c3f5afbdd8a130fd1d2763945fca"

  header: Header
  points: Annotated[List[Point32], 0, 0]
  channels: Annotated[List[ChannelFloat32], 0, 0]
