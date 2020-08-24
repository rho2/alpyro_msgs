from alpyro_msgs import RosMessage, float32


class ShapeResult(RosMessage):
  __msg_typ__ = "turtle_actionlib/ShapeResult"
  __msg_def__ = "ZmxvYXQzMiBpbnRlcmlvcl9hbmdsZQpmbG9hdDMyIGFwb3RoZW0KCg=="
  __md5_sum__ = "b06c6e2225f820dbc644270387cd1a7c"

  interior_angle: float32
  apothem: float32
