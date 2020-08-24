from typing import List
from typing_extensions import Annotated
from alpyro_msgs import RosMessage, int8
from alpyro_msgs.std_msgs.multiarraylayout import MultiArrayLayout


class Int8MultiArray(RosMessage):
  __msg_typ__ = "std_msgs/Int8MultiArray"
  __msg_def__ = "c3RkX21zZ3MvTXVsdGlBcnJheUxheW91dCBsYXlvdXQKICBzdGRfbXNncy9NdWx0aUFycmF5RGltZW5zaW9uW10gZGltCiAgICBzdHJpbmcgbGFiZWwKICAgIHVpbnQzMiBzaXplCiAgICB1aW50MzIgc3RyaWRlCiAgdWludDMyIGRhdGFfb2Zmc2V0CmludDhbXSBkYXRhCgo="
  __md5_sum__ = "d7c1af35a1b4781bbe79e03dd94b7c13"

  layout: MultiArrayLayout
  data: Annotated[List[int8], 0, 0]
