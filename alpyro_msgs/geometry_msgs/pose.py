from alpyro_msgs import RosMessage
from alpyro_msgs.geometry_msgs.point import Point
from alpyro_msgs.geometry_msgs.quaternion import Quaternion


class Pose(RosMessage):
  __msg_typ__ = "geometry_msgs/Pose"
  __msg_def__ = "Z2VvbWV0cnlfbXNncy9Qb2ludCBwb3NpdGlvbgogIGZsb2F0NjQgeAogIGZsb2F0NjQgeQogIGZsb2F0NjQgegpnZW9tZXRyeV9tc2dzL1F1YXRlcm5pb24gb3JpZW50YXRpb24KICBmbG9hdDY0IHgKICBmbG9hdDY0IHkKICBmbG9hdDY0IHoKICBmbG9hdDY0IHcKCg=="
  __md5_sum__ = "e45d45a5a1ce597b249e23fb30fc871f"

  position: Point
  orientation: Quaternion
