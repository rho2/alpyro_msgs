from typing import Final
from alpyro_msgs import RosMessage, string, uint32, uint8


class MenuEntry(RosMessage):
  __msg_typ__ = "visualization_msgs/MenuEntry"
  __msg_def__ = "dWludDggRkVFREJBQ0s9MAp1aW50OCBST1NSVU49MQp1aW50OCBST1NMQVVOQ0g9Mgp1aW50MzIgaWQKdWludDMyIHBhcmVudF9pZApzdHJpbmcgdGl0bGUKc3RyaW5nIGNvbW1hbmQKdWludDggY29tbWFuZF90eXBlCgo="
  __md5_sum__ = "b90ec63024573de83b57aa93eb39be2d"

  FEEDBACK: Final[uint8] = 0
  ROSRUN: Final[uint8] = 1
  ROSLAUNCH: Final[uint8] = 2
  id: uint32
  parent_id: uint32
  title: string
  command: string
  command_type: uint8
