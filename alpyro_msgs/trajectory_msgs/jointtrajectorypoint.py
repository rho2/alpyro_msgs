from typing import List
from typing_extensions import Annotated
from alpyro_msgs import RosMessage, duration, float64


class JointTrajectoryPoint(RosMessage):
  __msg_typ__ = "trajectory_msgs/JointTrajectoryPoint"
  __msg_def__ = "ZmxvYXQ2NFtdIHBvc2l0aW9ucwpmbG9hdDY0W10gdmVsb2NpdGllcwpmbG9hdDY0W10gYWNjZWxlcmF0aW9ucwpmbG9hdDY0W10gZWZmb3J0CmR1cmF0aW9uIHRpbWVfZnJvbV9zdGFydAoK"
  __md5_sum__ = "f3cd1e1c4d320c79d6985c904ae5dcd3"

  positions: Annotated[List[float64], 0, 0]
  velocities: Annotated[List[float64], 0, 0]
  accelerations: Annotated[List[float64], 0, 0]
  effort: Annotated[List[float64], 0, 0]
  time_from_start: duration
