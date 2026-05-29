#!/usr/bin/env python3
# Autonomous Navigator - ROS2 Nav2
# Author: Mohamed Hajjaj - The Inventor Hero

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import PoseStamped, Twist
from nav_msgs.msg import Odometry
from sensor_msgs.msg import LaserScan
import math

class AutonomousNavigator(Node):
    def __init__(self):
        super().__init__('autonomous_navigator')
        self.cmd_pub = self.create_publisher(Twist, '/cmd_vel', 10)
        self.create_subscription(LaserScan, '/scan', self.scan_callback, 10)
        self.create_subscription(Odometry,  '/odom', self.odom_callback,  10)
        self.obstacle_front = False
        self.position = (0.0, 0.0)
        self.timer = self.create_timer(0.1, self.navigate)
        self.get_logger().info('Autonomous Navigator Started')

    def scan_callback(self, msg):
        front = msg.ranges[0:30] + msg.ranges[330:360]
        valid = [r for r in front if 0.1 < r < 10.0]
        self.obstacle_front = bool(valid and min(valid) < 0.5)

    def odom_callback(self, msg):
        self.position = (
            msg.pose.pose.position.x,
            msg.pose.pose.position.y
        )

    def navigate(self):
        twist = Twist()
        if self.obstacle_front:
            self.get_logger().warn('Obstacle! Turning...')
            twist.angular.z = 0.5
        else:
            twist.linear.x = 0.2
        self.cmd_pub.publish(twist)

def main(args=None):
    rclpy.init(args=args)
    node = AutonomousNavigator()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.cmd_pub.publish(Twist())
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
