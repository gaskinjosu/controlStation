execute_process(COMMAND "/home/jared/csws/build/mr_teleoperator/mr_rqt/catkin_generated/python_distutils_install.sh" RESULT_VARIABLE res)

if(NOT res EQUAL 0)
  message(FATAL_ERROR "execute_process(/home/jared/csws/build/mr_teleoperator/mr_rqt/catkin_generated/python_distutils_install.sh) returned error code ")
endif()
