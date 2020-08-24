from alpyro_msgs import RosMessage
from alpyro_msgs.geometry_msgs.vector3 import Vector3


class Accel(RosMessage):
  __msg_typ__ = "geometry_msgs/Accel"
  __msg_def__ = "Z2VvbWV0cnlfbXNncy9WZWN0b3IzIGxpbmVhcgogIGZsb2F0NjQgeAogIGZsb2F0NjQgeQogIGZsb2F0NjQgegpnZW9tZXRyeV9tc2dzL1ZlY3RvcjMgYW5ndWxhcgogIGZsb2F0NjQgeAogIGZsb2F0NjQgeQogIGZsb2F0NjQgegoK"
  __md5_sum__ = "9f195f881246fdfa2798d1d3eebca84a"

  linear: Vector3
  angular: Vector3
