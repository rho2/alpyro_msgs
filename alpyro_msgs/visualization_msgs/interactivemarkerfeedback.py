from typing import Final
from alpyro_msgs import RosMessage, boolean, string, uint32, uint8
from alpyro_msgs.geometry_msgs.point import Point
from alpyro_msgs.geometry_msgs.pose import Pose
from alpyro_msgs.std_msgs.header import Header


class InteractiveMarkerFeedback(RosMessage):
  __msg_typ__ = "visualization_msgs/InteractiveMarkerFeedback"
  __msg_def__ = "dWludDggS0VFUF9BTElWRT0wCnVpbnQ4IFBPU0VfVVBEQVRFPTEKdWludDggTUVOVV9TRUxFQ1Q9Mgp1aW50OCBCVVRUT05fQ0xJQ0s9Mwp1aW50OCBNT1VTRV9ET1dOPTQKdWludDggTU9VU0VfVVA9NQpzdGRfbXNncy9IZWFkZXIgaGVhZGVyCiAgdWludDMyIHNlcQogIHRpbWUgc3RhbXAKICBzdHJpbmcgZnJhbWVfaWQKc3RyaW5nIGNsaWVudF9pZApzdHJpbmcgbWFya2VyX25hbWUKc3RyaW5nIGNvbnRyb2xfbmFtZQp1aW50OCBldmVudF90eXBlCmdlb21ldHJ5X21zZ3MvUG9zZSBwb3NlCiAgZ2VvbWV0cnlfbXNncy9Qb2ludCBwb3NpdGlvbgogICAgZmxvYXQ2NCB4CiAgICBmbG9hdDY0IHkKICAgIGZsb2F0NjQgegogIGdlb21ldHJ5X21zZ3MvUXVhdGVybmlvbiBvcmllbnRhdGlvbgogICAgZmxvYXQ2NCB4CiAgICBmbG9hdDY0IHkKICAgIGZsb2F0NjQgegogICAgZmxvYXQ2NCB3CnVpbnQzMiBtZW51X2VudHJ5X2lkCmdlb21ldHJ5X21zZ3MvUG9pbnQgbW91c2VfcG9pbnQKICBmbG9hdDY0IHgKICBmbG9hdDY0IHkKICBmbG9hdDY0IHoKYm9vbCBtb3VzZV9wb2ludF92YWxpZAoK"
  __md5_sum__ = "ab0f1eee058667e28c19ff3ffc3f4b78"

  KEEP_ALIVE: Final[uint8] = 0
  POSE_UPDATE: Final[uint8] = 1
  MENU_SELECT: Final[uint8] = 2
  BUTTON_CLICK: Final[uint8] = 3
  MOUSE_DOWN: Final[uint8] = 4
  MOUSE_UP: Final[uint8] = 5
  header: Header
  client_id: string
  marker_name: string
  control_name: string
  event_type: uint8
  pose: Pose
  menu_entry_id: uint32
  mouse_point: Point
  mouse_point_valid: boolean
