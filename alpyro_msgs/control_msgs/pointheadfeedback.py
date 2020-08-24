from alpyro_msgs import RosMessage, float64


class PointHeadFeedback(RosMessage):
  __msg_typ__ = "control_msgs/PointHeadFeedback"
  __msg_def__ = "ZmxvYXQ2NCBwb2ludGluZ19hbmdsZV9lcnJvcgoK"
  __md5_sum__ = "cce80d27fd763682da8805a73316cab4"

  pointing_angle_error: float64
