#========================================================
#Using Open Loop Control

#========================================================

#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import PoseStamped
from geometry_msgs.msg import Twist, Vector3
from move_base_msgs.msg import MoveBaseActionGoal, MoveBaseAction, MoveBaseGoal, MoveBaseActionResult

class Turtlebot:
  def __init__(self):
    # list that will receive the waypoints:
    self.waypoints = []
    # starting node waypoints nav:
    rospy.init_node('waypointsnav')
    # instance of the object that will publish in the topical move base:
    self.move_base_pub = rospy.Publisher("/move_base_simple/goal", PoseStamped, queue_size=1)

  # method for adding new points to the list::
  def add_waypoint(self, list):
    self.waypoints.append(list)

  # publish the position on the move_base, taking into account the map coordinate (0,0):
  def goal_move_base(self, pose_x, pose_y, pose_z, pose_w):
    msg_move_to_goal = PoseStamped()
    msg_move_to_goal.pose.position.x = pose_x 
    msg_move_to_goal.pose.position.y = pose_y
    msg_move_to_goal.pose.orientation.z = pose_z
    msg_move_to_goal.pose.orientation.w = pose_w
    msg_move_to_goal.header.frame_id = 'map'

    rospy.sleep(1)

    self.move_base_pub.publish(msg_move_to_goal)
    
  # navigate between the points, waiting to arrive at one point before going to the other:
  def nav_into_points(self):
    for i in range(len(self.waypoints)):
      self.goal_move_base(self.waypoints[i][0], self.waypoints[i][1], self.waypoints[i][2], self.waypoints[i][3])
      rospy.wait_for_message("/move_base/result", MoveBaseActionResult, timeout=None)

if __name__ == '__main__':
  robot = Turtlebot()  
  
  robot.add_waypoint([-6.1,-1.0,-0.7,0.7])
  robot.add_waypoint([1.1,3.4,-0.7,0.7])
  robot.add_waypoint([6.2,-0.9,-0.7,0.7])
  robot.add_waypoint([1.2,3.3,-0.7,0.7])
  robot.add_waypoint([-6.1,-1.0,-0.7,0.7])
  
  robot.nav_into_points()
