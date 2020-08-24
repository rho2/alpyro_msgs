from alpyro_msgs import RosMessage, float32


class ColorRGBA(RosMessage):
  __msg_typ__ = "std_msgs/ColorRGBA"
  __msg_def__ = "ZmxvYXQzMiByCmZsb2F0MzIgZwpmbG9hdDMyIGIKZmxvYXQzMiBhCgo="
  __md5_sum__ = "a29a96539573343b1310c73607334b00"

  r: float32
  g: float32
  b: float32
  a: float32
