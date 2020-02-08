cmake_minimum_required(VERSION 2.8.3)
project(rov_teleop)


find_package(catkin REQUIRED COMPONENTS
  rospy
  rqt_gui
  rqt_gui_py
)

catkin_package()
## Uncomment this if the package has a setup.py. This macro ensures
## modules and global scripts declared therein get installed
## See http://ros.org/doc/api/catkin/html/user_guide/setup_dot_py.html
 catkin_python_setup()


###########
## Build ##
###########

## Specify additional locations of header files
## Your package locations should be listed before other locations
include_directories(
# include
  ${catkin_INCLUDE_DIRS}
)


#############
## Install ##
#############


install(PROGRAMS scripts/rov_teleop.py
	DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION})		

install(DIRECTORY resource
	DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION})

install(FILES plugin.xml
	DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION})




