from typing import List
from typing_extensions import Annotated
from alpyro_msgs import RosMessage, float64, string
from alpyro_msgs.std_msgs.header import Header


class JointState(RosMessage):
  __msg_typ__ = "sensor_msgs/JointState"
  __msg_def__ = "c3RkX21zZ3MvSGVhZGVyIGhlYWRlcgogIHVpbnQzMiBzZXEKICB0aW1lIHN0YW1wCiAgc3RyaW5nIGZyYW1lX2lkCnN0cmluZ1tdIG5hbWUKZmxvYXQ2NFtdIHBvc2l0aW9uCmZsb2F0NjRbXSB2ZWxvY2l0eQpmbG9hdDY0W10gZWZmb3J0Cgo="
  __md5_sum__ = "3066dcd76a6cfaef579bd0f34173e9fd"

  header: Header
  name: Annotated[List[string], 0, 0]
  position: Annotated[List[float64], 0, 0]
  velocity: Annotated[List[float64], 0, 0]
  effort: Annotated[List[float64], 0, 0]
