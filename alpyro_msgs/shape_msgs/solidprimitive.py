from typing import List
from typing_extensions import Annotated
from typing import Final
from alpyro_msgs import RosMessage, float64, uint8


class SolidPrimitive(RosMessage):
  __msg_typ__ = "shape_msgs/SolidPrimitive"
  __msg_def__ = "dWludDggQk9YPTEKdWludDggU1BIRVJFPTIKdWludDggQ1lMSU5ERVI9Mwp1aW50OCBDT05FPTQKdWludDggQk9YX1g9MAp1aW50OCBCT1hfWT0xCnVpbnQ4IEJPWF9aPTIKdWludDggU1BIRVJFX1JBRElVUz0wCnVpbnQ4IENZTElOREVSX0hFSUdIVD0wCnVpbnQ4IENZTElOREVSX1JBRElVUz0xCnVpbnQ4IENPTkVfSEVJR0hUPTAKdWludDggQ09ORV9SQURJVVM9MQp1aW50OCB0eXBlCmZsb2F0NjRbXSBkaW1lbnNpb25zCgo="
  __md5_sum__ = "d8f8cbc74c5ff283fca29569ccefb45d"

  BOX: Final[uint8] = 1
  SPHERE: Final[uint8] = 2
  CYLINDER: Final[uint8] = 3
  CONE: Final[uint8] = 4
  BOX_X: Final[uint8] = 0
  BOX_Y: Final[uint8] = 1
  BOX_Z: Final[uint8] = 2
  SPHERE_RADIUS: Final[uint8] = 0
  CYLINDER_HEIGHT: Final[uint8] = 0
  CYLINDER_RADIUS: Final[uint8] = 1
  CONE_HEIGHT: Final[uint8] = 0
  CONE_RADIUS: Final[uint8] = 1
  type: uint8
  dimensions: Annotated[List[float64], 0, 0]
