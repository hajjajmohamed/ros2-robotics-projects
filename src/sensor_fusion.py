#!/usr/bin/env python3
# Sensor Fusion Node - Combines multiple sensor data
# Author: Mohamed Hajjaj - The Inventor Hero

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan, Range
from std_msgs.msg import Float32MultiArray
import numpy as np

class SensorFusion(Node):
    def __init__(self):
        super().__init__('sensor_fusion')
        self.publisher = self.create_publisher(Float32MultiArray, '/sensor_fusion/data', 10)
        self.create_subscription(LaserScan, '/scan',              self.lidar_cb,    10)
        self.create_subscription(Range,     '/ultrasonic/range',  self.ultrasonic_cb, 10)
        self.lidar_min    = float('inf')
        self.ultrasonic   = float('inf')
        self.timer = self.create_timer(0.1, self.publish_fused)
        self.get_logger().info('Sensor Fusion Node Started')

    def lidar_cb(self, msg):
        valid = [r for r in msg.ranges if 0.1 < r < 10.0]
        self.lidar_min = min(valid) if valid else float('inf')

    def ultrasonic_cb(self, msg):
        self.ultrasonic = msg.range

    def publish_fused(self):
        fused_distance = min(self.lidar_min, self.ultrasonic)
        msg = Float32MultiArray()
        msg.data = [self.lidar_min, self.ultrasonic, fused_distance]
        self.publisher.publish(msg)
        self.get_logger().info(
            f'Lidar: {self.lidar_min:.2f}m | '
            f'Ultrasonic: {self.ultrasonic:.2f}m | '
            f'Fused: {fused_distance:.2f}m'
        )

def main(args=None):
    rclpy.init(args=args)
    node = SensorFusion()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
