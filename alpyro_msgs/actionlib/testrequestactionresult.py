from typing import Final
from alpyro_msgs import RosMessage
from alpyro_msgs.actionlib.testrequestresult import TestRequestResult
from alpyro_msgs.actionlib_msgs.goalstatus import GoalStatus
from alpyro_msgs.std_msgs.header import Header


class TestRequestActionResult(RosMessage):
  __msg_typ__ = "actionlib/TestRequestActionResult"
  __msg_def__ = "c3RkX21zZ3MvSGVhZGVyIGhlYWRlcgogIHVpbnQzMiBzZXEKICB0aW1lIHN0YW1wCiAgc3RyaW5nIGZyYW1lX2lkCmFjdGlvbmxpYl9tc2dzL0dvYWxTdGF0dXMgc3RhdHVzCiAgdWludDggUEVORElORz0wCiAgdWludDggQUNUSVZFPTEKICB1aW50OCBQUkVFTVBURUQ9MgogIHVpbnQ4IFNVQ0NFRURFRD0zCiAgdWludDggQUJPUlRFRD00CiAgdWludDggUkVKRUNURUQ9NQogIHVpbnQ4IFBSRUVNUFRJTkc9NgogIHVpbnQ4IFJFQ0FMTElORz03CiAgdWludDggUkVDQUxMRUQ9OAogIHVpbnQ4IExPU1Q9OQogIGFjdGlvbmxpYl9tc2dzL0dvYWxJRCBnb2FsX2lkCiAgICB0aW1lIHN0YW1wCiAgICBzdHJpbmcgaWQKICB1aW50OCBzdGF0dXMKICBzdHJpbmcgdGV4dAphY3Rpb25saWIvVGVzdFJlcXVlc3RSZXN1bHQgcmVzdWx0CiAgaW50MzIgdGhlX3Jlc3VsdAogIGJvb2wgaXNfc2ltcGxlX3NlcnZlcgoK"
  __md5_sum__ = "0476d1fdf437a3a6e7d6d0e9f5561298"

  header: Header
  status: GoalStatus
  result: TestRequestResult
