from alpyro_msgs import RosMessage, float64


class Pose2D(RosMessage):
  __msg_typ__ = "geometry_msgs/Pose2D"
  __msg_def__ = "ZmxvYXQ2NCB4CmZsb2F0NjQgeQpmbG9hdDY0IHRoZXRhCgo="
  __md5_sum__ = "938fa65709584ad8e77d238529be13b8"

  x: float64
  y: float64
  theta: float64
