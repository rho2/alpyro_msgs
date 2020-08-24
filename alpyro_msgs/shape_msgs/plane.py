from typing import List
from typing_extensions import Annotated
from alpyro_msgs import RosMessage, float64


class Plane(RosMessage):
  __msg_typ__ = "shape_msgs/Plane"
  __msg_def__ = "ZmxvYXQ2NFs0XSBjb2VmCgo="
  __md5_sum__ = "2c1b92ed8f31492f8e73f6a4a44ca796"

  coef: Annotated[List[float64], 4, 0]
