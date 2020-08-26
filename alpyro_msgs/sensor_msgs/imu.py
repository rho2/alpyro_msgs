from typing import List
from typing_extensions import Annotated
from alpyro_msgs import RosMessage, float64
from alpyro_msgs.geometry_msgs.quaternion import Quaternion
from alpyro_msgs.geometry_msgs.vector3 import Vector3
from alpyro_msgs.std_msgs.header import Header


class Imu(RosMessage):
  __msg_typ__ = "sensor_msgs/Imu"
  __msg_def__ = "c3RkX21zZ3MvSGVhZGVyIGhlYWRlcgogIHVpbnQzMiBzZXEKICB0aW1lIHN0YW1wCiAgc3RyaW5nIGZyYW1lX2lkCmdlb21ldHJ5X21zZ3MvUXVhdGVybmlvbiBvcmllbnRhdGlvbgogIGZsb2F0NjQgeAogIGZsb2F0NjQgeQogIGZsb2F0NjQgegogIGZsb2F0NjQgdwpmbG9hdDY0WzldIG9yaWVudGF0aW9uX2NvdmFyaWFuY2UKZ2VvbWV0cnlfbXNncy9WZWN0b3IzIGFuZ3VsYXJfdmVsb2NpdHkKICBmbG9hdDY0IHgKICBmbG9hdDY0IHkKICBmbG9hdDY0IHoKZmxvYXQ2NFs5XSBhbmd1bGFyX3ZlbG9jaXR5X2NvdmFyaWFuY2UKZ2VvbWV0cnlfbXNncy9WZWN0b3IzIGxpbmVhcl9hY2NlbGVyYXRpb24KICBmbG9hdDY0IHgKICBmbG9hdDY0IHkKICBmbG9hdDY0IHoKZmxvYXQ2NFs5XSBsaW5lYXJfYWNjZWxlcmF0aW9uX2NvdmFyaWFuY2UKCg=="
  __md5_sum__ = "6a62c6daae103f4ff57a132d6f95cec2"

  header: Header
  orientation: Quaternion
  orientation_covariance: Annotated[List[float64], 9, 0]
  angular_velocity: Vector3
  angular_velocity_covariance: Annotated[List[float64], 9, 0]
  linear_acceleration: Vector3
  linear_acceleration_covariance: Annotated[List[float64], 9, 0]
