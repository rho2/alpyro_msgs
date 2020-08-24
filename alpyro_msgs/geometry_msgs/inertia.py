from alpyro_msgs import RosMessage, float64
from alpyro_msgs.geometry_msgs.vector3 import Vector3


class Inertia(RosMessage):
  __msg_typ__ = "geometry_msgs/Inertia"
  __msg_def__ = "ZmxvYXQ2NCBtCmdlb21ldHJ5X21zZ3MvVmVjdG9yMyBjb20KICBmbG9hdDY0IHgKICBmbG9hdDY0IHkKICBmbG9hdDY0IHoKZmxvYXQ2NCBpeHgKZmxvYXQ2NCBpeHkKZmxvYXQ2NCBpeHoKZmxvYXQ2NCBpeXkKZmxvYXQ2NCBpeXoKZmxvYXQ2NCBpenoKCg=="
  __md5_sum__ = "1d26e4bb6c83ff141c5cf0d883c2b0fe"

  m: float64
  com: Vector3
  ixx: float64
  ixy: float64
  ixz: float64
  iyy: float64
  iyz: float64
  izz: float64
