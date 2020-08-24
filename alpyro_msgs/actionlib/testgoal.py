from alpyro_msgs import RosMessage, int32


class TestGoal(RosMessage):
  __msg_typ__ = "actionlib/TestGoal"
  __msg_def__ = "aW50MzIgZ29hbAoK"
  __md5_sum__ = "18df0149936b7aa95588e3862476ebde"

  goal: int32
