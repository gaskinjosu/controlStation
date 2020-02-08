import os
import rospy
import rospkg

from geometry_msgs.msg import Twist
from std_msgs.msg import Int32
from qt_gui.plugin import Plugin
from python_qt_binding import loadUi
from python_qt_binding.QtWidgets import QWidget

class MyPlugin(Plugin):

    def __init__(self, context):
        super(MyPlugin, self).__init__(context)
        # Give QObjects reasonable names
        self.setObjectName('MyPlugin')

        # Process standalone plugin command-line arguments
        from argparse import ArgumentParser
        parser = ArgumentParser()
        # Add argument(s) to the parser.
        parser.add_argument("-q", "--quiet", action="store_true",
                      dest="quiet",
                      help="Put plugin in silent mode")
        args, unknowns = parser.parse_known_args(context.argv())
        if not args.quiet:
            print 'arguments: ', args
            print 'unknowns: ', unknowns

        # Create QWidget
        self._widget = QWidget()
        # Get path to UI file which should be in the "resource" folder of this package
        ui_file = os.path.join(rospkg.RosPack().get_path('rov_teleop'), 'resource', 'MyPlugin.ui')
        # Extend the widget with all attributes and children from UI file
        loadUi(ui_file, self._widget)
        # Give QObjects reasonable names
        self._widget.setObjectName('MyPluginUi')
        # Show _widget.windowTitle on left-top of each plugin (when 
        # it's set in _widget). This is useful when you open multiple 
        # plugins at once. Also if you open multiple instances of your 
        # plugin at once, these lines add number to make it easy to 
        # tell from pane to pane.
        if context.serial_number() > 1:
            self._widget.setWindowTitle(self._widget.windowTitle() + (' (%d)' % context.serial_number()))
        # Add widget to the user interface
        context.add_widget(self._widget)


	#AMENDED PART
	
	#publisher dictionary	
	self.publisher_dict = {}
	#connection initilization
	self.init_signals()
	#publisher initialization
	self.init_ros()


	#Set up variables to hold twist messages:
	self.xlin = 0.0
	self.ylin = 0.0
	self.zlin = 0.0
	self.xang = 0.0
	self.yang = 0.0
	self.zang = 0.0

	self.autostate = -1

	#set default velocity
	self.velocity = 0
	self.upper_velocity_limit = 100.0
	self.update_velocity(0.0)


	#FUNCTIONS:

    def update_velocity(self, vel):
	'''
	sets veloctiy and updates slider and velocity text fields
	'''

	self.velocity = vel
	self._widget.velocity_display.setText( str(vel) )
	self._widget.velocitySlider.setValue(vel)
	self.sendTwist()
	

    def init_signals(self):	
	'''
	connects all necessary signals from GUI
	'''
	self._widget.button_halt.toggled.connect(self.halt_checked)
	self._widget.button_verthalt.toggled.connect(self.verthalt_checked)
	self._widget.button_turnhalt.toggled.connect(self.turnhalt_checked)	

	self._widget.button_forward.toggled.connect(self.forward_checked)
	self._widget.button_forwardleft.toggled.connect(self.forwardleft_checked)
	self._widget.button_forwardright.toggled.connect(self.forwardright_checked)

	self._widget.button_backward.toggled.connect(self.backward_checked)
	self._widget.button_backwardleft.toggled.connect(self.backwardleft_checked)
	self._widget.button_backwardright.toggled.connect(self.backwardright_checked)

	self._widget.button_left.toggled.connect(self.left_checked)
	self._widget.button_right.toggled.connect(self.right_checked)

	self._widget.button_turnleft.toggled.connect(self.turnleft_checked)
	self._widget.button_turnright.toggled.connect(self.turnright_checked)
	
	self._widget.button_up.toggled.connect(self.up_checked)
	self._widget.button_down.toggled.connect(self.down_checked)

	self._widget.button_auto.toggled.connect(self.auto_checked)

	self._widget.velocitySlider.valueChanged.connect(self.slider_activity)

	#self._widget.velocity_display.textEdited.connect(self.velocity_edited)




    def init_ros(self):
	'''
	Method initializes ROS interaction
	'''
	try:
	    self.publisher_dict['movement'] = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
            self.publisher_dict['auto'] = rospy.Publisher('/auto_status', Int32, queue_size=1)

	except rospy.ROSException as e:
	    QMessageBox.about(self._widget, "ROS error", e.message)


    def keyPressEvent(self, event):
	if type(event) == QtGui.QKeyEvent:
	    print event.key()
	    event.accept()
	else:
	    event.ignore()

    #NOTE: need to set buttons to auto-repeat so that velocity values will be updated as slider is changed...
    
    def halt_checked(self):
	if(self._widget.button_halt.isChecked()):
	    self.xlin = 0
	    self.ylin = 0	
	self.sendTwist()

    def verthalt_checked(self):
	if(self._widget.button_verthalt.isChecked()):
	    self.zlin = 0	
	self.sendTwist()


    def turnhalt_checked(self):
	if(self._widget.button_turnhalt.isChecked()):	
	    self.sendTwist()



    #Movement in the "XY" Plane
    def forward_checked(self):
	if(self._widget.button_forward.isChecked()):
	    self.xlin = 1
	    self.ylin = 0
	else:
	    self.xlin = 0	
	self.sendTwist()

    def backward_checked(self):
	if(self._widget.button_backward.isChecked()):
	    self.xlin = -1
	    self.ylin = 0
	else:
	    self.xlin = 0
    	self.sendTwist()

    def left_checked(self):
	if(self._widget.button_left.isChecked()):
	    self.xlin = 0
	    self.ylin = -1
	else:
	    self.ylin = 0
	self.sendTwist()

    def right_checked(self):
	if(self._widget.button_right.isChecked()):
	    self.xlin = 0
	    self.ylin = 1
	else:
	    self.ylin = 0
	self.sendTwist()

#TODO

    def forwardleft_checked(self):
	if(self._widget.button_forwardleft.isChecked()):
	    self.xlin = 0
	    self.ylin = 0
	    self.sendTwist()

    def forwardright_checked(self):
	if(self._widget.button_forwardright.isChecked()):
	    self.xlin = 0
	    self.ylin = 0
	    self.sendTwist()


    def backwardleft_checked(self):
	if(self._widget.button_backwardleft.isChecked()):
	    self.xlin = 0
	    self.ylin = 0
	    self.sendTwist()


    def backwardright_checked(self):
	if(self._widget.button_backwardright.isChecked()):
	    self.xlin = 0
	    self.ylin = 0
	    self.sendTwist()
#END TODO

    def up_checked(self):
	if(self._widget.button_up.isChecked()):
	    self.zlin = 1
	else:
	    self.zlin = 0
	self.sendTwist()

    def down_checked(self):
	if(self._widget.button_down.isChecked()):
	    self.zlin = -1
	else:
	    self.zlin = 0
	self.sendTwist()

#TODO
    def turnleft_checked(self):
	if(self._widget.button_turnleft.isChecked()):
	    self.zlin = 0
	    self.sendTwist()

    def turnright_checked(self):
	if(self._widget.button_turnright.isChecked()):
	    self.zlin = 0
	    self.sendTwist()
#END TODO

    def auto_checked(self):
	self.autostate = -self.autostate
	self.publisher_dict['auto'].publish(self.autostate)

    def slider_activity(self):
	self.update_velocity( self._widget.velocitySlider.value())

    def sendTwist(self):
	self.twist = Twist()
	self.twist.linear.x = self.xlin * self.velocity
	self.twist.linear.y = self.ylin * self.velocity
	self.twist.linear.z = self.zlin * self.velocity
	self.twist.angular.x = self.xang
	self.twist.angular.y = self.yang
	self.twist.angular.z = self.zang
	
	self.publisher_dict['movement'].publish(self.twist)

    def shutdown_plugin(self):
        # TODO unregister all publishers here
        pass

    def save_settings(self, plugin_settings, instance_settings):
        # TODO save intrinsic configuration, usually using:
        # instance_settings.set_value(k, v)
        pass

    def restore_settings(self, plugin_settings, instance_settings):
        # TODO restore intrinsic configuration, usually using:
        # v = instance_settings.value(k)
        pass

    #def trigger_configuration(self):
        # Comment in to signal that the plugin has a way to configure
        # This will enable a setting button (gear icon) in each dock widget title bar
        # Usually used to open a modal configuration dialog

