from typing import List
from typing_extensions import Annotated
from alpyro_msgs import RosMessage, string, uint32, uint8
from alpyro_msgs.std_msgs.header import Header


class Image(RosMessage):
  __msg_typ__ = "sensor_msgs/Image"
  __msg_def__ = "c3RkX21zZ3MvSGVhZGVyIGhlYWRlcgogIHVpbnQzMiBzZXEKICB0aW1lIHN0YW1wCiAgc3RyaW5nIGZyYW1lX2lkCnVpbnQzMiBoZWlnaHQKdWludDMyIHdpZHRoCnN0cmluZyBlbmNvZGluZwp1aW50OCBpc19iaWdlbmRpYW4KdWludDMyIHN0ZXAKdWludDhbXSBkYXRhCgo="
  __md5_sum__ = "060021388200f6f0f447d0fcd9c64743"

  header: Header
  height: uint32
  width: uint32
  encoding: string
  is_bigendian: uint8
  step: uint32
  data: Annotated[bytes, 0, 0]
