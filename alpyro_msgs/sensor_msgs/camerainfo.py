from typing import List
from typing_extensions import Annotated
from alpyro_msgs import RosMessage, float64, string, uint32
from alpyro_msgs.sensor_msgs.regionofinterest import RegionOfInterest
from alpyro_msgs.std_msgs.header import Header


class CameraInfo(RosMessage):
  __msg_typ__ = "sensor_msgs/CameraInfo"
  __msg_def__ = "c3RkX21zZ3MvSGVhZGVyIGhlYWRlcgogIHVpbnQzMiBzZXEKICB0aW1lIHN0YW1wCiAgc3RyaW5nIGZyYW1lX2lkCnVpbnQzMiBoZWlnaHQKdWludDMyIHdpZHRoCnN0cmluZyBkaXN0b3J0aW9uX21vZGVsCmZsb2F0NjRbXSBECmZsb2F0NjRbOV0gSwpmbG9hdDY0WzldIFIKZmxvYXQ2NFsxMl0gUAp1aW50MzIgYmlubmluZ194CnVpbnQzMiBiaW5uaW5nX3kKc2Vuc29yX21zZ3MvUmVnaW9uT2ZJbnRlcmVzdCByb2kKICB1aW50MzIgeF9vZmZzZXQKICB1aW50MzIgeV9vZmZzZXQKICB1aW50MzIgaGVpZ2h0CiAgdWludDMyIHdpZHRoCiAgYm9vbCBkb19yZWN0aWZ5Cgo="
  __md5_sum__ = "c9a58c1b0b154e0e6da7578cb991d214"

  header: Header
  height: uint32
  width: uint32
  distortion_model: string
  D: Annotated[List[float64], 0, 0]
  K: Annotated[List[float64], 9, 0]
  R: Annotated[List[float64], 9, 0]
  P: Annotated[List[float64], 12, 0]
  binning_x: uint32
  binning_y: uint32
  roi: RegionOfInterest
