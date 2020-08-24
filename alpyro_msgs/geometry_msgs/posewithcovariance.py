from typing import List
from typing_extensions import Annotated
from alpyro_msgs import RosMessage, float64
from alpyro_msgs.geometry_msgs.pose import Pose


class PoseWithCovariance(RosMessage):
  __msg_typ__ = "geometry_msgs/PoseWithCovariance"
  __msg_def__ = "Z2VvbWV0cnlfbXNncy9Qb3NlIHBvc2UKICBnZW9tZXRyeV9tc2dzL1BvaW50IHBvc2l0aW9uCiAgICBmbG9hdDY0IHgKICAgIGZsb2F0NjQgeQogICAgZmxvYXQ2NCB6CiAgZ2VvbWV0cnlfbXNncy9RdWF0ZXJuaW9uIG9yaWVudGF0aW9uCiAgICBmbG9hdDY0IHgKICAgIGZsb2F0NjQgeQogICAgZmxvYXQ2NCB6CiAgICBmbG9hdDY0IHcKZmxvYXQ2NFszNl0gY292YXJpYW5jZQoK"
  __md5_sum__ = "c23e848cf1b7533a8d7c259073a97e6f"

  pose: Pose
  covariance: Annotated[List[float64], 36, 0]
