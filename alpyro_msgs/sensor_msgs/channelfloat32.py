from typing import List
from typing_extensions import Annotated
from alpyro_msgs import RosMessage, float32, string


class ChannelFloat32(RosMessage):
  __msg_typ__ = "sensor_msgs/ChannelFloat32"
  __msg_def__ = "c3RyaW5nIG5hbWUKZmxvYXQzMltdIHZhbHVlcwoK"
  __md5_sum__ = "3d40139cdd33dfedcb71ffeeeb42ae7f"

  name: string
  values: Annotated[List[float32], 0, 0]
