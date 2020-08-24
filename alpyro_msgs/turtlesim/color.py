from alpyro_msgs import RosMessage, uint8


class Color(RosMessage):
  __msg_typ__ = "turtlesim/Color"
  __msg_def__ = "dWludDggcgp1aW50OCBnCnVpbnQ4IGIKCg=="
  __md5_sum__ = "353891e354491c51aabe32df673fb446"

  r: uint8
  g: uint8
  b: uint8
