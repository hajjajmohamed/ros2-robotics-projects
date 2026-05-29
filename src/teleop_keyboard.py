#!/usr/bin/env python3
# Keyboard Teleoperation Node
# Author: Mohamed Hajjaj - The Inventor Hero

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import sys, tty, termios

KEYS = {
    'w': ( 0.3,  0.0),
    's': (-0.3,  0.0),
    'a': ( 0.0,  0.5),
    'd': ( 0.0, -0.5),
    ' ': ( 0.0,  0.0),
}

MSG = """
Keyboard Teleop - The Inventor Hero
------------------------------------
W : Forward    S : Backward
A : Turn Left  D : Turn Right
SPACE : Stop   Q : Quit
------------------------------------
"""

def get_key():
    fd = sys.stdin.fileno()
    old = termios.tcgetattr(fd)
    try:
        tty.setraw(fd)
        return sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old)

class TeleopKeyboard(Node):
    def __init__(self):
        super().__init__('teleop_keyboard')
        self.pub = self.create_publisher(Twist, '/cmd_vel', 10)
        self.get_logger().info('Teleop Keyboard Node Started')

def main(args=None):
    rclpy.init(args=args)
    node = TeleopKeyboard()
    print(MSG)
    try:
        while rclpy.ok():
            key = get_key()
            if key == 'q':
                break
            if key in KEYS:
                linear, angular = KEYS[key]
                twist = Twist()
                twist.linear.x  = linear
                twist.angular.z = angular
                node.pub.publish(twist)
                print(f'Key: {key} | Linear: {linear} | Angular: {angular}')
    except Exception as e:
        print(e)
    finally:
        node.pub.publish(Twist())
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
