from alpyro_msgs import RosMessage, string, uint32


class MultiArrayDimension(RosMessage):
  __msg_typ__ = "std_msgs/MultiArrayDimension"
  __msg_def__ = "c3RyaW5nIGxhYmVsCnVpbnQzMiBzaXplCnVpbnQzMiBzdHJpZGUKCg=="
  __md5_sum__ = "4cd0c83a8683deae40ecdac60e53bfa8"

  label: string
  size: uint32
  stride: uint32
