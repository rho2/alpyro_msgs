from alpyro_msgs import RosMessage, string, time, uint32


class Header(RosMessage):
  __msg_typ__ = "std_msgs/Header"
  __msg_def__ = "dWludDMyIHNlcQp0aW1lIHN0YW1wCnN0cmluZyBmcmFtZV9pZAoK"
  __md5_sum__ = "2176decaecbce78abc3b96ef049fabed"

  seq: uint32
  stamp: time
  frame_id: string
