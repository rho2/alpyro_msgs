from typing import List
from typing_extensions import Annotated
from alpyro_msgs import RosMessage, float32
from alpyro_msgs.std_msgs.multiarraylayout import MultiArrayLayout


class Float32MultiArray(RosMessage):
  __msg_typ__ = "std_msgs/Float32MultiArray"
  __msg_def__ = "c3RkX21zZ3MvTXVsdGlBcnJheUxheW91dCBsYXlvdXQKICBzdGRfbXNncy9NdWx0aUFycmF5RGltZW5zaW9uW10gZGltCiAgICBzdHJpbmcgbGFiZWwKICAgIHVpbnQzMiBzaXplCiAgICB1aW50MzIgc3RyaWRlCiAgdWludDMyIGRhdGFfb2Zmc2V0CmZsb2F0MzJbXSBkYXRhCgo="
  __md5_sum__ = "6a40e0ffa6a17a503ac3f8616991b1f6"

  layout: MultiArrayLayout
  data: Annotated[List[float32], 0, 0]
