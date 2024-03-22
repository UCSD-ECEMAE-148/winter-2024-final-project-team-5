from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='selfparking',
            executable='parking_recog',
            name='parking_recog',
            output='screen'
        )
    ])