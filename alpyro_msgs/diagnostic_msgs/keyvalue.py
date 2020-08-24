from alpyro_msgs import RosMessage, string


class KeyValue(RosMessage):
  __msg_typ__ = "diagnostic_msgs/KeyValue"
  __msg_def__ = "c3RyaW5nIGtleQpzdHJpbmcgdmFsdWUKCg=="
  __md5_sum__ = "cf57fdc6617a881a88c16e768132149c"

  key: string
  value: string
