from typing import Final
from alpyro_msgs import RosMessage, string, uint32, uint8


class PointField(RosMessage):
  __msg_typ__ = "sensor_msgs/PointField"
  __msg_def__ = "dWludDggSU5UOD0xCnVpbnQ4IFVJTlQ4PTIKdWludDggSU5UMTY9Mwp1aW50OCBVSU5UMTY9NAp1aW50OCBJTlQzMj01CnVpbnQ4IFVJTlQzMj02CnVpbnQ4IEZMT0FUMzI9Nwp1aW50OCBGTE9BVDY0PTgKc3RyaW5nIG5hbWUKdWludDMyIG9mZnNldAp1aW50OCBkYXRhdHlwZQp1aW50MzIgY291bnQKCg=="
  __md5_sum__ = "268eacb2962780ceac86cbd17e328150"

  INT8: Final[uint8] = 1
  UINT8: Final[uint8] = 2
  INT16: Final[uint8] = 3
  UINT16: Final[uint8] = 4
  INT32: Final[uint8] = 5
  UINT32: Final[uint8] = 6
  FLOAT32: Final[uint8] = 7
  FLOAT64: Final[uint8] = 8
  name: string
  offset: uint32
  datatype: uint8
  count: uint32
