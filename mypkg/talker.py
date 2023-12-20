# SPDX-FileCopyright Text: 2023 Kento Tsutsui
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from person_msgs.srv import Query

def cd(request, response):
    if request.name == "kento tsutsui":
        response.age = 20
    else:
        response.age = 255

    return response

rclpy.init()
node = Node("talker")
srv = node.create_service(Query, "query", cb)
rclpy.spin(node)