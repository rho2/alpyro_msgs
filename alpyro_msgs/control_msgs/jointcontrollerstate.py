from alpyro_msgs import RosMessage, boolean, float64
from alpyro_msgs.std_msgs.header import Header


class JointControllerState(RosMessage):
  __msg_typ__ = "control_msgs/JointControllerState"
  __msg_def__ = "c3RkX21zZ3MvSGVhZGVyIGhlYWRlcgogIHVpbnQzMiBzZXEKICB0aW1lIHN0YW1wCiAgc3RyaW5nIGZyYW1lX2lkCmZsb2F0NjQgc2V0X3BvaW50CmZsb2F0NjQgcHJvY2Vzc192YWx1ZQpmbG9hdDY0IHByb2Nlc3NfdmFsdWVfZG90CmZsb2F0NjQgZXJyb3IKZmxvYXQ2NCB0aW1lX3N0ZXAKZmxvYXQ2NCBjb21tYW5kCmZsb2F0NjQgcApmbG9hdDY0IGkKZmxvYXQ2NCBkCmZsb2F0NjQgaV9jbGFtcApib29sIGFudGl3aW5kdXAKCg=="
  __md5_sum__ = "987ad85e4756f3aef7f1e5e7fe0595d1"

  header: Header
  set_point: float64
  process_value: float64
  process_value_dot: float64
  error: float64
  time_step: float64
  command: float64
  p: float64
  i: float64
  d: float64
  i_clamp: float64
  antiwindup: boolean
