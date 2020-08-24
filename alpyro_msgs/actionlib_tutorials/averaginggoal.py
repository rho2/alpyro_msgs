from alpyro_msgs import RosMessage, int32


class AveragingGoal(RosMessage):
  __msg_typ__ = "actionlib_tutorials/AveragingGoal"
  __msg_def__ = "aW50MzIgc2FtcGxlcwoK"
  __md5_sum__ = "32c9b10ef9b253faa93b93f564762c8f"

  samples: int32
