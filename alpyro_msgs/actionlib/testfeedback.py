from alpyro_msgs import RosMessage, int32


class TestFeedback(RosMessage):
  __msg_typ__ = "actionlib/TestFeedback"
  __msg_def__ = "aW50MzIgZmVlZGJhY2sKCg=="
  __md5_sum__ = "49ceb5b32ea3af22073ede4a0328249e"

  feedback: int32
