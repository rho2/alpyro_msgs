from typing import Final
from alpyro_msgs import RosMessage, string, uint8
from alpyro_msgs.actionlib_msgs.goalid import GoalID


class GoalStatus(RosMessage):
  __msg_typ__ = "actionlib_msgs/GoalStatus"
  __msg_def__ = "dWludDggUEVORElORz0wCnVpbnQ4IEFDVElWRT0xCnVpbnQ4IFBSRUVNUFRFRD0yCnVpbnQ4IFNVQ0NFRURFRD0zCnVpbnQ4IEFCT1JURUQ9NAp1aW50OCBSRUpFQ1RFRD01CnVpbnQ4IFBSRUVNUFRJTkc9Ngp1aW50OCBSRUNBTExJTkc9Nwp1aW50OCBSRUNBTExFRD04CnVpbnQ4IExPU1Q9OQphY3Rpb25saWJfbXNncy9Hb2FsSUQgZ29hbF9pZAogIHRpbWUgc3RhbXAKICBzdHJpbmcgaWQKdWludDggc3RhdHVzCnN0cmluZyB0ZXh0Cgo="
  __md5_sum__ = "d388f9b87b3c471f784434d671988d4a"

  PENDING: Final[uint8] = 0
  ACTIVE: Final[uint8] = 1
  PREEMPTED: Final[uint8] = 2
  SUCCEEDED: Final[uint8] = 3
  ABORTED: Final[uint8] = 4
  REJECTED: Final[uint8] = 5
  PREEMPTING: Final[uint8] = 6
  RECALLING: Final[uint8] = 7
  RECALLED: Final[uint8] = 8
  LOST: Final[uint8] = 9
  goal_id: GoalID
  status: uint8
  text: string
