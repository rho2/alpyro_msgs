from typing import List
from typing_extensions import Annotated
from typing import Final
from alpyro_msgs import RosMessage, boolean, duration, int32, string, uint8
from alpyro_msgs.geometry_msgs.point import Point
from alpyro_msgs.geometry_msgs.pose import Pose
from alpyro_msgs.geometry_msgs.vector3 import Vector3
from alpyro_msgs.std_msgs.colorrgba import ColorRGBA
from alpyro_msgs.std_msgs.header import Header


class Marker(RosMessage):
  __msg_typ__ = "visualization_msgs/Marker"
  __msg_def__ = "dWludDggQVJST1c9MAp1aW50OCBDVUJFPTEKdWludDggU1BIRVJFPTIKdWludDggQ1lMSU5ERVI9Mwp1aW50OCBMSU5FX1NUUklQPTQKdWludDggTElORV9MSVNUPTUKdWludDggQ1VCRV9MSVNUPTYKdWludDggU1BIRVJFX0xJU1Q9Nwp1aW50OCBQT0lOVFM9OAp1aW50OCBURVhUX1ZJRVdfRkFDSU5HPTkKdWludDggTUVTSF9SRVNPVVJDRT0xMAp1aW50OCBUUklBTkdMRV9MSVNUPTExCnVpbnQ4IEFERD0wCnVpbnQ4IE1PRElGWT0wCnVpbnQ4IERFTEVURT0yCnVpbnQ4IERFTEVURUFMTD0zCnN0ZF9tc2dzL0hlYWRlciBoZWFkZXIKICB1aW50MzIgc2VxCiAgdGltZSBzdGFtcAogIHN0cmluZyBmcmFtZV9pZApzdHJpbmcgbnMKaW50MzIgaWQKaW50MzIgdHlwZQppbnQzMiBhY3Rpb24KZ2VvbWV0cnlfbXNncy9Qb3NlIHBvc2UKICBnZW9tZXRyeV9tc2dzL1BvaW50IHBvc2l0aW9uCiAgICBmbG9hdDY0IHgKICAgIGZsb2F0NjQgeQogICAgZmxvYXQ2NCB6CiAgZ2VvbWV0cnlfbXNncy9RdWF0ZXJuaW9uIG9yaWVudGF0aW9uCiAgICBmbG9hdDY0IHgKICAgIGZsb2F0NjQgeQogICAgZmxvYXQ2NCB6CiAgICBmbG9hdDY0IHcKZ2VvbWV0cnlfbXNncy9WZWN0b3IzIHNjYWxlCiAgZmxvYXQ2NCB4CiAgZmxvYXQ2NCB5CiAgZmxvYXQ2NCB6CnN0ZF9tc2dzL0NvbG9yUkdCQSBjb2xvcgogIGZsb2F0MzIgcgogIGZsb2F0MzIgZwogIGZsb2F0MzIgYgogIGZsb2F0MzIgYQpkdXJhdGlvbiBsaWZldGltZQpib29sIGZyYW1lX2xvY2tlZApnZW9tZXRyeV9tc2dzL1BvaW50W10gcG9pbnRzCiAgZmxvYXQ2NCB4CiAgZmxvYXQ2NCB5CiAgZmxvYXQ2NCB6CnN0ZF9tc2dzL0NvbG9yUkdCQVtdIGNvbG9ycwogIGZsb2F0MzIgcgogIGZsb2F0MzIgZwogIGZsb2F0MzIgYgogIGZsb2F0MzIgYQpzdHJpbmcgdGV4dApzdHJpbmcgbWVzaF9yZXNvdXJjZQpib29sIG1lc2hfdXNlX2VtYmVkZGVkX21hdGVyaWFscwoK"
  __md5_sum__ = "4048c9de2a16f4ae8e0538085ebf1b97"

  ARROW: Final[uint8] = 0
  CUBE: Final[uint8] = 1
  SPHERE: Final[uint8] = 2
  CYLINDER: Final[uint8] = 3
  LINE_STRIP: Final[uint8] = 4
  LINE_LIST: Final[uint8] = 5
  CUBE_LIST: Final[uint8] = 6
  SPHERE_LIST: Final[uint8] = 7
  POINTS: Final[uint8] = 8
  TEXT_VIEW_FACING: Final[uint8] = 9
  MESH_RESOURCE: Final[uint8] = 10
  TRIANGLE_LIST: Final[uint8] = 11
  ADD: Final[uint8] = 0
  MODIFY: Final[uint8] = 0
  DELETE: Final[uint8] = 2
  DELETEALL: Final[uint8] = 3
  header: Header
  ns: string
  id: int32
  type: int32
  action: int32
  pose: Pose
  scale: Vector3
  color: ColorRGBA
  lifetime: duration
  frame_locked: boolean
  points: Annotated[List[Point], 0, 0]
  colors: Annotated[List[ColorRGBA], 0, 0]
  text: string
  mesh_resource: string
  mesh_use_embedded_materials: boolean
