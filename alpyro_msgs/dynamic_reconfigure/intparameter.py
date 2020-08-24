from alpyro_msgs import RosMessage, int32, string


class IntParameter(RosMessage):
  __msg_typ__ = "dynamic_reconfigure/IntParameter"
  __msg_def__ = "c3RyaW5nIG5hbWUKaW50MzIgdmFsdWUKCg=="
  __md5_sum__ = "65fedc7a0cbfb8db035e46194a350bf1"

  name: string
  value: int32
