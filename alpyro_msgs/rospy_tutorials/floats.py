from typing import List
from typing_extensions import Annotated
from alpyro_msgs import RosMessage, float32


class Floats(RosMessage):
  __msg_typ__ = "rospy_tutorials/Floats"
  __msg_def__ = "ZmxvYXQzMltdIGRhdGEKCg=="
  __md5_sum__ = "420cd38b6b071cd49f2970c3e2cee511"

  data: Annotated[List[float32], 0, 0]
