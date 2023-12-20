# SPDX-FileCopyright Text: 2023 Kento Tsutsui
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16

class Listener():
    def __init__(self, node):
        self.node = node
        self.pub = node.create_subscription(Int16, "countup", self.cb, 10)

    def cb(self, msg):
        self.node.get_logger().info("Listen: %d" % msg.data)

def main():
    rclpy.init()
    node = Node("listener")
    listener = Listener(node)
    rclpy.spin(node)
