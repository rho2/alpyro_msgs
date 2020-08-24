from alpyro_msgs import RosMessage, time


class Clock(RosMessage):
  __msg_typ__ = "rosgraph_msgs/Clock"
  __msg_def__ = "dGltZSBjbG9jawoK"
  __md5_sum__ = "a9c97c1d230cfc112e270351a944ee47"

  clock: time
