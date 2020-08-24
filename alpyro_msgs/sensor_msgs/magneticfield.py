from typing import List
from typing_extensions import Annotated
from alpyro_msgs import RosMessage, float64
from alpyro_msgs.geometry_msgs.vector3 import Vector3
from alpyro_msgs.std_msgs.header import Header


class MagneticField(RosMessage):
  __msg_typ__ = "sensor_msgs/MagneticField"
  __msg_def__ = "c3RkX21zZ3MvSGVhZGVyIGhlYWRlcgogIHVpbnQzMiBzZXEKICB0aW1lIHN0YW1wCiAgc3RyaW5nIGZyYW1lX2lkCmdlb21ldHJ5X21zZ3MvVmVjdG9yMyBtYWduZXRpY19maWVsZAogIGZsb2F0NjQgeAogIGZsb2F0NjQgeQogIGZsb2F0NjQgegpmbG9hdDY0WzldIG1hZ25ldGljX2ZpZWxkX2NvdmFyaWFuY2UKCg=="
  __md5_sum__ = "2f3b0b43eed0c9501de0fa3ff89a45aa"

  header: Header
  magnetic_field: Vector3
  magnetic_field_covariance: Annotated[List[float64], 9, 0]
