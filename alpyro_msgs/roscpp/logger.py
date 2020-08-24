from alpyro_msgs import RosMessage, string


class Logger(RosMessage):
  __msg_typ__ = "roscpp/Logger"
  __msg_def__ = "c3RyaW5nIG5hbWUKc3RyaW5nIGxldmVsCgo="
  __md5_sum__ = "a6069a2ff40db7bd32143dd66e1f408e"

  name: string
  level: string
