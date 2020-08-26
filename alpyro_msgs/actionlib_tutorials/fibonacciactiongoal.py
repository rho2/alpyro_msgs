from alpyro_msgs import RosMessage
from alpyro_msgs.actionlib_msgs.goalid import GoalID
from alpyro_msgs.actionlib_tutorials.fibonaccigoal import FibonacciGoal
from alpyro_msgs.std_msgs.header import Header


class FibonacciActionGoal(RosMessage):
  __msg_typ__ = "actionlib_tutorials/FibonacciActionGoal"
  __msg_def__ = "c3RkX21zZ3MvSGVhZGVyIGhlYWRlcgogIHVpbnQzMiBzZXEKICB0aW1lIHN0YW1wCiAgc3RyaW5nIGZyYW1lX2lkCmFjdGlvbmxpYl9tc2dzL0dvYWxJRCBnb2FsX2lkCiAgdGltZSBzdGFtcAogIHN0cmluZyBpZAphY3Rpb25saWJfdHV0b3JpYWxzL0ZpYm9uYWNjaUdvYWwgZ29hbAogIGludDMyIG9yZGVyCgo="
  __md5_sum__ = "006871c7fa1d0e3d5fe2226bf17b2a94"

  header: Header
  goal_id: GoalID
  goal: FibonacciGoal
