from typing import List
from typing_extensions import Annotated
from alpyro_msgs import RosMessage
from alpyro_msgs.geometry_msgs.point import Point
from alpyro_msgs.shape_msgs.meshtriangle import MeshTriangle


class Mesh(RosMessage):
  __msg_typ__ = "shape_msgs/Mesh"
  __msg_def__ = "c2hhcGVfbXNncy9NZXNoVHJpYW5nbGVbXSB0cmlhbmdsZXMKICB1aW50MzJbM10gdmVydGV4X2luZGljZXMKZ2VvbWV0cnlfbXNncy9Qb2ludFtdIHZlcnRpY2VzCiAgZmxvYXQ2NCB4CiAgZmxvYXQ2NCB5CiAgZmxvYXQ2NCB6Cgo="
  __md5_sum__ = "1ffdae9486cd3316a121c578b47a85cc"

  triangles: Annotated[List[MeshTriangle], 0, 0]
  vertices: Annotated[List[Point], 0, 0]
