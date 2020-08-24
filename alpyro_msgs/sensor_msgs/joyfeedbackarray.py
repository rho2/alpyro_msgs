from typing import List
from typing_extensions import Annotated
from typing import Final
from alpyro_msgs import RosMessage
from alpyro_msgs.sensor_msgs.joyfeedback import JoyFeedback


class JoyFeedbackArray(RosMessage):
  __msg_typ__ = "sensor_msgs/JoyFeedbackArray"
  __msg_def__ = "c2Vuc29yX21zZ3MvSm95RmVlZGJhY2tbXSBhcnJheQogIHVpbnQ4IFRZUEVfTEVEPTAKICB1aW50OCBUWVBFX1JVTUJMRT0xCiAgdWludDggVFlQRV9CVVpaRVI9MgogIHVpbnQ4IHR5cGUKICB1aW50OCBpZAogIGZsb2F0MzIgaW50ZW5zaXR5Cgo="
  __md5_sum__ = "cde5730a895b1fc4dee6f91b754b213d"

  array: Annotated[List[JoyFeedback], 0, 0]
