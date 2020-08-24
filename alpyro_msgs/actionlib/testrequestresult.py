from alpyro_msgs import RosMessage, boolean, int32


class TestRequestResult(RosMessage):
  __msg_typ__ = "actionlib/TestRequestResult"
  __msg_def__ = "aW50MzIgdGhlX3Jlc3VsdApib29sIGlzX3NpbXBsZV9zZXJ2ZXIKCg=="
  __md5_sum__ = "61c2364524499c7c5017e2f3fce7ba06"

  the_result: int32
  is_simple_server: boolean
