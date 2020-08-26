from alpyro_msgs import RosMessage
from alpyro_msgs.actionlib_msgs.goalid import GoalID
from alpyro_msgs.std_msgs.header import Header
from alpyro_msgs.turtle_actionlib.shapegoal import ShapeGoal


class ShapeActionGoal(RosMessage):
  __msg_typ__ = "turtle_actionlib/ShapeActionGoal"
  __msg_def__ = "c3RkX21zZ3MvSGVhZGVyIGhlYWRlcgogIHVpbnQzMiBzZXEKICB0aW1lIHN0YW1wCiAgc3RyaW5nIGZyYW1lX2lkCmFjdGlvbmxpYl9tc2dzL0dvYWxJRCBnb2FsX2lkCiAgdGltZSBzdGFtcAogIHN0cmluZyBpZAp0dXJ0bGVfYWN0aW9ubGliL1NoYXBlR29hbCBnb2FsCiAgaW50MzIgZWRnZXMKICBmbG9hdDMyIHJhZGl1cwoK"
  __md5_sum__ = "dbfccd187f2ec9c593916447ffd6cc77"

  header: Header
  goal_id: GoalID
  goal: ShapeGoal
