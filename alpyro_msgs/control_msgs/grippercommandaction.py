from typing import Final
from alpyro_msgs import RosMessage
from alpyro_msgs.control_msgs.grippercommandactiongoal import GripperCommandActionGoal
from alpyro_msgs.control_msgs.grippercommandactionfeedback import GripperCommandActionFeedback
from alpyro_msgs.control_msgs.grippercommandactionresult import GripperCommandActionResult


class GripperCommandAction(RosMessage):
  __msg_typ__ = "control_msgs/GripperCommandAction"
  __msg_def__ = "Y29udHJvbF9tc2dzL0dyaXBwZXJDb21tYW5kQWN0aW9uR29hbCBhY3Rpb25fZ29hbAogIHN0ZF9tc2dzL0hlYWRlciBoZWFkZXIKICAgIHVpbnQzMiBzZXEKICAgIHRpbWUgc3RhbXAKICAgIHN0cmluZyBmcmFtZV9pZAogIGFjdGlvbmxpYl9tc2dzL0dvYWxJRCBnb2FsX2lkCiAgICB0aW1lIHN0YW1wCiAgICBzdHJpbmcgaWQKICBjb250cm9sX21zZ3MvR3JpcHBlckNvbW1hbmRHb2FsIGdvYWwKICAgIGNvbnRyb2xfbXNncy9HcmlwcGVyQ29tbWFuZCBjb21tYW5kCiAgICAgIGZsb2F0NjQgcG9zaXRpb24KICAgICAgZmxvYXQ2NCBtYXhfZWZmb3J0CmNvbnRyb2xfbXNncy9HcmlwcGVyQ29tbWFuZEFjdGlvblJlc3VsdCBhY3Rpb25fcmVzdWx0CiAgc3RkX21zZ3MvSGVhZGVyIGhlYWRlcgogICAgdWludDMyIHNlcQogICAgdGltZSBzdGFtcAogICAgc3RyaW5nIGZyYW1lX2lkCiAgYWN0aW9ubGliX21zZ3MvR29hbFN0YXR1cyBzdGF0dXMKICAgIHVpbnQ4IFBFTkRJTkc9MAogICAgdWludDggQUNUSVZFPTEKICAgIHVpbnQ4IFBSRUVNUFRFRD0yCiAgICB1aW50OCBTVUNDRUVERUQ9MwogICAgdWludDggQUJPUlRFRD00CiAgICB1aW50OCBSRUpFQ1RFRD01CiAgICB1aW50OCBQUkVFTVBUSU5HPTYKICAgIHVpbnQ4IFJFQ0FMTElORz03CiAgICB1aW50OCBSRUNBTExFRD04CiAgICB1aW50OCBMT1NUPTkKICAgIGFjdGlvbmxpYl9tc2dzL0dvYWxJRCBnb2FsX2lkCiAgICAgIHRpbWUgc3RhbXAKICAgICAgc3RyaW5nIGlkCiAgICB1aW50OCBzdGF0dXMKICAgIHN0cmluZyB0ZXh0CiAgY29udHJvbF9tc2dzL0dyaXBwZXJDb21tYW5kUmVzdWx0IHJlc3VsdAogICAgZmxvYXQ2NCBwb3NpdGlvbgogICAgZmxvYXQ2NCBlZmZvcnQKICAgIGJvb2wgc3RhbGxlZAogICAgYm9vbCByZWFjaGVkX2dvYWwKY29udHJvbF9tc2dzL0dyaXBwZXJDb21tYW5kQWN0aW9uRmVlZGJhY2sgYWN0aW9uX2ZlZWRiYWNrCiAgc3RkX21zZ3MvSGVhZGVyIGhlYWRlcgogICAgdWludDMyIHNlcQogICAgdGltZSBzdGFtcAogICAgc3RyaW5nIGZyYW1lX2lkCiAgYWN0aW9ubGliX21zZ3MvR29hbFN0YXR1cyBzdGF0dXMKICAgIHVpbnQ4IFBFTkRJTkc9MAogICAgdWludDggQUNUSVZFPTEKICAgIHVpbnQ4IFBSRUVNUFRFRD0yCiAgICB1aW50OCBTVUNDRUVERUQ9MwogICAgdWludDggQUJPUlRFRD00CiAgICB1aW50OCBSRUpFQ1RFRD01CiAgICB1aW50OCBQUkVFTVBUSU5HPTYKICAgIHVpbnQ4IFJFQ0FMTElORz03CiAgICB1aW50OCBSRUNBTExFRD04CiAgICB1aW50OCBMT1NUPTkKICAgIGFjdGlvbmxpYl9tc2dzL0dvYWxJRCBnb2FsX2lkCiAgICAgIHRpbWUgc3RhbXAKICAgICAgc3RyaW5nIGlkCiAgICB1aW50OCBzdGF0dXMKICAgIHN0cmluZyB0ZXh0CiAgY29udHJvbF9tc2dzL0dyaXBwZXJDb21tYW5kRmVlZGJhY2sgZmVlZGJhY2sKICAgIGZsb2F0NjQgcG9zaXRpb24KICAgIGZsb2F0NjQgZWZmb3J0CiAgICBib29sIHN0YWxsZWQKICAgIGJvb2wgcmVhY2hlZF9nb2FsCgo="
  __md5_sum__ = "950b2a6ebe831f5d4f4ceaba3d8be01e"

  action_goal: GripperCommandActionGoal
  action_result: GripperCommandActionResult
  action_feedback: GripperCommandActionFeedback
