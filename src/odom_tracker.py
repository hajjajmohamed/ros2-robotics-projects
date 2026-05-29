#!/usr/bin/env python3
# Odometry Tracker - Tracks robot position
# Author: Mohamed Hajjaj - The Inventor Hero

import rclpy
from rclpy.node import Node
from nav_msgs.msg import Odometry
import math

class OdomTracker(Node):
    def __init__(self):
        super().__init__('odom_tracker')
        self.create_subscription(Odometry, '/odom', self.odom_callback, 10)
        self.start_x = None
        self.start_y = None
        self.get_logger().info('Odometry Tracker Started')

    def odom_callback(self, msg):
        x = msg.pose.pose.position.x
        y = msg.pose.pose.position.y
        qz = msg.pose.pose.orientation.z
        qw = msg.pose.pose.orientation.w
        yaw = math.atan2(2 * qw * qz, 1 - 2 * qz * qz)

        if self.start_x is None:
            self.start_x = x
            self.start_y = y

        distance = math.sqrt(
            (x - self.start_x) ** 2 +
            (y - self.start_y) ** 2
        )
        self.get_logger().info(
            f'Position: ({x:.2f}, {y:.2f}) | '
            f'Yaw: {math.degrees(yaw):.1f}deg | '
            f'Distance: {distance:.2f}m'
        )

def main(args=None):
    rclpy.init(args=args)
    node = OdomTracker()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
