from alpyro_msgs import RosMessage, boolean, int32, string


class GroupState(RosMessage):
  __msg_typ__ = "dynamic_reconfigure/GroupState"
  __msg_def__ = "c3RyaW5nIG5hbWUKYm9vbCBzdGF0ZQppbnQzMiBpZAppbnQzMiBwYXJlbnQKCg=="
  __md5_sum__ = "a2d87f51dc22930325041a2f8b1571f8"

  name: string
  state: boolean
  id: int32
  parent: int32
