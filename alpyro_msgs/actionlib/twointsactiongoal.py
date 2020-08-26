from alpyro_msgs import RosMessage
from alpyro_msgs.actionlib.twointsgoal import TwoIntsGoal
from alpyro_msgs.actionlib_msgs.goalid import GoalID
from alpyro_msgs.std_msgs.header import Header


class TwoIntsActionGoal(RosMessage):
  __msg_typ__ = "actionlib/TwoIntsActionGoal"
  __msg_def__ = "c3RkX21zZ3MvSGVhZGVyIGhlYWRlcgogIHVpbnQzMiBzZXEKICB0aW1lIHN0YW1wCiAgc3RyaW5nIGZyYW1lX2lkCmFjdGlvbmxpYl9tc2dzL0dvYWxJRCBnb2FsX2lkCiAgdGltZSBzdGFtcAogIHN0cmluZyBpZAphY3Rpb25saWIvVHdvSW50c0dvYWwgZ29hbAogIGludDY0IGEKICBpbnQ2NCBiCgo="
  __md5_sum__ = "684a2db55d6ffb8046fb9d6764ce0860"

  header: Header
  goal_id: GoalID
  goal: TwoIntsGoal
