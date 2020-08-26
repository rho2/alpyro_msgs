from typing import Final
from alpyro_msgs import RosMessage
from alpyro_msgs.actionlib.twointsfeedback import TwoIntsFeedback
from alpyro_msgs.actionlib_msgs.goalstatus import GoalStatus
from alpyro_msgs.std_msgs.header import Header


class TwoIntsActionFeedback(RosMessage):
  __msg_typ__ = "actionlib/TwoIntsActionFeedback"
  __msg_def__ = "c3RkX21zZ3MvSGVhZGVyIGhlYWRlcgogIHVpbnQzMiBzZXEKICB0aW1lIHN0YW1wCiAgc3RyaW5nIGZyYW1lX2lkCmFjdGlvbmxpYl9tc2dzL0dvYWxTdGF0dXMgc3RhdHVzCiAgdWludDggUEVORElORz0wCiAgdWludDggQUNUSVZFPTEKICB1aW50OCBQUkVFTVBURUQ9MgogIHVpbnQ4IFNVQ0NFRURFRD0zCiAgdWludDggQUJPUlRFRD00CiAgdWludDggUkVKRUNURUQ9NQogIHVpbnQ4IFBSRUVNUFRJTkc9NgogIHVpbnQ4IFJFQ0FMTElORz03CiAgdWludDggUkVDQUxMRUQ9OAogIHVpbnQ4IExPU1Q9OQogIGFjdGlvbmxpYl9tc2dzL0dvYWxJRCBnb2FsX2lkCiAgICB0aW1lIHN0YW1wCiAgICBzdHJpbmcgaWQKICB1aW50OCBzdGF0dXMKICBzdHJpbmcgdGV4dAphY3Rpb25saWIvVHdvSW50c0ZlZWRiYWNrIGZlZWRiYWNrCgo="
  __md5_sum__ = "aae20e09065c3809e8a8e87c4c8953fd"

  header: Header
  status: GoalStatus
  feedback: TwoIntsFeedback
