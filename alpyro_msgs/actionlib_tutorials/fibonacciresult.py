from typing import List
from typing_extensions import Annotated
from alpyro_msgs import RosMessage, int32


class FibonacciResult(RosMessage):
  __msg_typ__ = "actionlib_tutorials/FibonacciResult"
  __msg_def__ = "aW50MzJbXSBzZXF1ZW5jZQoK"
  __md5_sum__ = "b81e37d2a31925a0e8ae261a8699cb79"

  sequence: Annotated[List[int32], 0, 0]
