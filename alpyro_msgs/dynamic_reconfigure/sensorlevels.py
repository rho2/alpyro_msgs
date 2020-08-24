from typing import Final
from alpyro_msgs import RosMessage, int8


class SensorLevels(RosMessage):
  __msg_typ__ = "dynamic_reconfigure/SensorLevels"
  __msg_def__ = "Ynl0ZSBSRUNPTkZJR1VSRV9DTE9TRT0zCmJ5dGUgUkVDT05GSUdVUkVfU1RPUD0xCmJ5dGUgUkVDT05GSUdVUkVfUlVOTklORz0wCgo="
  __md5_sum__ = "6322637bee96d5489db6e2127c47602c"

  RECONFIGURE_CLOSE: Final[int8] = 3
  RECONFIGURE_STOP: Final[int8] = 1
  RECONFIGURE_RUNNING: Final[int8] = 0
