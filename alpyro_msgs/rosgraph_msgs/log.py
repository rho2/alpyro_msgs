from typing import List
from typing_extensions import Annotated
from typing import Final
from alpyro_msgs import RosMessage, int8, string, uint32
from alpyro_msgs.std_msgs.header import Header


class Log(RosMessage):
  __msg_typ__ = "rosgraph_msgs/Log"
  __msg_def__ = "Ynl0ZSBERUJVRz0xCmJ5dGUgSU5GTz0yCmJ5dGUgV0FSTj00CmJ5dGUgRVJST1I9OApieXRlIEZBVEFMPTE2CnN0ZF9tc2dzL0hlYWRlciBoZWFkZXIKICB1aW50MzIgc2VxCiAgdGltZSBzdGFtcAogIHN0cmluZyBmcmFtZV9pZApieXRlIGxldmVsCnN0cmluZyBuYW1lCnN0cmluZyBtc2cKc3RyaW5nIGZpbGUKc3RyaW5nIGZ1bmN0aW9uCnVpbnQzMiBsaW5lCnN0cmluZ1tdIHRvcGljcwoK"
  __md5_sum__ = "acffd30cd6b6de30f120938c17c593fb"

  DEBUG: Final[int8] = 1
  INFO: Final[int8] = 2
  WARN: Final[int8] = 4
  ERROR: Final[int8] = 8
  FATAL: Final[int8] = 16
  header: Header
  level: int8
  name: string
  msg: string
  file: string
  function: string
  line: uint32
  topics: Annotated[List[string], 0, 0]
