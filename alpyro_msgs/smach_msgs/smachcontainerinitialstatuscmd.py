from typing import List
from typing_extensions import Annotated
from alpyro_msgs import RosMessage, string


class SmachContainerInitialStatusCmd(RosMessage):
  __msg_typ__ = "smach_msgs/SmachContainerInitialStatusCmd"
  __msg_def__ = "c3RyaW5nIHBhdGgKc3RyaW5nW10gaW5pdGlhbF9zdGF0ZXMKc3RyaW5nIGxvY2FsX2RhdGEKCg=="
  __md5_sum__ = "45f8cf31fc29b829db77f23001f788d6"

  path: string
  initial_states: Annotated[List[string], 0, 0]
  local_data: string
