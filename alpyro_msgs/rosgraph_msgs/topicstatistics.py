from alpyro_msgs import RosMessage, duration, int32, string, time


class TopicStatistics(RosMessage):
  __msg_typ__ = "rosgraph_msgs/TopicStatistics"
  __msg_def__ = "c3RyaW5nIHRvcGljCnN0cmluZyBub2RlX3B1YgpzdHJpbmcgbm9kZV9zdWIKdGltZSB3aW5kb3dfc3RhcnQKdGltZSB3aW5kb3dfc3RvcAppbnQzMiBkZWxpdmVyZWRfbXNncwppbnQzMiBkcm9wcGVkX21zZ3MKaW50MzIgdHJhZmZpYwpkdXJhdGlvbiBwZXJpb2RfbWVhbgpkdXJhdGlvbiBwZXJpb2Rfc3RkZGV2CmR1cmF0aW9uIHBlcmlvZF9tYXgKZHVyYXRpb24gc3RhbXBfYWdlX21lYW4KZHVyYXRpb24gc3RhbXBfYWdlX3N0ZGRldgpkdXJhdGlvbiBzdGFtcF9hZ2VfbWF4Cgo="
  __md5_sum__ = "10152ed868c5097a5e2e4a89d7daa710"

  topic: string
  node_pub: string
  node_sub: string
  window_start: time
  window_stop: time
  delivered_msgs: int32
  dropped_msgs: int32
  traffic: int32
  period_mean: duration
  period_stddev: duration
  period_max: duration
  stamp_age_mean: duration
  stamp_age_stddev: duration
  stamp_age_max: duration
