from typing import Final
from alpyro_msgs import RosMessage, string, uint8


class TF2Error(RosMessage):
  __msg_typ__ = "tf2_msgs/TF2Error"
  __msg_def__ = "dWludDggTk9fRVJST1I9MAp1aW50OCBMT09LVVBfRVJST1I9MQp1aW50OCBDT05ORUNUSVZJVFlfRVJST1I9Mgp1aW50OCBFWFRSQVBPTEFUSU9OX0VSUk9SPTMKdWludDggSU5WQUxJRF9BUkdVTUVOVF9FUlJPUj00CnVpbnQ4IFRJTUVPVVRfRVJST1I9NQp1aW50OCBUUkFOU0ZPUk1fRVJST1I9Ngp1aW50OCBlcnJvcgpzdHJpbmcgZXJyb3Jfc3RyaW5nCgo="
  __md5_sum__ = "bc6848fd6fd750c92e38575618a4917d"

  NO_ERROR: Final[uint8] = 0
  LOOKUP_ERROR: Final[uint8] = 1
  CONNECTIVITY_ERROR: Final[uint8] = 2
  EXTRAPOLATION_ERROR: Final[uint8] = 3
  INVALID_ARGUMENT_ERROR: Final[uint8] = 4
  TIMEOUT_ERROR: Final[uint8] = 5
  TRANSFORM_ERROR: Final[uint8] = 6
  error: uint8
  error_string: string
