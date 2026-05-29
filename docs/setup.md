# ROS2 Setup Guide

## Install ROS2 Humble on Ubuntu 22.04

    sudo apt update && sudo apt install curl -y
    sudo curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key         -o /usr/share/keyrings/ros-archive-keyring.gpg
    echo "deb [arch=$(dpkg --print-architecture)         signed-by=/usr/share/keyrings/ros-archive-keyring.gpg]         http://packages.ros.org/ros2/ubuntu         $(. /etc/os-release && echo $UBUNTU_CODENAME) main" |         sudo tee /etc/apt/sources.list.d/ros2.list > /dev/null
    sudo apt update
    sudo apt install ros-humble-desktop -y

## Source ROS2

    echo "source /opt/ros/humble/setup.bash" >> ~/.bashrc
    source ~/.bashrc

## Run Nodes

    python3 src/teleop_keyboard.py
    python3 src/autonomous_navigator.py
    python3 src/sensor_fusion.py
    python3 src/odom_tracker.py
