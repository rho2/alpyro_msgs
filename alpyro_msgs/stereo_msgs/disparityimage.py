from typing import List
from typing_extensions import Annotated
from alpyro_msgs import RosMessage, float32
from alpyro_msgs.std_msgs.header import Header
from alpyro_msgs.sensor_msgs.image import Image
from alpyro_msgs.sensor_msgs.regionofinterest import RegionOfInterest


class DisparityImage(RosMessage):
  __msg_typ__ = "stereo_msgs/DisparityImage"
  __msg_def__ = "c3RkX21zZ3MvSGVhZGVyIGhlYWRlcgogIHVpbnQzMiBzZXEKICB0aW1lIHN0YW1wCiAgc3RyaW5nIGZyYW1lX2lkCnNlbnNvcl9tc2dzL0ltYWdlIGltYWdlCiAgc3RkX21zZ3MvSGVhZGVyIGhlYWRlcgogICAgdWludDMyIHNlcQogICAgdGltZSBzdGFtcAogICAgc3RyaW5nIGZyYW1lX2lkCiAgdWludDMyIGhlaWdodAogIHVpbnQzMiB3aWR0aAogIHN0cmluZyBlbmNvZGluZwogIHVpbnQ4IGlzX2JpZ2VuZGlhbgogIHVpbnQzMiBzdGVwCiAgdWludDhbXSBkYXRhCmZsb2F0MzIgZgpmbG9hdDMyIFQKc2Vuc29yX21zZ3MvUmVnaW9uT2ZJbnRlcmVzdCB2YWxpZF93aW5kb3cKICB1aW50MzIgeF9vZmZzZXQKICB1aW50MzIgeV9vZmZzZXQKICB1aW50MzIgaGVpZ2h0CiAgdWludDMyIHdpZHRoCiAgYm9vbCBkb19yZWN0aWZ5CmZsb2F0MzIgbWluX2Rpc3Bhcml0eQpmbG9hdDMyIG1heF9kaXNwYXJpdHkKZmxvYXQzMiBkZWx0YV9kCgo="
  __md5_sum__ = "04a177815f75271039fa21f16acad8c9"

  header: Header
  image: Image
  f: float32
  T: float32
  valid_window: RegionOfInterest
  min_disparity: float32
  max_disparity: float32
  delta_d: float32