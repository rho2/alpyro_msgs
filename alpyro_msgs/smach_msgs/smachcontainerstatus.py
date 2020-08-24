from typing import List
from typing_extensions import Annotated
from alpyro_msgs import RosMessage, string
from alpyro_msgs.std_msgs.header import Header


class SmachContainerStatus(RosMessage):
  __msg_typ__ = "smach_msgs/SmachContainerStatus"
  __msg_def__ = "c3RkX21zZ3MvSGVhZGVyIGhlYWRlcgogIHVpbnQzMiBzZXEKICB0aW1lIHN0YW1wCiAgc3RyaW5nIGZyYW1lX2lkCnN0cmluZyBwYXRoCnN0cmluZ1tdIGluaXRpYWxfc3RhdGVzCnN0cmluZ1tdIGFjdGl2ZV9zdGF0ZXMKc3RyaW5nIGxvY2FsX2RhdGEKc3RyaW5nIGluZm8KCg=="
  __md5_sum__ = "5ba2bb79ac19e3842d562a191f2a675b"

  header: Header
  path: string
  initial_states: Annotated[List[string], 0, 0]
  active_states: Annotated[List[string], 0, 0]
  local_data: string
  info: string
