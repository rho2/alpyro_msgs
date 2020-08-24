from alpyro_msgs import RosMessage, boolean, uint32


class RegionOfInterest(RosMessage):
  __msg_typ__ = "sensor_msgs/RegionOfInterest"
  __msg_def__ = "dWludDMyIHhfb2Zmc2V0CnVpbnQzMiB5X29mZnNldAp1aW50MzIgaGVpZ2h0CnVpbnQzMiB3aWR0aApib29sIGRvX3JlY3RpZnkKCg=="
  __md5_sum__ = "bdb633039d588fcccb441a4d43ccfe09"

  x_offset: uint32
  y_offset: uint32
  height: uint32
  width: uint32
  do_rectify: boolean
