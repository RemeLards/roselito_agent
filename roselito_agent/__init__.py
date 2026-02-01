#!/usr/bin/env python

# Copyright (C) 2025 Helio Perroni Filho (xperroni@gmail.com)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

r'''Module placeholder.
'''

import geometry_msgs.msg

import rclpy

class ParameterNode(rclpy.node.Node):
    def __init__(self, node_name: str):
        super().__init__(node_name)

        self.declare_parameter('global_frame', 'map')
        self.declare_parameter('robot_base_frame', 'base_footprint')
        self.declare_parameter('save_path', 'route.pon')

        # One '_' so Child Classes can access parameters
        self._global_frame = self.get_parameter('global_frame').value
        self._robot_frame = self.get_parameter('robot_base_frame').value
        self._save_path = self.get_parameter('save_path').value

def get_current_pose(
    now,
    transform,
    frame_id,
) -> geometry_msgs.msg.PoseStamped :
    pose = geometry_msgs.msg.PoseStamped()
    pose.header.frame_id = frame_id
    pose.header.stamp = now

    translation = transform.transform.translation
    pose.pose.position.x = translation.x
    pose.pose.position.y = translation.y
    pose.pose.position.z = translation.z
    pose.pose.orientation = transform.transform.rotation

    return pose