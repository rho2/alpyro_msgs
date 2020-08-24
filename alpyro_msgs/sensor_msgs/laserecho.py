from typing import List
from typing_extensions import Annotated
from alpyro_msgs import RosMessage, float32


class LaserEcho(RosMessage):
  __msg_typ__ = "sensor_msgs/LaserEcho"
  __msg_def__ = "ZmxvYXQzMltdIGVjaG9lcwoK"
  __md5_sum__ = "8bc5ae449b200fba4d552b4225586696"

  echoes: Annotated[List[float32], 0, 0]
