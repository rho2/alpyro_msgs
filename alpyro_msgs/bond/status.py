from alpyro_msgs import RosMessage, boolean, float32, string
from alpyro_msgs.std_msgs.header import Header


class Status(RosMessage):
  __msg_typ__ = "bond/Status"
  __msg_def__ = "c3RkX21zZ3MvSGVhZGVyIGhlYWRlcgogIHVpbnQzMiBzZXEKICB0aW1lIHN0YW1wCiAgc3RyaW5nIGZyYW1lX2lkCnN0cmluZyBpZApzdHJpbmcgaW5zdGFuY2VfaWQKYm9vbCBhY3RpdmUKZmxvYXQzMiBoZWFydGJlYXRfdGltZW91dApmbG9hdDMyIGhlYXJ0YmVhdF9wZXJpb2QKCg=="
  __md5_sum__ = "eacc84bf5d65b6777d4c50f463dfb9c8"

  header: Header
  id: string
  instance_id: string
  active: boolean
  heartbeat_timeout: float32
  heartbeat_period: float32
