from alpyro_msgs import RosMessage, float32, int32


class ShapeGoal(RosMessage):
  __msg_typ__ = "turtle_actionlib/ShapeGoal"
  __msg_def__ = "aW50MzIgZWRnZXMKZmxvYXQzMiByYWRpdXMKCg=="
  __md5_sum__ = "3b9202ab7292cebe5a95ab2bf6b9c091"

  edges: int32
  radius: float32
