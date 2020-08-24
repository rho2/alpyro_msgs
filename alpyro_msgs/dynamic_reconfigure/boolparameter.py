from alpyro_msgs import RosMessage, boolean, string


class BoolParameter(RosMessage):
  __msg_typ__ = "dynamic_reconfigure/BoolParameter"
  __msg_def__ = "c3RyaW5nIG5hbWUKYm9vbCB2YWx1ZQoK"
  __md5_sum__ = "23f05028c1a699fb83e22401228c3a9e"

  name: string
  value: boolean
