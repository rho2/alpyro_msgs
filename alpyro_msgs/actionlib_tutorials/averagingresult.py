from alpyro_msgs import RosMessage, float32


class AveragingResult(RosMessage):
  __msg_typ__ = "actionlib_tutorials/AveragingResult"
  __msg_def__ = "ZmxvYXQzMiBtZWFuCmZsb2F0MzIgc3RkX2RldgoK"
  __md5_sum__ = "d5c7decf6df75ffb4367a05c1bcc7612"

  mean: float32
  std_dev: float32
