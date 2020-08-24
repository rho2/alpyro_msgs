from typing import Final
from alpyro_msgs import RosMessage, float32, uint8
from alpyro_msgs.std_msgs.header import Header


class Range(RosMessage):
  __msg_typ__ = "sensor_msgs/Range"
  __msg_def__ = "dWludDggVUxUUkFTT1VORD0wCnVpbnQ4IElORlJBUkVEPTEKc3RkX21zZ3MvSGVhZGVyIGhlYWRlcgogIHVpbnQzMiBzZXEKICB0aW1lIHN0YW1wCiAgc3RyaW5nIGZyYW1lX2lkCnVpbnQ4IHJhZGlhdGlvbl90eXBlCmZsb2F0MzIgZmllbGRfb2ZfdmlldwpmbG9hdDMyIG1pbl9yYW5nZQpmbG9hdDMyIG1heF9yYW5nZQpmbG9hdDMyIHJhbmdlCgo="
  __md5_sum__ = "c005c34273dc426c67a020a87bc24148"

  ULTRASOUND: Final[uint8] = 0
  INFRARED: Final[uint8] = 1
  header: Header
  radiation_type: uint8
  field_of_view: float32
  min_range: float32
  max_range: float32
  range: float32
