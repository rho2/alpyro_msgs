from typing import Final
from alpyro_msgs import RosMessage, boolean, duration, int32, string


class TestRequestGoal(RosMessage):
  __msg_typ__ = "actionlib/TestRequestGoal"
  __msg_def__ = "aW50MzIgVEVSTUlOQVRFX1NVQ0NFU1M9MAppbnQzMiBURVJNSU5BVEVfQUJPUlRFRD0xCmludDMyIFRFUk1JTkFURV9SRUpFQ1RFRD0yCmludDMyIFRFUk1JTkFURV9MT1NFPTMKaW50MzIgVEVSTUlOQVRFX0RST1A9NAppbnQzMiBURVJNSU5BVEVfRVhDRVBUSU9OPTUKaW50MzIgdGVybWluYXRlX3N0YXR1cwpib29sIGlnbm9yZV9jYW5jZWwKc3RyaW5nIHJlc3VsdF90ZXh0CmludDMyIHRoZV9yZXN1bHQKYm9vbCBpc19zaW1wbGVfY2xpZW50CmR1cmF0aW9uIGRlbGF5X2FjY2VwdApkdXJhdGlvbiBkZWxheV90ZXJtaW5hdGUKZHVyYXRpb24gcGF1c2Vfc3RhdHVzCgo="
  __md5_sum__ = "db5d00ba98302d6c6dd3737e9a03ceea"

  TERMINATE_SUCCESS: Final[int32] = 0
  TERMINATE_ABORTED: Final[int32] = 1
  TERMINATE_REJECTED: Final[int32] = 2
  TERMINATE_LOSE: Final[int32] = 3
  TERMINATE_DROP: Final[int32] = 4
  TERMINATE_EXCEPTION: Final[int32] = 5
  terminate_status: int32
  ignore_cancel: boolean
  result_text: string
  the_result: int32
  is_simple_client: boolean
  delay_accept: duration
  delay_terminate: duration
  pause_status: duration
