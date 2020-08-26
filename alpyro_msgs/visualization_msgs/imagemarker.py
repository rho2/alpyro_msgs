from typing import List
from typing_extensions import Annotated
from typing import Final
from alpyro_msgs import RosMessage, duration, float32, int32, string, uint8
from alpyro_msgs.geometry_msgs.point import Point
from alpyro_msgs.std_msgs.colorrgba import ColorRGBA
from alpyro_msgs.std_msgs.header import Header


class ImageMarker(RosMessage):
  __msg_typ__ = "visualization_msgs/ImageMarker"
  __msg_def__ = "dWludDggQ0lSQ0xFPTAKdWludDggTElORV9TVFJJUD0xCnVpbnQ4IExJTkVfTElTVD0yCnVpbnQ4IFBPTFlHT049Mwp1aW50OCBQT0lOVFM9NAp1aW50OCBBREQ9MAp1aW50OCBSRU1PVkU9MQpzdGRfbXNncy9IZWFkZXIgaGVhZGVyCiAgdWludDMyIHNlcQogIHRpbWUgc3RhbXAKICBzdHJpbmcgZnJhbWVfaWQKc3RyaW5nIG5zCmludDMyIGlkCmludDMyIHR5cGUKaW50MzIgYWN0aW9uCmdlb21ldHJ5X21zZ3MvUG9pbnQgcG9zaXRpb24KICBmbG9hdDY0IHgKICBmbG9hdDY0IHkKICBmbG9hdDY0IHoKZmxvYXQzMiBzY2FsZQpzdGRfbXNncy9Db2xvclJHQkEgb3V0bGluZV9jb2xvcgogIGZsb2F0MzIgcgogIGZsb2F0MzIgZwogIGZsb2F0MzIgYgogIGZsb2F0MzIgYQp1aW50OCBmaWxsZWQKc3RkX21zZ3MvQ29sb3JSR0JBIGZpbGxfY29sb3IKICBmbG9hdDMyIHIKICBmbG9hdDMyIGcKICBmbG9hdDMyIGIKICBmbG9hdDMyIGEKZHVyYXRpb24gbGlmZXRpbWUKZ2VvbWV0cnlfbXNncy9Qb2ludFtdIHBvaW50cwogIGZsb2F0NjQgeAogIGZsb2F0NjQgeQogIGZsb2F0NjQgegpzdGRfbXNncy9Db2xvclJHQkFbXSBvdXRsaW5lX2NvbG9ycwogIGZsb2F0MzIgcgogIGZsb2F0MzIgZwogIGZsb2F0MzIgYgogIGZsb2F0MzIgYQoK"
  __md5_sum__ = "1de93c67ec8858b831025a08fbf1b35c"

  CIRCLE: Final[uint8] = 0
  LINE_STRIP: Final[uint8] = 1
  LINE_LIST: Final[uint8] = 2
  POLYGON: Final[uint8] = 3
  POINTS: Final[uint8] = 4
  ADD: Final[uint8] = 0
  REMOVE: Final[uint8] = 1
  header: Header
  ns: string
  id: int32
  type: int32
  action: int32
  position: Point
  scale: float32
  outline_color: ColorRGBA
  filled: uint8
  fill_color: ColorRGBA
  lifetime: duration
  points: Annotated[List[Point], 0, 0]
  outline_colors: Annotated[List[ColorRGBA], 0, 0]
