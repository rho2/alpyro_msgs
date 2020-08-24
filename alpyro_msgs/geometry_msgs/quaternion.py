from alpyro_msgs import RosMessage, float64


class Quaternion(RosMessage):
  __msg_typ__ = "geometry_msgs/Quaternion"
  __msg_def__ = "ZmxvYXQ2NCB4CmZsb2F0NjQgeQpmbG9hdDY0IHoKZmxvYXQ2NCB3Cgo="
  __md5_sum__ = "a779879fadf0160734f906b8c19c7004"

  x: float64
  y: float64
  z: float64
  w: float64
