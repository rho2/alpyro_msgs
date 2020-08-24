from alpyro_msgs import RosMessage, boolean, float64


class GripperCommandFeedback(RosMessage):
  __msg_typ__ = "control_msgs/GripperCommandFeedback"
  __msg_def__ = "ZmxvYXQ2NCBwb3NpdGlvbgpmbG9hdDY0IGVmZm9ydApib29sIHN0YWxsZWQKYm9vbCByZWFjaGVkX2dvYWwKCg=="
  __md5_sum__ = "e4cbff56d3562bcf113da5a5adeef91f"

  position: float64
  effort: float64
  stalled: boolean
  reached_goal: boolean
