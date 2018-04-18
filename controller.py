#!/usr/bin/env python

from inputs import devices
from inputs import get_gamepad
import rospy
from rc_node.msg import car_input

def main():
  pub = rospy.Publisher('/car_input', car_input, queue_size=10)
  rospy.init_node('LogitechController')
  msg = car_input()
  
  while not rospy.is_shutdown():
    events = get_gamepad()
    # Simply read the events from the gamepad, and send them over ROS
    for event in events:
      print(event.code, event.state)
      if event.code =='ABS_X':
        msg.steer_angle = -event.state/32786.0*30.0
      if event.code =='ABS_RZ':
        msg.power = event.state/255.0
      elif event.code == 'ABS_Z':
        msg.power = -event.state/255.0

    pub.publish(msg)

if __name__ == '__main__':
  try:
    main()
  except rospy.ROSInterruptException:
    pass
