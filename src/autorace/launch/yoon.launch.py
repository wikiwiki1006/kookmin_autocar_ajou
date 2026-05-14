import os
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    
    # 1. 실행할 첫 번째 노드 설정 (예: 카메라 노드)
    yoon_pub_node = Node(
        package='autorace',       # 패키지 이름
        executable='yoon_pub',      # setup.py의 entry_points에 등록했던 명령어 이름
        name='yoon_pub',        # 실행될 때 노드에 붙여줄 새로운 이름 (생략 가능)
        # output='screen'               # 터미널에 print(로그)를 출력하라는 뜻
    )

    # 2. 실행할 두 번째 노드 설정 (예: 모터 제어 노드)
    yoon_sub_node = Node(
        package='autorace',       
        executable='yoon_sub',       
        name='my_motor_node',         
        output='screen'
    )

    # 3. 위에서 설정한 노드들을 LaunchDescription에 담아서 반환
    return LaunchDescription([
        yoon_pub_node,
        yoon_sub_node
    ])