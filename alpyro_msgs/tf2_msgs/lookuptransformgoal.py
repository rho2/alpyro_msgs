from alpyro_msgs import RosMessage, boolean, duration, string, time


class LookupTransformGoal(RosMessage):
  __msg_typ__ = "tf2_msgs/LookupTransformGoal"
  __msg_def__ = "c3RyaW5nIHRhcmdldF9mcmFtZQpzdHJpbmcgc291cmNlX2ZyYW1lCnRpbWUgc291cmNlX3RpbWUKZHVyYXRpb24gdGltZW91dAp0aW1lIHRhcmdldF90aW1lCnN0cmluZyBmaXhlZF9mcmFtZQpib29sIGFkdmFuY2VkCgo="
  __md5_sum__ = "35e3720468131d675a18bb6f3e5f22f8"

  target_frame: string
  source_frame: string
  source_time: time
  timeout: duration
  target_time: time
  fixed_frame: string
  advanced: boolean
