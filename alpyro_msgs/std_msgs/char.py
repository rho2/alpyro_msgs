from alpyro_msgs import RosMessage, uint8


class Char(RosMessage):
  __msg_typ__ = "std_msgs/Char"
  __msg_def__ = "Y2hhciBkYXRhCgo="
  __md5_sum__ = "1bf77f25acecdedba0e224b162199717"

  data: uint8
