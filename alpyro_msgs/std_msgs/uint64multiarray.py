from typing import List
from typing_extensions import Annotated
from alpyro_msgs import RosMessage, uint64
from alpyro_msgs.std_msgs.multiarraylayout import MultiArrayLayout


class UInt64MultiArray(RosMessage):
  __msg_typ__ = "std_msgs/UInt64MultiArray"
  __msg_def__ = "c3RkX21zZ3MvTXVsdGlBcnJheUxheW91dCBsYXlvdXQKICBzdGRfbXNncy9NdWx0aUFycmF5RGltZW5zaW9uW10gZGltCiAgICBzdHJpbmcgbGFiZWwKICAgIHVpbnQzMiBzaXplCiAgICB1aW50MzIgc3RyaWRlCiAgdWludDMyIGRhdGFfb2Zmc2V0CnVpbnQ2NFtdIGRhdGEKCg=="
  __md5_sum__ = "6088f127afb1d6c72927aa1247e945af"

  layout: MultiArrayLayout
  data: Annotated[List[uint64], 0, 0]
