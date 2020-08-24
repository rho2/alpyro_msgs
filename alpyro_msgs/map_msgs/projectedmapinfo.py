from alpyro_msgs import RosMessage, float64, string


class ProjectedMapInfo(RosMessage):
  __msg_typ__ = "map_msgs/ProjectedMapInfo"
  __msg_def__ = "c3RyaW5nIGZyYW1lX2lkCmZsb2F0NjQgeApmbG9hdDY0IHkKZmxvYXQ2NCB3aWR0aApmbG9hdDY0IGhlaWdodApmbG9hdDY0IG1pbl96CmZsb2F0NjQgbWF4X3oKCg=="
  __md5_sum__ = "2dc10595ae94de23f22f8a6d2a0eef7a"

  frame_id: string
  x: float64
  y: float64
  width: float64
  height: float64
  min_z: float64
  max_z: float64
