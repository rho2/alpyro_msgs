from typing import List
from typing_extensions import Annotated
from alpyro_msgs import RosMessage
from alpyro_msgs.dynamic_reconfigure.boolparameter import BoolParameter
from alpyro_msgs.dynamic_reconfigure.doubleparameter import DoubleParameter
from alpyro_msgs.dynamic_reconfigure.groupstate import GroupState
from alpyro_msgs.dynamic_reconfigure.intparameter import IntParameter
from alpyro_msgs.dynamic_reconfigure.strparameter import StrParameter


class Config(RosMessage):
  __msg_typ__ = "dynamic_reconfigure/Config"
  __msg_def__ = "ZHluYW1pY19yZWNvbmZpZ3VyZS9Cb29sUGFyYW1ldGVyW10gYm9vbHMKICBzdHJpbmcgbmFtZQogIGJvb2wgdmFsdWUKZHluYW1pY19yZWNvbmZpZ3VyZS9JbnRQYXJhbWV0ZXJbXSBpbnRzCiAgc3RyaW5nIG5hbWUKICBpbnQzMiB2YWx1ZQpkeW5hbWljX3JlY29uZmlndXJlL1N0clBhcmFtZXRlcltdIHN0cnMKICBzdHJpbmcgbmFtZQogIHN0cmluZyB2YWx1ZQpkeW5hbWljX3JlY29uZmlndXJlL0RvdWJsZVBhcmFtZXRlcltdIGRvdWJsZXMKICBzdHJpbmcgbmFtZQogIGZsb2F0NjQgdmFsdWUKZHluYW1pY19yZWNvbmZpZ3VyZS9Hcm91cFN0YXRlW10gZ3JvdXBzCiAgc3RyaW5nIG5hbWUKICBib29sIHN0YXRlCiAgaW50MzIgaWQKICBpbnQzMiBwYXJlbnQKCg=="
  __md5_sum__ = "958f16a05573709014982821e6822580"

  bools: Annotated[List[BoolParameter], 0, 0]
  ints: Annotated[List[IntParameter], 0, 0]
  strs: Annotated[List[StrParameter], 0, 0]
  doubles: Annotated[List[DoubleParameter], 0, 0]
  groups: Annotated[List[GroupState], 0, 0]
