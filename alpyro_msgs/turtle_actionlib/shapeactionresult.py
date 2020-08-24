from typing import Final
from alpyro_msgs import RosMessage
from alpyro_msgs.turtle_actionlib.shaperesult import ShapeResult
from alpyro_msgs.std_msgs.header import Header
from alpyro_msgs.actionlib_msgs.goalstatus import GoalStatus


class ShapeActionResult(RosMessage):
  __msg_typ__ = "turtle_actionlib/ShapeActionResult"
  __msg_def__ = "c3RkX21zZ3MvSGVhZGVyIGhlYWRlcgogIHVpbnQzMiBzZXEKICB0aW1lIHN0YW1wCiAgc3RyaW5nIGZyYW1lX2lkCmFjdGlvbmxpYl9tc2dzL0dvYWxTdGF0dXMgc3RhdHVzCiAgdWludDggUEVORElORz0wCiAgdWludDggQUNUSVZFPTEKICB1aW50OCBQUkVFTVBURUQ9MgogIHVpbnQ4IFNVQ0NFRURFRD0zCiAgdWludDggQUJPUlRFRD00CiAgdWludDggUkVKRUNURUQ9NQogIHVpbnQ4IFBSRUVNUFRJTkc9NgogIHVpbnQ4IFJFQ0FMTElORz03CiAgdWludDggUkVDQUxMRUQ9OAogIHVpbnQ4IExPU1Q9OQogIGFjdGlvbmxpYl9tc2dzL0dvYWxJRCBnb2FsX2lkCiAgICB0aW1lIHN0YW1wCiAgICBzdHJpbmcgaWQKICB1aW50OCBzdGF0dXMKICBzdHJpbmcgdGV4dAp0dXJ0bGVfYWN0aW9ubGliL1NoYXBlUmVzdWx0IHJlc3VsdAogIGZsb2F0MzIgaW50ZXJpb3JfYW5nbGUKICBmbG9hdDMyIGFwb3RoZW0KCg=="
  __md5_sum__ = "c8d13d5d140f1047a2e4d3bf5c045822"

  header: Header
  status: GoalStatus
  result: ShapeResult
