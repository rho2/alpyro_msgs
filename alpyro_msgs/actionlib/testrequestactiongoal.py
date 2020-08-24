from typing import Final
from alpyro_msgs import RosMessage
from alpyro_msgs.actionlib_msgs.goalid import GoalID
from alpyro_msgs.std_msgs.header import Header
from alpyro_msgs.actionlib.testrequestgoal import TestRequestGoal


class TestRequestActionGoal(RosMessage):
  __msg_typ__ = "actionlib/TestRequestActionGoal"
  __msg_def__ = "c3RkX21zZ3MvSGVhZGVyIGhlYWRlcgogIHVpbnQzMiBzZXEKICB0aW1lIHN0YW1wCiAgc3RyaW5nIGZyYW1lX2lkCmFjdGlvbmxpYl9tc2dzL0dvYWxJRCBnb2FsX2lkCiAgdGltZSBzdGFtcAogIHN0cmluZyBpZAphY3Rpb25saWIvVGVzdFJlcXVlc3RHb2FsIGdvYWwKICBpbnQzMiBURVJNSU5BVEVfU1VDQ0VTUz0wCiAgaW50MzIgVEVSTUlOQVRFX0FCT1JURUQ9MQogIGludDMyIFRFUk1JTkFURV9SRUpFQ1RFRD0yCiAgaW50MzIgVEVSTUlOQVRFX0xPU0U9MwogIGludDMyIFRFUk1JTkFURV9EUk9QPTQKICBpbnQzMiBURVJNSU5BVEVfRVhDRVBUSU9OPTUKICBpbnQzMiB0ZXJtaW5hdGVfc3RhdHVzCiAgYm9vbCBpZ25vcmVfY2FuY2VsCiAgc3RyaW5nIHJlc3VsdF90ZXh0CiAgaW50MzIgdGhlX3Jlc3VsdAogIGJvb2wgaXNfc2ltcGxlX2NsaWVudAogIGR1cmF0aW9uIGRlbGF5X2FjY2VwdAogIGR1cmF0aW9uIGRlbGF5X3Rlcm1pbmF0ZQogIGR1cmF0aW9uIHBhdXNlX3N0YXR1cwoK"
  __md5_sum__ = "1889556d3fef88f821c7cb004e4251f3"

  header: Header
  goal_id: GoalID
  goal: TestRequestGoal
