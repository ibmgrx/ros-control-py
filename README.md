#Documentation:

#For the first we need to pull ros docker image.
```
docker pull ros
docker pull ros:noetic-robot
```
#Then runnig ros image to setup
```
docker run –name roslocal -it ros
```
#In new terminal find your active container, make sure roslocal there
```
docker ps -l
```
#Running the container
```
docker exec -it roslocal bash
```
#Setup our environment
```
source ros_entrypoint.sh

source /opt/ros/noetic/setup.bash

echo "source /opt/ros/noetic/setup.bash" >> ~/.bashrc

source ~/.bashrc

sudo apt install python3-rosdep python3-rosinstall python3-rosinstall-generator python3-wstool build-essential

sudo apt install python3-rosdep
```
#Create a package
```
cd ~/catkin_ws/src

catkin_create_pkg py_control_1 py_control_2 rospy roscpp
```
#Build package
```
cd ~/catkin_ws

catkin_make

. ~/catkin_ws/devel/setup.bash
```
#Running roscore master
```
roscore
```
#Running package as node
```
roslaunch py_control_1 py_control_1.launch
```
#Or
```
roslaunch py_control_2 py_control_2.launch
```
#For testing using turtlebot3
```
sudo apt-get install ros-noetic-joy ros-noetic-teleop-twist-joy \
ros-noetic-teleop-twist-keyboard ros-noetic-laser-proc \
ros-noetic-rgbd-launch ros-noetic-rosserial-arduino \
ros-noetic-rosserial-python ros-noetic-rosserial-client \
ros-noetic-rosserial-msgs ros-noetic-amcl ros-noetic-map-server \
ros-noetic-move-base ros-noetic-urdf ros-noetic-xacro \
ros-noetic-compressed-image-transport ros-noetic-rqt* ros-noetic-rviz \
ros-noetic-gmapping ros-noetic-navigation ros-noetic-interactive-markers

cd ~/catkin_ws/src/
sudo apt install ros-noetic-dynamixel-sdk
sudo apt install ros-noetic-turtlebot3-msgs
sudo apt install ros-noetic-turtlebot3
git clone -b noetic-devel https://github.com/ROBOTIS-GIT/turtlebot3_simulations.git
cd ~/catkin_ws && catkin_make
sudo apt install ros-noetic-turtlebot3-gazebo
export TURTLEBOT3_MODEL=burger
roslaunch turtlebot3_gazebo turtlebot3_empty_world.launch
```
#For testing navigation
```
roslaunch turtlebot3_navigation turtlebot3_navigation.launch map_file:=$HOME/map.yaml
roslaunch turtlebot3_teleop turtlebot3_teleop_key.launch
```
