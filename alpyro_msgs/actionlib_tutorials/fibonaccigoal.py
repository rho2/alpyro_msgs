from alpyro_msgs import RosMessage, int32


class FibonacciGoal(RosMessage):
  __msg_typ__ = "actionlib_tutorials/FibonacciGoal"
  __msg_def__ = "aW50MzIgb3JkZXIKCg=="
  __md5_sum__ = "6889063349a00b249bd1661df429d822"

  order: int32
