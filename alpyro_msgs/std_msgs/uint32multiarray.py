from typing import List
from typing_extensions import Annotated
from alpyro_msgs import RosMessage, uint32
from alpyro_msgs.std_msgs.multiarraylayout import MultiArrayLayout


class UInt32MultiArray(RosMessage):
  __msg_typ__ = "std_msgs/UInt32MultiArray"
  __msg_def__ = "c3RkX21zZ3MvTXVsdGlBcnJheUxheW91dCBsYXlvdXQKICBzdGRfbXNncy9NdWx0aUFycmF5RGltZW5zaW9uW10gZGltCiAgICBzdHJpbmcgbGFiZWwKICAgIHVpbnQzMiBzaXplCiAgICB1aW50MzIgc3RyaWRlCiAgdWludDMyIGRhdGFfb2Zmc2V0CnVpbnQzMltdIGRhdGEKCg=="
  __md5_sum__ = "4d6a180abc9be191b96a7eda6c8a233d"

  layout: MultiArrayLayout
  data: Annotated[List[uint32], 0, 0]
