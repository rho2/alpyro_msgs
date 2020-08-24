from typing import List
from typing_extensions import Annotated
from alpyro_msgs import RosMessage, float32
from alpyro_msgs.std_msgs.header import Header


class LaserScan(RosMessage):
  __msg_typ__ = "sensor_msgs/LaserScan"
  __msg_def__ = "c3RkX21zZ3MvSGVhZGVyIGhlYWRlcgogIHVpbnQzMiBzZXEKICB0aW1lIHN0YW1wCiAgc3RyaW5nIGZyYW1lX2lkCmZsb2F0MzIgYW5nbGVfbWluCmZsb2F0MzIgYW5nbGVfbWF4CmZsb2F0MzIgYW5nbGVfaW5jcmVtZW50CmZsb2F0MzIgdGltZV9pbmNyZW1lbnQKZmxvYXQzMiBzY2FuX3RpbWUKZmxvYXQzMiByYW5nZV9taW4KZmxvYXQzMiByYW5nZV9tYXgKZmxvYXQzMltdIHJhbmdlcwpmbG9hdDMyW10gaW50ZW5zaXRpZXMKCg=="
  __md5_sum__ = "90c7ef2dc6895d81024acba2ac42f369"

  header: Header
  angle_min: float32
  angle_max: float32
  angle_increment: float32
  time_increment: float32
  scan_time: float32
  range_min: float32
  range_max: float32
  ranges: Annotated[List[float32], 0, 0]
  intensities: Annotated[List[float32], 0, 0]
