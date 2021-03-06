from typing import List
from typing_extensions import Annotated
from typing import Final
from alpyro_msgs import RosMessage
from alpyro_msgs.actionlib_msgs.goalstatus import GoalStatus
from alpyro_msgs.control_msgs.followjointtrajectoryfeedback import FollowJointTrajectoryFeedback
from alpyro_msgs.std_msgs.header import Header


class FollowJointTrajectoryActionFeedback(RosMessage):
  __msg_typ__ = "control_msgs/FollowJointTrajectoryActionFeedback"
  __msg_def__ = "c3RkX21zZ3MvSGVhZGVyIGhlYWRlcgogIHVpbnQzMiBzZXEKICB0aW1lIHN0YW1wCiAgc3RyaW5nIGZyYW1lX2lkCmFjdGlvbmxpYl9tc2dzL0dvYWxTdGF0dXMgc3RhdHVzCiAgdWludDggUEVORElORz0wCiAgdWludDggQUNUSVZFPTEKICB1aW50OCBQUkVFTVBURUQ9MgogIHVpbnQ4IFNVQ0NFRURFRD0zCiAgdWludDggQUJPUlRFRD00CiAgdWludDggUkVKRUNURUQ9NQogIHVpbnQ4IFBSRUVNUFRJTkc9NgogIHVpbnQ4IFJFQ0FMTElORz03CiAgdWludDggUkVDQUxMRUQ9OAogIHVpbnQ4IExPU1Q9OQogIGFjdGlvbmxpYl9tc2dzL0dvYWxJRCBnb2FsX2lkCiAgICB0aW1lIHN0YW1wCiAgICBzdHJpbmcgaWQKICB1aW50OCBzdGF0dXMKICBzdHJpbmcgdGV4dApjb250cm9sX21zZ3MvRm9sbG93Sm9pbnRUcmFqZWN0b3J5RmVlZGJhY2sgZmVlZGJhY2sKICBzdGRfbXNncy9IZWFkZXIgaGVhZGVyCiAgICB1aW50MzIgc2VxCiAgICB0aW1lIHN0YW1wCiAgICBzdHJpbmcgZnJhbWVfaWQKICBzdHJpbmdbXSBqb2ludF9uYW1lcwogIHRyYWplY3RvcnlfbXNncy9Kb2ludFRyYWplY3RvcnlQb2ludCBkZXNpcmVkCiAgICBmbG9hdDY0W10gcG9zaXRpb25zCiAgICBmbG9hdDY0W10gdmVsb2NpdGllcwogICAgZmxvYXQ2NFtdIGFjY2VsZXJhdGlvbnMKICAgIGZsb2F0NjRbXSBlZmZvcnQKICAgIGR1cmF0aW9uIHRpbWVfZnJvbV9zdGFydAogIHRyYWplY3RvcnlfbXNncy9Kb2ludFRyYWplY3RvcnlQb2ludCBhY3R1YWwKICAgIGZsb2F0NjRbXSBwb3NpdGlvbnMKICAgIGZsb2F0NjRbXSB2ZWxvY2l0aWVzCiAgICBmbG9hdDY0W10gYWNjZWxlcmF0aW9ucwogICAgZmxvYXQ2NFtdIGVmZm9ydAogICAgZHVyYXRpb24gdGltZV9mcm9tX3N0YXJ0CiAgdHJhamVjdG9yeV9tc2dzL0pvaW50VHJhamVjdG9yeVBvaW50IGVycm9yCiAgICBmbG9hdDY0W10gcG9zaXRpb25zCiAgICBmbG9hdDY0W10gdmVsb2NpdGllcwogICAgZmxvYXQ2NFtdIGFjY2VsZXJhdGlvbnMKICAgIGZsb2F0NjRbXSBlZmZvcnQKICAgIGR1cmF0aW9uIHRpbWVfZnJvbV9zdGFydAoK"
  __md5_sum__ = "d8920dc4eae9fc107e00999cce4be641"

  header: Header
  status: GoalStatus
  feedback: FollowJointTrajectoryFeedback
