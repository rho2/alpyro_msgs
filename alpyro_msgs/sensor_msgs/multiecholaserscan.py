from typing import List
from typing_extensions import Annotated
from alpyro_msgs import RosMessage, float32
from alpyro_msgs.sensor_msgs.laserecho import LaserEcho
from alpyro_msgs.std_msgs.header import Header


class MultiEchoLaserScan(RosMessage):
  __msg_typ__ = "sensor_msgs/MultiEchoLaserScan"
  __msg_def__ = "c3RkX21zZ3MvSGVhZGVyIGhlYWRlcgogIHVpbnQzMiBzZXEKICB0aW1lIHN0YW1wCiAgc3RyaW5nIGZyYW1lX2lkCmZsb2F0MzIgYW5nbGVfbWluCmZsb2F0MzIgYW5nbGVfbWF4CmZsb2F0MzIgYW5nbGVfaW5jcmVtZW50CmZsb2F0MzIgdGltZV9pbmNyZW1lbnQKZmxvYXQzMiBzY2FuX3RpbWUKZmxvYXQzMiByYW5nZV9taW4KZmxvYXQzMiByYW5nZV9tYXgKc2Vuc29yX21zZ3MvTGFzZXJFY2hvW10gcmFuZ2VzCiAgZmxvYXQzMltdIGVjaG9lcwpzZW5zb3JfbXNncy9MYXNlckVjaG9bXSBpbnRlbnNpdGllcwogIGZsb2F0MzJbXSBlY2hvZXMKCg=="
  __md5_sum__ = "6fefb0c6da89d7c8abe4b339f5c2f8fb"

  header: Header
  angle_min: float32
  angle_max: float32
  angle_increment: float32
  time_increment: float32
  scan_time: float32
  range_min: float32
  range_max: float32
  ranges: Annotated[List[LaserEcho], 0, 0]
  intensities: Annotated[List[LaserEcho], 0, 0]
