from typing import Final
from alpyro_msgs import RosMessage
from alpyro_msgs.actionlib_msgs.goalstatus import GoalStatus
from alpyro_msgs.control_msgs.grippercommandfeedback import GripperCommandFeedback
from alpyro_msgs.std_msgs.header import Header


class GripperCommandActionFeedback(RosMessage):
  __msg_typ__ = "control_msgs/GripperCommandActionFeedback"
  __msg_def__ = "c3RkX21zZ3MvSGVhZGVyIGhlYWRlcgogIHVpbnQzMiBzZXEKICB0aW1lIHN0YW1wCiAgc3RyaW5nIGZyYW1lX2lkCmFjdGlvbmxpYl9tc2dzL0dvYWxTdGF0dXMgc3RhdHVzCiAgdWludDggUEVORElORz0wCiAgdWludDggQUNUSVZFPTEKICB1aW50OCBQUkVFTVBURUQ9MgogIHVpbnQ4IFNVQ0NFRURFRD0zCiAgdWludDggQUJPUlRFRD00CiAgdWludDggUkVKRUNURUQ9NQogIHVpbnQ4IFBSRUVNUFRJTkc9NgogIHVpbnQ4IFJFQ0FMTElORz03CiAgdWludDggUkVDQUxMRUQ9OAogIHVpbnQ4IExPU1Q9OQogIGFjdGlvbmxpYl9tc2dzL0dvYWxJRCBnb2FsX2lkCiAgICB0aW1lIHN0YW1wCiAgICBzdHJpbmcgaWQKICB1aW50OCBzdGF0dXMKICBzdHJpbmcgdGV4dApjb250cm9sX21zZ3MvR3JpcHBlckNvbW1hbmRGZWVkYmFjayBmZWVkYmFjawogIGZsb2F0NjQgcG9zaXRpb24KICBmbG9hdDY0IGVmZm9ydAogIGJvb2wgc3RhbGxlZAogIGJvb2wgcmVhY2hlZF9nb2FsCgo="
  __md5_sum__ = "653dff30c045f5e6ff3feb3409f4558d"

  header: Header
  status: GoalStatus
  feedback: GripperCommandFeedback
