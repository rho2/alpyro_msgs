from typing import List
from typing_extensions import Annotated
from alpyro_msgs import RosMessage, float64
from alpyro_msgs.std_msgs.multiarraylayout import MultiArrayLayout


class Float64MultiArray(RosMessage):
  __msg_typ__ = "std_msgs/Float64MultiArray"
  __msg_def__ = "c3RkX21zZ3MvTXVsdGlBcnJheUxheW91dCBsYXlvdXQKICBzdGRfbXNncy9NdWx0aUFycmF5RGltZW5zaW9uW10gZGltCiAgICBzdHJpbmcgbGFiZWwKICAgIHVpbnQzMiBzaXplCiAgICB1aW50MzIgc3RyaWRlCiAgdWludDMyIGRhdGFfb2Zmc2V0CmZsb2F0NjRbXSBkYXRhCgo="
  __md5_sum__ = "4b7d974086d4060e7db4613a7e6c3ba4"

  layout: MultiArrayLayout
  data: Annotated[List[float64], 0, 0]
