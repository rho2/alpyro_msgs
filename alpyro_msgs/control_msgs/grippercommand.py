from alpyro_msgs import RosMessage, float64


class GripperCommand(RosMessage):
  __msg_typ__ = "control_msgs/GripperCommand"
  __msg_def__ = "ZmxvYXQ2NCBwb3NpdGlvbgpmbG9hdDY0IG1heF9lZmZvcnQKCg=="
  __md5_sum__ = "680acaff79486f017132a7f198d40f08"

  position: float64
  max_effort: float64
