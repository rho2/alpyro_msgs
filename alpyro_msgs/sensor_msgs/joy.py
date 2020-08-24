from typing import List
from typing_extensions import Annotated
from alpyro_msgs import RosMessage, float32, int32
from alpyro_msgs.std_msgs.header import Header


class Joy(RosMessage):
  __msg_typ__ = "sensor_msgs/Joy"
  __msg_def__ = "c3RkX21zZ3MvSGVhZGVyIGhlYWRlcgogIHVpbnQzMiBzZXEKICB0aW1lIHN0YW1wCiAgc3RyaW5nIGZyYW1lX2lkCmZsb2F0MzJbXSBheGVzCmludDMyW10gYnV0dG9ucwoK"
  __md5_sum__ = "5a9ea5f83505693b71e785041e67a8bb"

  header: Header
  axes: Annotated[List[float32], 0, 0]
  buttons: Annotated[List[int32], 0, 0]
