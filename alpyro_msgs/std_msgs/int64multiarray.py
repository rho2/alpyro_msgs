from typing import List
from typing_extensions import Annotated
from alpyro_msgs import RosMessage, int64
from alpyro_msgs.std_msgs.multiarraylayout import MultiArrayLayout


class Int64MultiArray(RosMessage):
  __msg_typ__ = "std_msgs/Int64MultiArray"
  __msg_def__ = "c3RkX21zZ3MvTXVsdGlBcnJheUxheW91dCBsYXlvdXQKICBzdGRfbXNncy9NdWx0aUFycmF5RGltZW5zaW9uW10gZGltCiAgICBzdHJpbmcgbGFiZWwKICAgIHVpbnQzMiBzaXplCiAgICB1aW50MzIgc3RyaWRlCiAgdWludDMyIGRhdGFfb2Zmc2V0CmludDY0W10gZGF0YQoK"
  __md5_sum__ = "54865aa6c65be0448113a2afc6a49270"

  layout: MultiArrayLayout
  data: Annotated[List[int64], 0, 0]
