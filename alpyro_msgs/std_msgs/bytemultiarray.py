from typing import List
from typing_extensions import Annotated
from alpyro_msgs import RosMessage, int8
from alpyro_msgs.std_msgs.multiarraylayout import MultiArrayLayout


class ByteMultiArray(RosMessage):
  __msg_typ__ = "std_msgs/ByteMultiArray"
  __msg_def__ = "c3RkX21zZ3MvTXVsdGlBcnJheUxheW91dCBsYXlvdXQKICBzdGRfbXNncy9NdWx0aUFycmF5RGltZW5zaW9uW10gZGltCiAgICBzdHJpbmcgbGFiZWwKICAgIHVpbnQzMiBzaXplCiAgICB1aW50MzIgc3RyaWRlCiAgdWludDMyIGRhdGFfb2Zmc2V0CmJ5dGVbXSBkYXRhCgo="
  __md5_sum__ = "70ea476cbcfd65ac2f68f3cda1e891fe"

  layout: MultiArrayLayout
  data: Annotated[List[int8], 0, 0]
