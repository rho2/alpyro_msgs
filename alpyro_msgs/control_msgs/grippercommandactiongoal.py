from alpyro_msgs import RosMessage
from alpyro_msgs.actionlib_msgs.goalid import GoalID
from alpyro_msgs.control_msgs.grippercommandgoal import GripperCommandGoal
from alpyro_msgs.std_msgs.header import Header


class GripperCommandActionGoal(RosMessage):
  __msg_typ__ = "control_msgs/GripperCommandActionGoal"
  __msg_def__ = "c3RkX21zZ3MvSGVhZGVyIGhlYWRlcgogIHVpbnQzMiBzZXEKICB0aW1lIHN0YW1wCiAgc3RyaW5nIGZyYW1lX2lkCmFjdGlvbmxpYl9tc2dzL0dvYWxJRCBnb2FsX2lkCiAgdGltZSBzdGFtcAogIHN0cmluZyBpZApjb250cm9sX21zZ3MvR3JpcHBlckNvbW1hbmRHb2FsIGdvYWwKICBjb250cm9sX21zZ3MvR3JpcHBlckNvbW1hbmQgY29tbWFuZAogICAgZmxvYXQ2NCBwb3NpdGlvbgogICAgZmxvYXQ2NCBtYXhfZWZmb3J0Cgo="
  __md5_sum__ = "aa581f648a35ed681db2ec0bf7a82bea"

  header: Header
  goal_id: GoalID
  goal: GripperCommandGoal
