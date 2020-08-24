from typing import List
from typing_extensions import Annotated
from alpyro_msgs import RosMessage, string
from alpyro_msgs.std_msgs.header import Header
from alpyro_msgs.trajectory_msgs.jointtrajectorypoint import JointTrajectoryPoint


class JointTrajectory(RosMessage):
  __msg_typ__ = "trajectory_msgs/JointTrajectory"
  __msg_def__ = "c3RkX21zZ3MvSGVhZGVyIGhlYWRlcgogIHVpbnQzMiBzZXEKICB0aW1lIHN0YW1wCiAgc3RyaW5nIGZyYW1lX2lkCnN0cmluZ1tdIGpvaW50X25hbWVzCnRyYWplY3RvcnlfbXNncy9Kb2ludFRyYWplY3RvcnlQb2ludFtdIHBvaW50cwogIGZsb2F0NjRbXSBwb3NpdGlvbnMKICBmbG9hdDY0W10gdmVsb2NpdGllcwogIGZsb2F0NjRbXSBhY2NlbGVyYXRpb25zCiAgZmxvYXQ2NFtdIGVmZm9ydAogIGR1cmF0aW9uIHRpbWVfZnJvbV9zdGFydAoK"
  __md5_sum__ = "65b4f94a94d1ed67169da35a02f33d3f"

  header: Header
  joint_names: Annotated[List[string], 0, 0]
  points: Annotated[List[JointTrajectoryPoint], 0, 0]
