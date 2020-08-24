from alpyro_msgs import RosMessage
from alpyro_msgs.control_msgs.grippercommand import GripperCommand


class GripperCommandGoal(RosMessage):
  __msg_typ__ = "control_msgs/GripperCommandGoal"
  __msg_def__ = "Y29udHJvbF9tc2dzL0dyaXBwZXJDb21tYW5kIGNvbW1hbmQKICBmbG9hdDY0IHBvc2l0aW9uCiAgZmxvYXQ2NCBtYXhfZWZmb3J0Cgo="
  __md5_sum__ = "86fd82f4ddc48a4cb6856cfa69217e43"

  command: GripperCommand
