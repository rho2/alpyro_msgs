from typing import List
from typing_extensions import Annotated
from alpyro_msgs import RosMessage, uint32


class MeshTriangle(RosMessage):
  __msg_typ__ = "shape_msgs/MeshTriangle"
  __msg_def__ = "dWludDMyWzNdIHZlcnRleF9pbmRpY2VzCgo="
  __md5_sum__ = "23688b2e6d2de3d32fe8af104a903253"

  vertex_indices: Annotated[List[uint32], 3, 0]
