from alpyro_msgs import RosMessage
from alpyro_msgs.geometry_msgs.quaternion import Quaternion
from alpyro_msgs.std_msgs.header import Header


class QuaternionStamped(RosMessage):
  __msg_typ__ = "geometry_msgs/QuaternionStamped"
  __msg_def__ = "c3RkX21zZ3MvSGVhZGVyIGhlYWRlcgogIHVpbnQzMiBzZXEKICB0aW1lIHN0YW1wCiAgc3RyaW5nIGZyYW1lX2lkCmdlb21ldHJ5X21zZ3MvUXVhdGVybmlvbiBxdWF0ZXJuaW9uCiAgZmxvYXQ2NCB4CiAgZmxvYXQ2NCB5CiAgZmxvYXQ2NCB6CiAgZmxvYXQ2NCB3Cgo="
  __md5_sum__ = "e57f1e547e0e1fd13504588ffc8334e2"

  header: Header
  quaternion: Quaternion
