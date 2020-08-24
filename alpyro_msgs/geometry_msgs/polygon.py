from typing import List
from typing_extensions import Annotated
from alpyro_msgs import RosMessage
from alpyro_msgs.geometry_msgs.point32 import Point32


class Polygon(RosMessage):
  __msg_typ__ = "geometry_msgs/Polygon"
  __msg_def__ = "Z2VvbWV0cnlfbXNncy9Qb2ludDMyW10gcG9pbnRzCiAgZmxvYXQzMiB4CiAgZmxvYXQzMiB5CiAgZmxvYXQzMiB6Cgo="
  __md5_sum__ = "cd60a26494a087f577976f0329fa120e"

  points: Annotated[List[Point32], 0, 0]
