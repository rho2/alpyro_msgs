from typing import List
from typing_extensions import Annotated
from alpyro_msgs import RosMessage, int32, int8, uint32
from alpyro_msgs.std_msgs.header import Header


class OccupancyGridUpdate(RosMessage):
  __msg_typ__ = "map_msgs/OccupancyGridUpdate"
  __msg_def__ = "c3RkX21zZ3MvSGVhZGVyIGhlYWRlcgogIHVpbnQzMiBzZXEKICB0aW1lIHN0YW1wCiAgc3RyaW5nIGZyYW1lX2lkCmludDMyIHgKaW50MzIgeQp1aW50MzIgd2lkdGgKdWludDMyIGhlaWdodAppbnQ4W10gZGF0YQoK"
  __md5_sum__ = "b295be292b335c34718bd939deebe1c9"

  header: Header
  x: int32
  y: int32
  width: uint32
  height: uint32
  data: Annotated[List[int8], 0, 0]
