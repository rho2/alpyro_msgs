from typing import List
from typing_extensions import Annotated
from alpyro_msgs import RosMessage, int16
from alpyro_msgs.std_msgs.multiarraylayout import MultiArrayLayout


class Int16MultiArray(RosMessage):
  __msg_typ__ = "std_msgs/Int16MultiArray"
  __msg_def__ = "c3RkX21zZ3MvTXVsdGlBcnJheUxheW91dCBsYXlvdXQKICBzdGRfbXNncy9NdWx0aUFycmF5RGltZW5zaW9uW10gZGltCiAgICBzdHJpbmcgbGFiZWwKICAgIHVpbnQzMiBzaXplCiAgICB1aW50MzIgc3RyaWRlCiAgdWludDMyIGRhdGFfb2Zmc2V0CmludDE2W10gZGF0YQoK"
  __md5_sum__ = "d9338d7f523fcb692fae9d0a0e9f067c"

  layout: MultiArrayLayout
  data: Annotated[List[int16], 0, 0]
