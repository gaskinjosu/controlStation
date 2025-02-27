# generated from genmsg/cmake/pkg-genmsg.cmake.em

message(STATUS "interpreter: 1 messages, 0 services")

set(MSG_I_FLAGS "-Iinterpreter:/home/jared/csws/src/interpreter/msg;-Istd_msgs:/opt/ros/melodic/share/std_msgs/cmake/../msg")

# Find all generators
find_package(gencpp REQUIRED)
find_package(geneus REQUIRED)
find_package(genlisp REQUIRED)
find_package(gennodejs REQUIRED)
find_package(genpy REQUIRED)

add_custom_target(interpreter_generate_messages ALL)

# verify that message/service dependencies have not changed since configure



get_filename_component(_filename "/home/jared/csws/src/interpreter/msg/i2c.msg" NAME_WE)
add_custom_target(_interpreter_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "interpreter" "/home/jared/csws/src/interpreter/msg/i2c.msg" "std_msgs/Header"
)

#
#  langs = gencpp;geneus;genlisp;gennodejs;genpy
#

### Section generating for lang: gencpp
### Generating Messages
_generate_msg_cpp(interpreter
  "/home/jared/csws/src/interpreter/msg/i2c.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/interpreter
)

### Generating Services

### Generating Module File
_generate_module_cpp(interpreter
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/interpreter
  "${ALL_GEN_OUTPUT_FILES_cpp}"
)

add_custom_target(interpreter_generate_messages_cpp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_cpp}
)
add_dependencies(interpreter_generate_messages interpreter_generate_messages_cpp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/jared/csws/src/interpreter/msg/i2c.msg" NAME_WE)
add_dependencies(interpreter_generate_messages_cpp _interpreter_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(interpreter_gencpp)
add_dependencies(interpreter_gencpp interpreter_generate_messages_cpp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS interpreter_generate_messages_cpp)

### Section generating for lang: geneus
### Generating Messages
_generate_msg_eus(interpreter
  "/home/jared/csws/src/interpreter/msg/i2c.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/interpreter
)

### Generating Services

### Generating Module File
_generate_module_eus(interpreter
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/interpreter
  "${ALL_GEN_OUTPUT_FILES_eus}"
)

add_custom_target(interpreter_generate_messages_eus
  DEPENDS ${ALL_GEN_OUTPUT_FILES_eus}
)
add_dependencies(interpreter_generate_messages interpreter_generate_messages_eus)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/jared/csws/src/interpreter/msg/i2c.msg" NAME_WE)
add_dependencies(interpreter_generate_messages_eus _interpreter_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(interpreter_geneus)
add_dependencies(interpreter_geneus interpreter_generate_messages_eus)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS interpreter_generate_messages_eus)

### Section generating for lang: genlisp
### Generating Messages
_generate_msg_lisp(interpreter
  "/home/jared/csws/src/interpreter/msg/i2c.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/interpreter
)

### Generating Services

### Generating Module File
_generate_module_lisp(interpreter
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/interpreter
  "${ALL_GEN_OUTPUT_FILES_lisp}"
)

add_custom_target(interpreter_generate_messages_lisp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_lisp}
)
add_dependencies(interpreter_generate_messages interpreter_generate_messages_lisp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/jared/csws/src/interpreter/msg/i2c.msg" NAME_WE)
add_dependencies(interpreter_generate_messages_lisp _interpreter_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(interpreter_genlisp)
add_dependencies(interpreter_genlisp interpreter_generate_messages_lisp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS interpreter_generate_messages_lisp)

### Section generating for lang: gennodejs
### Generating Messages
_generate_msg_nodejs(interpreter
  "/home/jared/csws/src/interpreter/msg/i2c.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/interpreter
)

### Generating Services

### Generating Module File
_generate_module_nodejs(interpreter
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/interpreter
  "${ALL_GEN_OUTPUT_FILES_nodejs}"
)

add_custom_target(interpreter_generate_messages_nodejs
  DEPENDS ${ALL_GEN_OUTPUT_FILES_nodejs}
)
add_dependencies(interpreter_generate_messages interpreter_generate_messages_nodejs)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/jared/csws/src/interpreter/msg/i2c.msg" NAME_WE)
add_dependencies(interpreter_generate_messages_nodejs _interpreter_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(interpreter_gennodejs)
add_dependencies(interpreter_gennodejs interpreter_generate_messages_nodejs)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS interpreter_generate_messages_nodejs)

### Section generating for lang: genpy
### Generating Messages
_generate_msg_py(interpreter
  "/home/jared/csws/src/interpreter/msg/i2c.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/interpreter
)

### Generating Services

### Generating Module File
_generate_module_py(interpreter
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/interpreter
  "${ALL_GEN_OUTPUT_FILES_py}"
)

add_custom_target(interpreter_generate_messages_py
  DEPENDS ${ALL_GEN_OUTPUT_FILES_py}
)
add_dependencies(interpreter_generate_messages interpreter_generate_messages_py)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/jared/csws/src/interpreter/msg/i2c.msg" NAME_WE)
add_dependencies(interpreter_generate_messages_py _interpreter_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(interpreter_genpy)
add_dependencies(interpreter_genpy interpreter_generate_messages_py)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS interpreter_generate_messages_py)



if(gencpp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/interpreter)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/interpreter
    DESTINATION ${gencpp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_cpp)
  add_dependencies(interpreter_generate_messages_cpp std_msgs_generate_messages_cpp)
endif()

if(geneus_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/interpreter)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/interpreter
    DESTINATION ${geneus_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_eus)
  add_dependencies(interpreter_generate_messages_eus std_msgs_generate_messages_eus)
endif()

if(genlisp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/interpreter)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/interpreter
    DESTINATION ${genlisp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_lisp)
  add_dependencies(interpreter_generate_messages_lisp std_msgs_generate_messages_lisp)
endif()

if(gennodejs_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/interpreter)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/interpreter
    DESTINATION ${gennodejs_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_nodejs)
  add_dependencies(interpreter_generate_messages_nodejs std_msgs_generate_messages_nodejs)
endif()

if(genpy_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/interpreter)
  install(CODE "execute_process(COMMAND \"/usr/bin/python2\" -m compileall \"${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/interpreter\")")
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/interpreter
    DESTINATION ${genpy_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_py)
  add_dependencies(interpreter_generate_messages_py std_msgs_generate_messages_py)
endif()
