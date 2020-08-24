from alpyro_msgs import RosMessage, int64


class TwoIntsResult(RosMessage):
  __msg_typ__ = "actionlib/TwoIntsResult"
  __msg_def__ = "aW50NjQgc3VtCgo="
  __md5_sum__ = "b88405221c77b1878a3cbbfff53428d7"

  sum: int64
