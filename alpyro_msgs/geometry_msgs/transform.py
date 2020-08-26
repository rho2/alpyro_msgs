from alpyro_msgs import RosMessage
from alpyro_msgs.geometry_msgs.quaternion import Quaternion
from alpyro_msgs.geometry_msgs.vector3 import Vector3


class Transform(RosMessage):
  __msg_typ__ = "geometry_msgs/Transform"
  __msg_def__ = "Z2VvbWV0cnlfbXNncy9WZWN0b3IzIHRyYW5zbGF0aW9uCiAgZmxvYXQ2NCB4CiAgZmxvYXQ2NCB5CiAgZmxvYXQ2NCB6Cmdlb21ldHJ5X21zZ3MvUXVhdGVybmlvbiByb3RhdGlvbgogIGZsb2F0NjQgeAogIGZsb2F0NjQgeQogIGZsb2F0NjQgegogIGZsb2F0NjQgdwoK"
  __md5_sum__ = "ac9eff44abf714214112b05d54a3cf9b"

  translation: Vector3
  rotation: Quaternion
