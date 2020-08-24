from typing import List
from typing_extensions import Annotated
from alpyro_msgs import RosMessage, float64, string
from alpyro_msgs.std_msgs.header import Header


class JointJog(RosMessage):
  __msg_typ__ = "control_msgs/JointJog"
  __msg_def__ = "c3RkX21zZ3MvSGVhZGVyIGhlYWRlcgogIHVpbnQzMiBzZXEKICB0aW1lIHN0YW1wCiAgc3RyaW5nIGZyYW1lX2lkCnN0cmluZ1tdIGpvaW50X25hbWVzCmZsb2F0NjRbXSBkaXNwbGFjZW1lbnRzCmZsb2F0NjRbXSB2ZWxvY2l0aWVzCmZsb2F0NjQgZHVyYXRpb24KCg=="
  __md5_sum__ = "1685da700c8c2e1254afc92a5fb89c96"

  header: Header
  joint_names: Annotated[List[string], 0, 0]
  displacements: Annotated[List[float64], 0, 0]
  velocities: Annotated[List[float64], 0, 0]
  duration: float64
