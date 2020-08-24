FROM osrf/ros:noetic-desktop-focal

WORKDIR /alpyro
COPY gen_msgs.py /alpyro
COPY rosmsg /alpyro


ENTRYPOINT [ "/alpyro/gen_msgs.py" ]