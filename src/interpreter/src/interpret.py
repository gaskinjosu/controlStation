#!/usr/bin/env python
import roslib; roslib.load_manifest('interpreter')
import rospy
import tf.transformations
from geometry_msgs.msg import Twist
from std_msgs.msg import Int32
#from interpreter.msg import i2c

autoStatus = 0


#############ATTEMPT TO DO I2C#########
#import smbus

#Set this same address in the arduino:
#address = 0x04
#bus = smbus.SMBus(1)


######################################

def move_callback(msg):
 
    if(autoStatus == 0):
       
        #These will hold the thruster values to be sent over I2c
        thruster1 = 0
        thruster2 = 0
        thruster3 = 0
        thruster4 = 0
        thruster5 = 0

        #These are the Id's of the individual thrusters that will accompany the above
        #data that is being sent (these match the ID's that are used in the embedded system arduino code)
        id1 = 11
        id2 = 12
        id3 = 13
        id4 = 14
        id5 = 15

        #The following code takes the Twist messages from the control station
        #and maps them to thruster values for sending 
        # via I2C. (these values will be between 0 and 20 - inclusive, 
        #because the Twist components will have a mangnitude of
        # at most 10)

        #Handling requests for strafing movement in XY plane
        if (msg.linear.x >= 0):
            thruster4 = msg.linear.x
            thruster2 = msg.linear.x
        elif (msg.linear.x < 0):
            thruster4 = abs(msg.linear.x) + 10
            thruster2 = abs(msg.linear.x) + 10

        if (msg.linear.y >= 0):
            thruster1 = msg.linear.y
            thruster3 = msg.linear.y
        elif (msg.linear.y < 0):
            thruster1 = abs(msg.linear.y) + 10
            thruster3 = abs(msg.linear.y) + 10

        # Handling requests for up/down movement
        if (msg.linear.z >= 0):
            thruster5 = msg.linear.z
        elif (msg.linear.z < 0):
            thruster5 = abs(msg.linear.z) + 10

        #Handling requests for turning movement (mutually exclusive from strafing)
        if (msg.angular.z < 0):
            thruster4 = abs(msg.angular.z) + 10
            thruster2 = abs(msg.angular.z)
        elif (msg.angular.z > 0):
            thruster4 = msg.angular.z
            thruster2 = msg.angular.z + 10

        #Will need to publish the following: 
        rospy.loginfo("Publishing the following for the I2C node")
        rospy.loginfo("Thruster1: %d:%d"%(id1,thruster1))
        rospy.loginfo("Thruster2: %d:%d"%(id2,thruster2))
        rospy.loginfo("Thruster3: %d:%d"%(id3,thruster3))
        rospy.loginfo("Thruster4: %d:%d"%(id4,thruster4))
        rospy.loginfo("Thruster5: %d:%d"%(id5,thruster5))

        #Note that this means that for each command from the control station (individual button press),
        #this interpreter node will parse what the control station has published and will produce a set of commands
        # for the thrusters, that it will in turn publish. Then, the I2C node will take this published information, and
        # will pass it to the arduino embedded system over I2C. The embedded system will continue to hold all thrusters 
        # in the same state until it receieves another command.

	###I2C ATTEMPT##########
	#bus.write_byte_data(address,id1,thruster1)
	#bus.write_byte_data(address,id2,thruster2)
	#bus.write_byte_data(address,id3,thruster3)
	#bus.write_byte_data(address,id4,thruster4)
	#bus.write_byte_data(address,id5,thruster5)
	#######################

def manip_callback(msg):

    if(autoStatus == 0):
        #This is the ID of the servo that matches the one in the embedded system
        #(used for identifying this servo I2C messages)
        servoid = 10
        servoState = 0

        #The control station should be sending the correct message for controlling the manipulator,
        #So this value simply needs to be passed on to the embedded system (no manipulation required)
        servoState = msg.data

        rospy.loginfo("Publishing the following for the I2C node")
        rospy.loginfo("Manipulator: %d:%d"%(servoid,servoState))


	###I2C ATTEMPT##########
	#bus.write_byte_data(address,servoid,serovState)
	#######################

def auto_callback(msg):
    
    #Change a global variable to reflect the new autonomous status
    #This global variable will be used to prevent the other callback functions for 
    # handling input from the control station from publishing data while the robot is
    # in auto mode.
    global autoStatus
    if(msg.data == -1):
        autoStatus = 0
    if(msg.data == 1):
        autoStatus = 1

def listener():

    
    rospy.init_node('interpreter')
    rospy.Subscriber('/move_command',Twist,move_callback)
    rospy.Subscriber('/manip_command',Int32,manip_callback)
    rospy.Subscriber('/auto_status',Int32,auto_callback)
    #rospy.Publisher('/iout',i2c,queue_size=10) 

    rospy.spin()

if __name__ == '__main__':
    listener()
