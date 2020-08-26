from typing import List
from typing_extensions import Annotated
from alpyro_msgs import RosMessage, uint8
from alpyro_msgs.std_msgs.multiarraylayout import MultiArrayLayout


class UInt8MultiArray(RosMessage):
  __msg_typ__ = "std_msgs/UInt8MultiArray"
  __msg_def__ = "c3RkX21zZ3MvTXVsdGlBcnJheUxheW91dCBsYXlvdXQKICBzdGRfbXNncy9NdWx0aUFycmF5RGltZW5zaW9uW10gZGltCiAgICBzdHJpbmcgbGFiZWwKICAgIHVpbnQzMiBzaXplCiAgICB1aW50MzIgc3RyaWRlCiAgdWludDMyIGRhdGFfb2Zmc2V0CnVpbnQ4W10gZGF0YQoK"
  __md5_sum__ = "82373f1612381bb6ee473b5cd6f5d89c"

  layout: MultiArrayLayout
  data: Annotated[bytes, 0, 0]
