from alpyro_msgs import RosMessage, string


class StrParameter(RosMessage):
  __msg_typ__ = "dynamic_reconfigure/StrParameter"
  __msg_def__ = "c3RyaW5nIG5hbWUKc3RyaW5nIHZhbHVlCgo="
  __md5_sum__ = "bc6ccc4a57f61779c8eaae61e9f422e0"

  name: string
  value: string
