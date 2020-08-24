from alpyro_msgs import RosMessage, float32, time, uint32
from alpyro_msgs.geometry_msgs.pose import Pose


class MapMetaData(RosMessage):
  __msg_typ__ = "nav_msgs/MapMetaData"
  __msg_def__ = "dGltZSBtYXBfbG9hZF90aW1lCmZsb2F0MzIgcmVzb2x1dGlvbgp1aW50MzIgd2lkdGgKdWludDMyIGhlaWdodApnZW9tZXRyeV9tc2dzL1Bvc2Ugb3JpZ2luCiAgZ2VvbWV0cnlfbXNncy9Qb2ludCBwb3NpdGlvbgogICAgZmxvYXQ2NCB4CiAgICBmbG9hdDY0IHkKICAgIGZsb2F0NjQgegogIGdlb21ldHJ5X21zZ3MvUXVhdGVybmlvbiBvcmllbnRhdGlvbgogICAgZmxvYXQ2NCB4CiAgICBmbG9hdDY0IHkKICAgIGZsb2F0NjQgegogICAgZmxvYXQ2NCB3Cgo="
  __md5_sum__ = "10cfc8a2818024d3248802c00c95f11b"

  map_load_time: time
  resolution: float32
  width: uint32
  height: uint32
  origin: Pose
