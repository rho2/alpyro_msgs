from alpyro_msgs import RosMessage, string, time


class GoalID(RosMessage):
  __msg_typ__ = "actionlib_msgs/GoalID"
  __msg_def__ = "dGltZSBzdGFtcApzdHJpbmcgaWQKCg=="
  __md5_sum__ = "302881f31927c1df708a2dbab0e80ee8"

  stamp: time
  id: string
