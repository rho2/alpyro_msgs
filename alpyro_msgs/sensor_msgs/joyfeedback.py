from typing import Final
from alpyro_msgs import RosMessage, float32, uint8


class JoyFeedback(RosMessage):
  __msg_typ__ = "sensor_msgs/JoyFeedback"
  __msg_def__ = "dWludDggVFlQRV9MRUQ9MAp1aW50OCBUWVBFX1JVTUJMRT0xCnVpbnQ4IFRZUEVfQlVaWkVSPTIKdWludDggdHlwZQp1aW50OCBpZApmbG9hdDMyIGludGVuc2l0eQoK"
  __md5_sum__ = "f4dcd73460360d98f36e55ee7f2e46f1"

  TYPE_LED: Final[uint8] = 0
  TYPE_RUMBLE: Final[uint8] = 1
  TYPE_BUZZER: Final[uint8] = 2
  type: uint8
  id: uint8
  intensity: float32
