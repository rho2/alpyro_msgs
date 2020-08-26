from alpyro_msgs import RosMessage
from alpyro_msgs.actionlib_msgs.goalid import GoalID
from alpyro_msgs.std_msgs.header import Header
from alpyro_msgs.tf2_msgs.lookuptransformgoal import LookupTransformGoal


class LookupTransformActionGoal(RosMessage):
  __msg_typ__ = "tf2_msgs/LookupTransformActionGoal"
  __msg_def__ = "c3RkX21zZ3MvSGVhZGVyIGhlYWRlcgogIHVpbnQzMiBzZXEKICB0aW1lIHN0YW1wCiAgc3RyaW5nIGZyYW1lX2lkCmFjdGlvbmxpYl9tc2dzL0dvYWxJRCBnb2FsX2lkCiAgdGltZSBzdGFtcAogIHN0cmluZyBpZAp0ZjJfbXNncy9Mb29rdXBUcmFuc2Zvcm1Hb2FsIGdvYWwKICBzdHJpbmcgdGFyZ2V0X2ZyYW1lCiAgc3RyaW5nIHNvdXJjZV9mcmFtZQogIHRpbWUgc291cmNlX3RpbWUKICBkdXJhdGlvbiB0aW1lb3V0CiAgdGltZSB0YXJnZXRfdGltZQogIHN0cmluZyBmaXhlZF9mcmFtZQogIGJvb2wgYWR2YW5jZWQKCg=="
  __md5_sum__ = "f2e7bcdb75c847978d0351a13e699da5"

  header: Header
  goal_id: GoalID
  goal: LookupTransformGoal
