from alpyro_msgs import RosMessage, string, uint32


class ParamDescription(RosMessage):
  __msg_typ__ = "dynamic_reconfigure/ParamDescription"
  __msg_def__ = "c3RyaW5nIG5hbWUKc3RyaW5nIHR5cGUKdWludDMyIGxldmVsCnN0cmluZyBkZXNjcmlwdGlvbgpzdHJpbmcgZWRpdF9tZXRob2QKCg=="
  __md5_sum__ = "7434fcb9348c13054e0c3b267c8cb34d"

  name: string
  type: string
  level: uint32
  description: string
  edit_method: string
