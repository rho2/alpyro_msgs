from typing import Final
from alpyro_msgs import RosMessage, int8, uint16


class NavSatStatus(RosMessage):
  __msg_typ__ = "sensor_msgs/NavSatStatus"
  __msg_def__ = "aW50OCBTVEFUVVNfTk9fRklYPS0xCmludDggU1RBVFVTX0ZJWD0wCmludDggU1RBVFVTX1NCQVNfRklYPTEKaW50OCBTVEFUVVNfR0JBU19GSVg9Mgp1aW50MTYgU0VSVklDRV9HUFM9MQp1aW50MTYgU0VSVklDRV9HTE9OQVNTPTIKdWludDE2IFNFUlZJQ0VfQ09NUEFTUz00CnVpbnQxNiBTRVJWSUNFX0dBTElMRU89OAppbnQ4IHN0YXR1cwp1aW50MTYgc2VydmljZQoK"
  __md5_sum__ = "331cdbddfa4bc96ffc3b9ad98900a54c"

  STATUS_NO_FIX: Final[int8] = -1
  STATUS_FIX: Final[int8] = 0
  STATUS_SBAS_FIX: Final[int8] = 1
  STATUS_GBAS_FIX: Final[int8] = 2
  SERVICE_GPS: Final[uint16] = 1
  SERVICE_GLONASS: Final[uint16] = 2
  SERVICE_COMPASS: Final[uint16] = 4
  SERVICE_GALILEO: Final[uint16] = 8
  status: int8
  service: uint16
