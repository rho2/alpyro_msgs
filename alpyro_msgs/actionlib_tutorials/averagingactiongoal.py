from alpyro_msgs import RosMessage
from alpyro_msgs.actionlib_msgs.goalid import GoalID
from alpyro_msgs.actionlib_tutorials.averaginggoal import AveragingGoal
from alpyro_msgs.std_msgs.header import Header


class AveragingActionGoal(RosMessage):
  __msg_typ__ = "actionlib_tutorials/AveragingActionGoal"
  __msg_def__ = "c3RkX21zZ3MvSGVhZGVyIGhlYWRlcgogIHVpbnQzMiBzZXEKICB0aW1lIHN0YW1wCiAgc3RyaW5nIGZyYW1lX2lkCmFjdGlvbmxpYl9tc2dzL0dvYWxJRCBnb2FsX2lkCiAgdGltZSBzdGFtcAogIHN0cmluZyBpZAphY3Rpb25saWJfdHV0b3JpYWxzL0F2ZXJhZ2luZ0dvYWwgZ29hbAogIGludDMyIHNhbXBsZXMKCg=="
  __md5_sum__ = "1561825b734ebd6039851c501e3fb570"

  header: Header
  goal_id: GoalID
  goal: AveragingGoal
