from alpyro_msgs import RosMessage, float32


class Velocity(RosMessage):
  __msg_typ__ = "turtle_actionlib/Velocity"
  __msg_def__ = "ZmxvYXQzMiBsaW5lYXIKZmxvYXQzMiBhbmd1bGFyCgo="
  __md5_sum__ = "9d5c2dcd348ac8f76ce2a4307bd63a13"

  linear: float32
  angular: float32
