from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='pointcloud_to_laserscan',
            executable='pointcloud_to_laserscan_node',
            name='pc_to_scan',
            parameters=[{
                'target_frame': 'base_link',
                'transform_tolerance': 0.01,
                'min_height': -0.2,
                'max_height': 0.5,
                'angle_min': -3.14,
                'angle_max': 3.14,
                'range_min': 0.1,
                'range_max': 10.0,
                'use_inf': True,
            }],
            remappings=[
                ('cloud_in', '/velodyne_points'),
                ('scan', '/scan'),
            ],
            # 关键：QoS修复
            qos_overrides={
                '/scan': {
                    'subscription': {
                        'reliability': 'best_effort'
                    }
                }
            }
        )
    ])