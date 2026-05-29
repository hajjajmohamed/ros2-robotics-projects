# ROS2 Robotics Projects

Collection of ROS2 robotics nodes for autonomous navigation, sensor fusion, and robot control.

## Projects Included

| Node                  | Description                          |
|-----------------------|--------------------------------------|
| autonomous_navigator  | Obstacle avoidance + auto navigation |
| sensor_fusion         | Combines LiDAR + ultrasonic data     |
| teleop_keyboard       | Keyboard teleoperation control       |
| odom_tracker          | Real-time position tracking          |

## Tech Stack

| Category  | Technologies              |
|-----------|---------------------------|
| Framework | ROS2 Humble               |
| Language  | Python 3, C++             |
| Hardware  | Raspberry Pi 4, LiDAR     |
| Simulator | Gazebo                    |
| OS        | Ubuntu 22.04              |

## Project Structure

    ros2-robotics-projects/
    src/
        autonomous_navigator.py  - Auto navigation with obstacle avoidance
        sensor_fusion.py         - Multi-sensor data fusion
        teleop_keyboard.py       - Keyboard robot control
        odom_tracker.py          - Position and distance tracking
    docs/
        setup.md                 - ROS2 installation guide
    media/
    requirements.txt

## Installation

    git clone https://github.com/hajjajmohamed/ros2-robotics-projects.git
    cd ros2-robotics-projects
    source /opt/ros/humble/setup.bash
    python3 src/teleop_keyboard.py

## Author
Mohamed Hajjaj - The Inventor Hero
National Innovation Champion 2026
GITEX Africa 2026 Participant
GitHub: https://github.com/hajjajmohamed
Instagram: https://instagram.com/the.inventor.hero
