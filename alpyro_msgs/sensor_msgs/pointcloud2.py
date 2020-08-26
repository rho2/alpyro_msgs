from typing import List
from typing_extensions import Annotated
from typing import Final
from alpyro_msgs import RosMessage, boolean, uint32, uint8
from alpyro_msgs.sensor_msgs.pointfield import PointField
from alpyro_msgs.std_msgs.header import Header


class PointCloud2(RosMessage):
  __msg_typ__ = "sensor_msgs/PointCloud2"
  __msg_def__ = "c3RkX21zZ3MvSGVhZGVyIGhlYWRlcgogIHVpbnQzMiBzZXEKICB0aW1lIHN0YW1wCiAgc3RyaW5nIGZyYW1lX2lkCnVpbnQzMiBoZWlnaHQKdWludDMyIHdpZHRoCnNlbnNvcl9tc2dzL1BvaW50RmllbGRbXSBmaWVsZHMKICB1aW50OCBJTlQ4PTEKICB1aW50OCBVSU5UOD0yCiAgdWludDggSU5UMTY9MwogIHVpbnQ4IFVJTlQxNj00CiAgdWludDggSU5UMzI9NQogIHVpbnQ4IFVJTlQzMj02CiAgdWludDggRkxPQVQzMj03CiAgdWludDggRkxPQVQ2ND04CiAgc3RyaW5nIG5hbWUKICB1aW50MzIgb2Zmc2V0CiAgdWludDggZGF0YXR5cGUKICB1aW50MzIgY291bnQKYm9vbCBpc19iaWdlbmRpYW4KdWludDMyIHBvaW50X3N0ZXAKdWludDMyIHJvd19zdGVwCnVpbnQ4W10gZGF0YQpib29sIGlzX2RlbnNlCgo="
  __md5_sum__ = "1158d486dd51d683ce2f1be655c3c181"

  header: Header
  height: uint32
  width: uint32
  fields: Annotated[List[PointField], 0, 0]
  is_bigendian: boolean
  point_step: uint32
  row_step: uint32
  data: Annotated[bytes, 0, 0]
  is_dense: boolean
