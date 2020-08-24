from typing import List
from typing_extensions import Annotated
from alpyro_msgs import RosMessage, uint32
from alpyro_msgs.std_msgs.multiarraydimension import MultiArrayDimension


class MultiArrayLayout(RosMessage):
  __msg_typ__ = "std_msgs/MultiArrayLayout"
  __msg_def__ = "c3RkX21zZ3MvTXVsdGlBcnJheURpbWVuc2lvbltdIGRpbQogIHN0cmluZyBsYWJlbAogIHVpbnQzMiBzaXplCiAgdWludDMyIHN0cmlkZQp1aW50MzIgZGF0YV9vZmZzZXQKCg=="
  __md5_sum__ = "0fed2a11c13e11c5571b4e2a995a91a3"

  dim: Annotated[List[MultiArrayDimension], 0, 0]
  data_offset: uint32
