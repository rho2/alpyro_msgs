from typing import List
from typing_extensions import Annotated
from alpyro_msgs import RosMessage, int32
from alpyro_msgs.std_msgs.multiarraylayout import MultiArrayLayout


class Int32MultiArray(RosMessage):
  __msg_typ__ = "std_msgs/Int32MultiArray"
  __msg_def__ = "c3RkX21zZ3MvTXVsdGlBcnJheUxheW91dCBsYXlvdXQKICBzdGRfbXNncy9NdWx0aUFycmF5RGltZW5zaW9uW10gZGltCiAgICBzdHJpbmcgbGFiZWwKICAgIHVpbnQzMiBzaXplCiAgICB1aW50MzIgc3RyaWRlCiAgdWludDMyIGRhdGFfb2Zmc2V0CmludDMyW10gZGF0YQoK"
  __md5_sum__ = "1d99f79f8b325b44fee908053e9c945b"

  layout: MultiArrayLayout
  data: Annotated[List[int32], 0, 0]
