# SPDX-FileCopyright Text: 2023 Kento Tsutsui
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16

class Listener():
    def __init__(self):
        self.pub = node.create_subscription(Int16, "countup", cb, 10)


def cb(msg):
    global node
    node.get_logger().info("Listen: %d" % msg.data)

rclpy.init()
node = Node("listener")
listener = Listener()
#pub = node.create_subscription(Int16, "countup", cb, 10)
rclpy.spin(node)
