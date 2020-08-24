from alpyro_msgs import RosMessage, float32, int32


class AveragingFeedback(RosMessage):
  __msg_typ__ = "actionlib_tutorials/AveragingFeedback"
  __msg_def__ = "aW50MzIgc2FtcGxlCmZsb2F0MzIgZGF0YQpmbG9hdDMyIG1lYW4KZmxvYXQzMiBzdGRfZGV2Cgo="
  __md5_sum__ = "9e8dfc53c2f2a032ca33fa80ec46fd4f"

  sample: int32
  data: float32
  mean: float32
  std_dev: float32
