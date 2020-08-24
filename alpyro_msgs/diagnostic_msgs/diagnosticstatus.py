from typing import List
from typing_extensions import Annotated
from typing import Final
from alpyro_msgs import RosMessage, int8, string
from alpyro_msgs.diagnostic_msgs.keyvalue import KeyValue


class DiagnosticStatus(RosMessage):
  __msg_typ__ = "diagnostic_msgs/DiagnosticStatus"
  __msg_def__ = "Ynl0ZSBPSz0wCmJ5dGUgV0FSTj0xCmJ5dGUgRVJST1I9MgpieXRlIFNUQUxFPTMKYnl0ZSBsZXZlbApzdHJpbmcgbmFtZQpzdHJpbmcgbWVzc2FnZQpzdHJpbmcgaGFyZHdhcmVfaWQKZGlhZ25vc3RpY19tc2dzL0tleVZhbHVlW10gdmFsdWVzCiAgc3RyaW5nIGtleQogIHN0cmluZyB2YWx1ZQoK"
  __md5_sum__ = "d0ce08bc6e5ba34c7754f563a9cabaf1"

  OK: Final[int8] = 0
  WARN: Final[int8] = 1
  ERROR: Final[int8] = 2
  STALE: Final[int8] = 3
  level: int8
  name: string
  message: string
  hardware_id: string
  values: Annotated[List[KeyValue], 0, 0]
