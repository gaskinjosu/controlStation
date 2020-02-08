#!/usr/bin/env python2

import sys

from rov_teleop.my_module import MyPlugin
from rqt_gui.main import Main
'''
Starts the rqt plugin

run with command:
$ rqt --standalone rov_teleop

'''

plugin = 'rov_teleop'
main = Main(filename=plugin)
sys.exit(main.main(standalone=plugin))
