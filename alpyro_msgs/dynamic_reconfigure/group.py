from typing import List
from typing_extensions import Annotated
from alpyro_msgs import RosMessage, int32, string
from alpyro_msgs.dynamic_reconfigure.paramdescription import ParamDescription


class Group(RosMessage):
  __msg_typ__ = "dynamic_reconfigure/Group"
  __msg_def__ = "c3RyaW5nIG5hbWUKc3RyaW5nIHR5cGUKZHluYW1pY19yZWNvbmZpZ3VyZS9QYXJhbURlc2NyaXB0aW9uW10gcGFyYW1ldGVycwogIHN0cmluZyBuYW1lCiAgc3RyaW5nIHR5cGUKICB1aW50MzIgbGV2ZWwKICBzdHJpbmcgZGVzY3JpcHRpb24KICBzdHJpbmcgZWRpdF9tZXRob2QKaW50MzIgcGFyZW50CmludDMyIGlkCgo="
  __md5_sum__ = "9e8cd9e9423c94823db3614dd8b1cf7a"

  name: string
  type: string
  parameters: Annotated[List[ParamDescription], 0, 0]
  parent: int32
  id: int32
