from alpyro_msgs import RosMessage
from alpyro_msgs.actionlib_msgs.goalid import GoalID
from alpyro_msgs.nav_msgs.getmapgoal import GetMapGoal
from alpyro_msgs.std_msgs.header import Header


class GetMapActionGoal(RosMessage):
  __msg_typ__ = "nav_msgs/GetMapActionGoal"
  __msg_def__ = "c3RkX21zZ3MvSGVhZGVyIGhlYWRlcgogIHVpbnQzMiBzZXEKICB0aW1lIHN0YW1wCiAgc3RyaW5nIGZyYW1lX2lkCmFjdGlvbmxpYl9tc2dzL0dvYWxJRCBnb2FsX2lkCiAgdGltZSBzdGFtcAogIHN0cmluZyBpZApuYXZfbXNncy9HZXRNYXBHb2FsIGdvYWwKCg=="
  __md5_sum__ = "4b30be6cd12b9e72826df56b481f40e0"

  header: Header
  goal_id: GoalID
  goal: GetMapGoal
