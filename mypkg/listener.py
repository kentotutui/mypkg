# SPDX-FileCopyright Text: 2023 Kento Tsutsui
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from person_msgs.srv import Query

def main():
    rclpy.init()
    node = Node("listener")
    client = node.create_client(Query, 'query')
    while not client.wait_for_service(timeout_sec=1.0):
        node.get_logger().info('wait')

    req = Query.Request()
    req.name = "kento tsutsui"
    future = client.call_async(req)

    while rclpy.ok():
        rclpy.spin_once(node)
        if future.done():
            try:
                response = future.result()
            except:
                node.get_logger().info('call feiled')
            else:
                node.get_logger().info("age: {}".format(response.age))
            
            break

    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()