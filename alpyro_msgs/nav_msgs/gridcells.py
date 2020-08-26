from typing import List
from typing_extensions import Annotated
from alpyro_msgs import RosMessage, float32
from alpyro_msgs.geometry_msgs.point import Point
from alpyro_msgs.std_msgs.header import Header


class GridCells(RosMessage):
  __msg_typ__ = "nav_msgs/GridCells"
  __msg_def__ = "c3RkX21zZ3MvSGVhZGVyIGhlYWRlcgogIHVpbnQzMiBzZXEKICB0aW1lIHN0YW1wCiAgc3RyaW5nIGZyYW1lX2lkCmZsb2F0MzIgY2VsbF93aWR0aApmbG9hdDMyIGNlbGxfaGVpZ2h0Cmdlb21ldHJ5X21zZ3MvUG9pbnRbXSBjZWxscwogIGZsb2F0NjQgeAogIGZsb2F0NjQgeQogIGZsb2F0NjQgegoK"
  __md5_sum__ = "b9e4f5df6d28e272ebde00a3994830f5"

  header: Header
  cell_width: float32
  cell_height: float32
  cells: Annotated[List[Point], 0, 0]
