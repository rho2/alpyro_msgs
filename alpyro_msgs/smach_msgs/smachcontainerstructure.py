from typing import List
from typing_extensions import Annotated
from alpyro_msgs import RosMessage, string
from alpyro_msgs.std_msgs.header import Header


class SmachContainerStructure(RosMessage):
  __msg_typ__ = "smach_msgs/SmachContainerStructure"
  __msg_def__ = "c3RkX21zZ3MvSGVhZGVyIGhlYWRlcgogIHVpbnQzMiBzZXEKICB0aW1lIHN0YW1wCiAgc3RyaW5nIGZyYW1lX2lkCnN0cmluZyBwYXRoCnN0cmluZ1tdIGNoaWxkcmVuCnN0cmluZ1tdIGludGVybmFsX291dGNvbWVzCnN0cmluZ1tdIG91dGNvbWVzX2Zyb20Kc3RyaW5nW10gb3V0Y29tZXNfdG8Kc3RyaW5nW10gY29udGFpbmVyX291dGNvbWVzCgo="
  __md5_sum__ = "3d3d1e0d0f99779ee9e58101a5dcf7ea"

  header: Header
  path: string
  children: Annotated[List[string], 0, 0]
  internal_outcomes: Annotated[List[string], 0, 0]
  outcomes_from: Annotated[List[string], 0, 0]
  outcomes_to: Annotated[List[string], 0, 0]
  container_outcomes: Annotated[List[string], 0, 0]
