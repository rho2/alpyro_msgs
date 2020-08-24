from typing import List
from typing_extensions import Annotated
from alpyro_msgs import RosMessage, float64
from alpyro_msgs.geometry_msgs.twist import Twist


class TwistWithCovariance(RosMessage):
  __msg_typ__ = "geometry_msgs/TwistWithCovariance"
  __msg_def__ = "Z2VvbWV0cnlfbXNncy9Ud2lzdCB0d2lzdAogIGdlb21ldHJ5X21zZ3MvVmVjdG9yMyBsaW5lYXIKICAgIGZsb2F0NjQgeAogICAgZmxvYXQ2NCB5CiAgICBmbG9hdDY0IHoKICBnZW9tZXRyeV9tc2dzL1ZlY3RvcjMgYW5ndWxhcgogICAgZmxvYXQ2NCB4CiAgICBmbG9hdDY0IHkKICAgIGZsb2F0NjQgegpmbG9hdDY0WzM2XSBjb3ZhcmlhbmNlCgo="
  __md5_sum__ = "1fe8a28e6890a4cc3ae4c3ca5c7d82e6"

  twist: Twist
  covariance: Annotated[List[float64], 36, 0]
