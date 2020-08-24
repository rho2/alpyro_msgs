from alpyro_msgs import RosMessage, int32


class TestResult(RosMessage):
  __msg_typ__ = "actionlib/TestResult"
  __msg_def__ = "aW50MzIgcmVzdWx0Cgo="
  __md5_sum__ = "034a8e20d6a306665e3a5b340fab3f09"

  result: int32
