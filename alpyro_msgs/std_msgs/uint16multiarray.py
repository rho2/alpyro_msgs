from typing import List
from typing_extensions import Annotated
from alpyro_msgs import RosMessage, uint16
from alpyro_msgs.std_msgs.multiarraylayout import MultiArrayLayout


class UInt16MultiArray(RosMessage):
  __msg_typ__ = "std_msgs/UInt16MultiArray"
  __msg_def__ = "c3RkX21zZ3MvTXVsdGlBcnJheUxheW91dCBsYXlvdXQKICBzdGRfbXNncy9NdWx0aUFycmF5RGltZW5zaW9uW10gZGltCiAgICBzdHJpbmcgbGFiZWwKICAgIHVpbnQzMiBzaXplCiAgICB1aW50MzIgc3RyaWRlCiAgdWludDMyIGRhdGFfb2Zmc2V0CnVpbnQxNltdIGRhdGEKCg=="
  __md5_sum__ = "52f264f1c973c4b73790d384c6cb4484"

  layout: MultiArrayLayout
  data: Annotated[List[uint16], 0, 0]
