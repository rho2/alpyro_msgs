from typing import Final
from alpyro_msgs import RosMessage
from alpyro_msgs.std_msgs.header import Header
from alpyro_msgs.tf2_msgs.lookuptransformresult import LookupTransformResult
from alpyro_msgs.actionlib_msgs.goalstatus import GoalStatus


class LookupTransformActionResult(RosMessage):
  __msg_typ__ = "tf2_msgs/LookupTransformActionResult"
  __msg_def__ = "c3RkX21zZ3MvSGVhZGVyIGhlYWRlcgogIHVpbnQzMiBzZXEKICB0aW1lIHN0YW1wCiAgc3RyaW5nIGZyYW1lX2lkCmFjdGlvbmxpYl9tc2dzL0dvYWxTdGF0dXMgc3RhdHVzCiAgdWludDggUEVORElORz0wCiAgdWludDggQUNUSVZFPTEKICB1aW50OCBQUkVFTVBURUQ9MgogIHVpbnQ4IFNVQ0NFRURFRD0zCiAgdWludDggQUJPUlRFRD00CiAgdWludDggUkVKRUNURUQ9NQogIHVpbnQ4IFBSRUVNUFRJTkc9NgogIHVpbnQ4IFJFQ0FMTElORz03CiAgdWludDggUkVDQUxMRUQ9OAogIHVpbnQ4IExPU1Q9OQogIGFjdGlvbmxpYl9tc2dzL0dvYWxJRCBnb2FsX2lkCiAgICB0aW1lIHN0YW1wCiAgICBzdHJpbmcgaWQKICB1aW50OCBzdGF0dXMKICBzdHJpbmcgdGV4dAp0ZjJfbXNncy9Mb29rdXBUcmFuc2Zvcm1SZXN1bHQgcmVzdWx0CiAgZ2VvbWV0cnlfbXNncy9UcmFuc2Zvcm1TdGFtcGVkIHRyYW5zZm9ybQogICAgc3RkX21zZ3MvSGVhZGVyIGhlYWRlcgogICAgICB1aW50MzIgc2VxCiAgICAgIHRpbWUgc3RhbXAKICAgICAgc3RyaW5nIGZyYW1lX2lkCiAgICBzdHJpbmcgY2hpbGRfZnJhbWVfaWQKICAgIGdlb21ldHJ5X21zZ3MvVHJhbnNmb3JtIHRyYW5zZm9ybQogICAgICBnZW9tZXRyeV9tc2dzL1ZlY3RvcjMgdHJhbnNsYXRpb24KICAgICAgICBmbG9hdDY0IHgKICAgICAgICBmbG9hdDY0IHkKICAgICAgICBmbG9hdDY0IHoKICAgICAgZ2VvbWV0cnlfbXNncy9RdWF0ZXJuaW9uIHJvdGF0aW9uCiAgICAgICAgZmxvYXQ2NCB4CiAgICAgICAgZmxvYXQ2NCB5CiAgICAgICAgZmxvYXQ2NCB6CiAgICAgICAgZmxvYXQ2NCB3CiAgdGYyX21zZ3MvVEYyRXJyb3IgZXJyb3IKICAgIHVpbnQ4IE5PX0VSUk9SPTAKICAgIHVpbnQ4IExPT0tVUF9FUlJPUj0xCiAgICB1aW50OCBDT05ORUNUSVZJVFlfRVJST1I9MgogICAgdWludDggRVhUUkFQT0xBVElPTl9FUlJPUj0zCiAgICB1aW50OCBJTlZBTElEX0FSR1VNRU5UX0VSUk9SPTQKICAgIHVpbnQ4IFRJTUVPVVRfRVJST1I9NQogICAgdWludDggVFJBTlNGT1JNX0VSUk9SPTYKICAgIHVpbnQ4IGVycm9yCiAgICBzdHJpbmcgZXJyb3Jfc3RyaW5nCgo="
  __md5_sum__ = "ac26ce75a41384fa8bb4dc10f491ab90"

  header: Header
  status: GoalStatus
  result: LookupTransformResult
