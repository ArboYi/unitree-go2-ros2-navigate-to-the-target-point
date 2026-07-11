# Unitree Go2 ROS2 Autonomous Navigation

A ROS 2 Humble based autonomous navigation project for the Unitree Go2 quadruped robot, integrating SLAM and Nav2 for autonomous mapping and point-to-point navigation in a simulated factory environment.

## Overview

This project is developed based on the Unitree Go2 ROS 2 configuration files from:

https://github.com/anujjain-dev/unitree-go2-ros2

The original project provides configuration files for the **Unitree Go2 robot configured with the CHAMP controller in ROS 2 Humble**.

Based on this foundation, this project extends the robot simulation and navigation capabilities by adding:

* SLAM-based mapping
* Nav2 autonomous navigation
* Point-to-point navigation in RViz
* Factory environment simulation

The goal of this project is to enable autonomous navigation and inspection tasks for a quadruped robot in a simulated industrial environment.

---

## Features

### ✅ Working Gazebo Demo with SLAM

A complete Gazebo simulation demo with SLAM integration.

Capabilities:

* Real-time map building
* LiDAR-based environment perception
* Robot localization
* Map generation and saving

Launch:

```bash
ros2 launch go2_config slam.launch.py
```

---

### ✅ Working Gazebo Demo with Nav2 Integration

A complete Nav2 navigation demo based on a pre-built map.

Capabilities:

* Loading an existing map
* Global path planning
* Local obstacle avoidance
* RViz 2D Goal Pose navigation
* Point-to-point autonomous navigation

Launch:

```bash
ros2 launch go2_config navigate.launch.py
```

---

### ✅ Factory Environment Simulation

The factory/warehouse Gazebo world is based on:

https://github.com/wh200720041/warehouse_simulation_toolkit

The environment is used for testing robot navigation and inspection scenarios.

---

## Software Environment

* Ubuntu 22.04
* ROS 2 Humble
* Gazebo Classic 11
* RViz2
* CHAMP Controller
* SLAM Toolbox
* Nav2

---


# Launch Instructions

## 1. Start Unitree Go2 Gazebo Simulation

Launch the Unitree Go2 robot and its sensors (including LiDAR) in Gazebo:

```bash
ros2 launch go2_config gazebo_velodyne.launch.py
```

This will start:

* Unitree Go2 quadruped robot
* CHAMP controller
* Gazebo simulation environment
* Velodyne LiDAR sensor

---

## 2. SLAM Mapping

To build a map:

```bash
ros2 launch go2_config slam.launch.py
```

Move the robot around the environment to collect sensor information.

After completing mapping, save the generated map for later navigation.

---

## 3. Nav2 Point-to-Point Navigation

The factory map has already been created in this project:

```bash
ros2 launch go2_config navigate.launch.py
```

Then use RViz:

```
2D Pose Estimate
2D Goal Pose
```

to send navigation goals.

The robot will autonomously plan and navigate to the target point.

---

## 4. Using Your Own Gazebo World

If you want to use a custom Gazebo world, modify the world path in:

```
src/unitree-go2-ros2/robots/configs/go2_config/launch/gazebo_velodyne.launch.py
```

Replace the default world path with your own `.world` file.


After modification, rebuild:

```bash
colcon build

source install/setup.bash
```

---


## Acknowledgements

This project is built upon the following open-source projects:

### Unitree Go2 ROS2 Configuration

Original repository:

https://github.com/anujjain-dev/unitree-go2-ros2

Provides:

* Unitree Go2 robot configuration files
* CHAMP controller integration
* ROS 2 Humble support

---

### Warehouse Simulation Toolkit

Original repository:

https://github.com/wh200720041/warehouse_simulation_toolkit

Provides:

* Factory/warehouse Gazebo simulation environment

---

## License

This project is for research and educational purposes.
Thanks to the original authors for providing open-source resources.
