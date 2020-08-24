from alpyro_msgs import RosMessage, int64


class TwoIntsGoal(RosMessage):
  __msg_typ__ = "actionlib/TwoIntsGoal"
  __msg_def__ = "aW50NjQgYQppbnQ2NCBiCgo="
  __md5_sum__ = "36d09b846be0b371c5f190354dd3153e"

  a: int64
  b: int64
