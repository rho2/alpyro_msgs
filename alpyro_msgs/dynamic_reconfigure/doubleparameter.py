from alpyro_msgs import RosMessage, float64, string


class DoubleParameter(RosMessage):
  __msg_typ__ = "dynamic_reconfigure/DoubleParameter"
  __msg_def__ = "c3RyaW5nIG5hbWUKZmxvYXQ2NCB2YWx1ZQoK"
  __md5_sum__ = "d8512f27253c0f65f928a67c329cd658"

  name: string
  value: float64
