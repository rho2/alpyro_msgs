from alpyro_msgs import RosMessage, float64, string


class JointTolerance(RosMessage):
  __msg_typ__ = "control_msgs/JointTolerance"
  __msg_def__ = "c3RyaW5nIG5hbWUKZmxvYXQ2NCBwb3NpdGlvbgpmbG9hdDY0IHZlbG9jaXR5CmZsb2F0NjQgYWNjZWxlcmF0aW9uCgo="
  __md5_sum__ = "f544fe9c16cf04547e135dd6063ff5be"

  name: string
  position: float64
  velocity: float64
  acceleration: float64
