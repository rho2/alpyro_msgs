from alpyro_msgs import RosMessage, duration, float64


class SingleJointPositionGoal(RosMessage):
  __msg_typ__ = "control_msgs/SingleJointPositionGoal"
  __msg_def__ = "ZmxvYXQ2NCBwb3NpdGlvbgpkdXJhdGlvbiBtaW5fZHVyYXRpb24KZmxvYXQ2NCBtYXhfdmVsb2NpdHkKCg=="
  __md5_sum__ = "fbaaa562a23a013fd5053e5f72cbb35c"

  position: float64
  min_duration: duration
  max_velocity: float64
