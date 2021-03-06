from typing import List
from typing_extensions import Annotated
from alpyro_msgs import RosMessage
from alpyro_msgs.geometry_msgs.twistwithcovariance import TwistWithCovariance
from alpyro_msgs.std_msgs.header import Header


class TwistWithCovarianceStamped(RosMessage):
  __msg_typ__ = "geometry_msgs/TwistWithCovarianceStamped"
  __msg_def__ = "c3RkX21zZ3MvSGVhZGVyIGhlYWRlcgogIHVpbnQzMiBzZXEKICB0aW1lIHN0YW1wCiAgc3RyaW5nIGZyYW1lX2lkCmdlb21ldHJ5X21zZ3MvVHdpc3RXaXRoQ292YXJpYW5jZSB0d2lzdAogIGdlb21ldHJ5X21zZ3MvVHdpc3QgdHdpc3QKICAgIGdlb21ldHJ5X21zZ3MvVmVjdG9yMyBsaW5lYXIKICAgICAgZmxvYXQ2NCB4CiAgICAgIGZsb2F0NjQgeQogICAgICBmbG9hdDY0IHoKICAgIGdlb21ldHJ5X21zZ3MvVmVjdG9yMyBhbmd1bGFyCiAgICAgIGZsb2F0NjQgeAogICAgICBmbG9hdDY0IHkKICAgICAgZmxvYXQ2NCB6CiAgZmxvYXQ2NFszNl0gY292YXJpYW5jZQoK"
  __md5_sum__ = "8927a1a12fb2607ceea095b2dc440a96"

  header: Header
  twist: TwistWithCovariance
