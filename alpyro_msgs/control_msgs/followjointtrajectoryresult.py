from typing import Final
from alpyro_msgs import RosMessage, int32, string


class FollowJointTrajectoryResult(RosMessage):
  __msg_typ__ = "control_msgs/FollowJointTrajectoryResult"
  __msg_def__ = "aW50MzIgU1VDQ0VTU0ZVTD0wCmludDMyIElOVkFMSURfR09BTD0tMQppbnQzMiBJTlZBTElEX0pPSU5UUz0tMgppbnQzMiBPTERfSEVBREVSX1RJTUVTVEFNUD0tMwppbnQzMiBQQVRIX1RPTEVSQU5DRV9WSU9MQVRFRD0tNAppbnQzMiBHT0FMX1RPTEVSQU5DRV9WSU9MQVRFRD0tNQppbnQzMiBlcnJvcl9jb2RlCnN0cmluZyBlcnJvcl9zdHJpbmcKCg=="
  __md5_sum__ = "493383b18409bfb604b4e26c676401d2"

  SUCCESSFUL: Final[int32] = 0
  INVALID_GOAL: Final[int32] = -1
  INVALID_JOINTS: Final[int32] = -2
  OLD_HEADER_TIMESTAMP: Final[int32] = -3
  PATH_TOLERANCE_VIOLATED: Final[int32] = -4
  GOAL_TOLERANCE_VIOLATED: Final[int32] = -5
  error_code: int32
  error_string: string
