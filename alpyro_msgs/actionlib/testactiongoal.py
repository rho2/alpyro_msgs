from alpyro_msgs import RosMessage
from alpyro_msgs.actionlib.testgoal import TestGoal
from alpyro_msgs.actionlib_msgs.goalid import GoalID
from alpyro_msgs.std_msgs.header import Header


class TestActionGoal(RosMessage):
  __msg_typ__ = "actionlib/TestActionGoal"
  __msg_def__ = "c3RkX21zZ3MvSGVhZGVyIGhlYWRlcgogIHVpbnQzMiBzZXEKICB0aW1lIHN0YW1wCiAgc3RyaW5nIGZyYW1lX2lkCmFjdGlvbmxpYl9tc2dzL0dvYWxJRCBnb2FsX2lkCiAgdGltZSBzdGFtcAogIHN0cmluZyBpZAphY3Rpb25saWIvVGVzdEdvYWwgZ29hbAogIGludDMyIGdvYWwKCg=="
  __md5_sum__ = "348369c5b403676156094e8c159720bf"

  header: Header
  goal_id: GoalID
  goal: TestGoal
