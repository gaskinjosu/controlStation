#!/bin/sh

if [ -n "$DESTDIR" ] ; then
    case $DESTDIR in
        /*) # ok
            ;;
        *)
            /bin/echo "DESTDIR argument must be absolute... "
            /bin/echo "otherwise python's distutils will bork things."
            exit 1
    esac
    DESTDIR_ARG="--root=$DESTDIR"
fi

echo_and_run() { echo "+ $@" ; "$@" ; }

echo_and_run cd "/home/jared/csws/src/rov_teleop"

# ensure that Python install destination exists
echo_and_run mkdir -p "$DESTDIR/home/jared/csws/install/lib/python2.7/dist-packages"

# Note that PYTHONPATH is pulled from the environment to support installing
# into one location when some dependencies were installed in another
# location, #123.
echo_and_run /usr/bin/env \
    PYTHONPATH="/home/jared/csws/install/lib/python2.7/dist-packages:/home/jared/csws/build/lib/python2.7/dist-packages:$PYTHONPATH" \
    CATKIN_BINARY_DIR="/home/jared/csws/build" \
    "/usr/bin/python2" \
    "/home/jared/csws/src/rov_teleop/setup.py" \
    build --build-base "/home/jared/csws/build/rov_teleop" \
    install \
    $DESTDIR_ARG \
    --install-layout=deb --prefix="/home/jared/csws/install" --install-scripts="/home/jared/csws/install/bin"
