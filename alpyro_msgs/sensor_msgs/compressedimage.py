from typing import List
from typing_extensions import Annotated
from alpyro_msgs import RosMessage, string, uint8
from alpyro_msgs.std_msgs.header import Header


class CompressedImage(RosMessage):
  __msg_typ__ = "sensor_msgs/CompressedImage"
  __msg_def__ = "c3RkX21zZ3MvSGVhZGVyIGhlYWRlcgogIHVpbnQzMiBzZXEKICB0aW1lIHN0YW1wCiAgc3RyaW5nIGZyYW1lX2lkCnN0cmluZyBmb3JtYXQKdWludDhbXSBkYXRhCgo="
  __md5_sum__ = "8f7a12909da2c9d3332d540a0977563f"

  header: Header
  format: string
  data: Annotated[bytes, 0, 0]
