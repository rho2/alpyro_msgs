from typing import Final
from alpyro_msgs import RosMessage
from alpyro_msgs.actionlib_msgs.goalstatus import GoalStatus
from alpyro_msgs.control_msgs.singlejointpositionresult import SingleJointPositionResult
from alpyro_msgs.std_msgs.header import Header


class SingleJointPositionActionResult(RosMessage):
  __msg_typ__ = "control_msgs/SingleJointPositionActionResult"
  __msg_def__ = "c3RkX21zZ3MvSGVhZGVyIGhlYWRlcgogIHVpbnQzMiBzZXEKICB0aW1lIHN0YW1wCiAgc3RyaW5nIGZyYW1lX2lkCmFjdGlvbmxpYl9tc2dzL0dvYWxTdGF0dXMgc3RhdHVzCiAgdWludDggUEVORElORz0wCiAgdWludDggQUNUSVZFPTEKICB1aW50OCBQUkVFTVBURUQ9MgogIHVpbnQ4IFNVQ0NFRURFRD0zCiAgdWludDggQUJPUlRFRD00CiAgdWludDggUkVKRUNURUQ9NQogIHVpbnQ4IFBSRUVNUFRJTkc9NgogIHVpbnQ4IFJFQ0FMTElORz03CiAgdWludDggUkVDQUxMRUQ9OAogIHVpbnQ4IExPU1Q9OQogIGFjdGlvbmxpYl9tc2dzL0dvYWxJRCBnb2FsX2lkCiAgICB0aW1lIHN0YW1wCiAgICBzdHJpbmcgaWQKICB1aW50OCBzdGF0dXMKICBzdHJpbmcgdGV4dApjb250cm9sX21zZ3MvU2luZ2xlSm9pbnRQb3NpdGlvblJlc3VsdCByZXN1bHQKCg=="
  __md5_sum__ = "1eb06eeff08fa7ea874431638cb52332"

  header: Header
  status: GoalStatus
  result: SingleJointPositionResult
