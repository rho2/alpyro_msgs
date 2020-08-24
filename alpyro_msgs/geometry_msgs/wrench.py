from alpyro_msgs import RosMessage
from alpyro_msgs.geometry_msgs.vector3 import Vector3


class Wrench(RosMessage):
  __msg_typ__ = "geometry_msgs/Wrench"
  __msg_def__ = "Z2VvbWV0cnlfbXNncy9WZWN0b3IzIGZvcmNlCiAgZmxvYXQ2NCB4CiAgZmxvYXQ2NCB5CiAgZmxvYXQ2NCB6Cmdlb21ldHJ5X21zZ3MvVmVjdG9yMyB0b3JxdWUKICBmbG9hdDY0IHgKICBmbG9hdDY0IHkKICBmbG9hdDY0IHoKCg=="
  __md5_sum__ = "4f539cf138b23283b520fd271b567936"

  force: Vector3
  torque: Vector3
