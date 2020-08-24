from typing import List
from typing_extensions import Annotated
from alpyro_msgs import RosMessage, float64
from alpyro_msgs.geometry_msgs.accel import Accel


class AccelWithCovariance(RosMessage):
  __msg_typ__ = "geometry_msgs/AccelWithCovariance"
  __msg_def__ = "Z2VvbWV0cnlfbXNncy9BY2NlbCBhY2NlbAogIGdlb21ldHJ5X21zZ3MvVmVjdG9yMyBsaW5lYXIKICAgIGZsb2F0NjQgeAogICAgZmxvYXQ2NCB5CiAgICBmbG9hdDY0IHoKICBnZW9tZXRyeV9tc2dzL1ZlY3RvcjMgYW5ndWxhcgogICAgZmxvYXQ2NCB4CiAgICBmbG9hdDY0IHkKICAgIGZsb2F0NjQgegpmbG9hdDY0WzM2XSBjb3ZhcmlhbmNlCgo="
  __md5_sum__ = "ad5a718d699c6be72a02b8d6a139f334"

  accel: Accel
  covariance: Annotated[List[float64], 36, 0]
