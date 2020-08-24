from alpyro_msgs import RosMessage, string
from alpyro_msgs.std_msgs.header import Header


class HeaderString(RosMessage):
  __msg_typ__ = "rospy_tutorials/HeaderString"
  __msg_def__ = "c3RkX21zZ3MvSGVhZGVyIGhlYWRlcgogIHVpbnQzMiBzZXEKICB0aW1lIHN0YW1wCiAgc3RyaW5nIGZyYW1lX2lkCnN0cmluZyBkYXRhCgo="
  __md5_sum__ = "c99a9440709e4d4a9716d55b8270d5e7"

  header: Header
  data: string
