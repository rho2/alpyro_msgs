from typing import Final
from alpyro_msgs import RosMessage
from alpyro_msgs.actionlib.twointsresult import TwoIntsResult
from alpyro_msgs.actionlib_msgs.goalstatus import GoalStatus
from alpyro_msgs.std_msgs.header import Header


class TwoIntsActionResult(RosMessage):
  __msg_typ__ = "actionlib/TwoIntsActionResult"
  __msg_def__ = "c3RkX21zZ3MvSGVhZGVyIGhlYWRlcgogIHVpbnQzMiBzZXEKICB0aW1lIHN0YW1wCiAgc3RyaW5nIGZyYW1lX2lkCmFjdGlvbmxpYl9tc2dzL0dvYWxTdGF0dXMgc3RhdHVzCiAgdWludDggUEVORElORz0wCiAgdWludDggQUNUSVZFPTEKICB1aW50OCBQUkVFTVBURUQ9MgogIHVpbnQ4IFNVQ0NFRURFRD0zCiAgdWludDggQUJPUlRFRD00CiAgdWludDggUkVKRUNURUQ9NQogIHVpbnQ4IFBSRUVNUFRJTkc9NgogIHVpbnQ4IFJFQ0FMTElORz03CiAgdWludDggUkVDQUxMRUQ9OAogIHVpbnQ4IExPU1Q9OQogIGFjdGlvbmxpYl9tc2dzL0dvYWxJRCBnb2FsX2lkCiAgICB0aW1lIHN0YW1wCiAgICBzdHJpbmcgaWQKICB1aW50OCBzdGF0dXMKICBzdHJpbmcgdGV4dAphY3Rpb25saWIvVHdvSW50c1Jlc3VsdCByZXN1bHQKICBpbnQ2NCBzdW0KCg=="
  __md5_sum__ = "3ba7dea8b8cddcae4528ade4ef74b6e7"

  header: Header
  status: GoalStatus
  result: TwoIntsResult
