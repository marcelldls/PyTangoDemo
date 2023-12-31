#!/usr/bin/env python
# -*- coding:utf-8 -*-


# ############################################################################
#  license :
# ============================================================================
#
#  File :        PogoTestDevice.py
#
#  Project :     PyTango
#
# This file is part of Tango device class.
# 
# Tango is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# Tango is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with Tango.  If not, see <http://www.gnu.org/licenses/>.
# 
#
#  $Author :      marcell.nagy$
#
#  $Revision :    $
#
#  $Date :        $
#
#  $HeadUrl :     $
# ============================================================================
#            This file is generated by POGO
#     (Program Obviously used to Generate tango Object)
# ############################################################################

__all__ = ["PogoTestDevice", "PogoTestDeviceClass", "main"]

__docformat__ = 'restructuredtext'

import PyTango
import sys
# Add additional import
#----- PROTECTED REGION ID(PogoTestDevice.additionnal_import) ENABLED START -----#

#----- PROTECTED REGION END -----#	//	PogoTestDevice.additionnal_import

# Device States Description
# No states for this device


class PogoTestDevice (PyTango.Device_4Impl):
    """A Test Device used for evaluating Pogo"""
    
    # -------- Add you global variables here --------------------------
    #----- PROTECTED REGION ID(PogoTestDevice.global_variables) ENABLED START -----#
    
    #----- PROTECTED REGION END -----#	//	PogoTestDevice.global_variables

    def __init__(self, cl, name):
        PyTango.Device_4Impl.__init__(self,cl,name)
        self.debug_stream("In __init__()")
        PogoTestDevice.init_device(self)
        #----- PROTECTED REGION ID(PogoTestDevice.__init__) ENABLED START -----#
        
        #----- PROTECTED REGION END -----#	//	PogoTestDevice.__init__
        
    def delete_device(self):
        self.debug_stream("In delete_device()")
        #----- PROTECTED REGION ID(PogoTestDevice.delete_device) ENABLED START -----#
        
        #----- PROTECTED REGION END -----#	//	PogoTestDevice.delete_device

    def init_device(self):
        self.debug_stream("In init_device()")
        self.get_device_properties(self.get_device_class())
        #----- PROTECTED REGION ID(PogoTestDevice.init_device) ENABLED START -----#
        
        #----- PROTECTED REGION END -----#	//	PogoTestDevice.init_device

    def always_executed_hook(self):
        self.debug_stream("In always_excuted_hook()")
        #----- PROTECTED REGION ID(PogoTestDevice.always_executed_hook) ENABLED START -----#
        
        #----- PROTECTED REGION END -----#	//	PogoTestDevice.always_executed_hook

    # -------------------------------------------------------------------------
    #    PogoTestDevice read/write attribute methods
    # -------------------------------------------------------------------------
    
    
    
            
    def read_attr_hardware(self, data):
        self.debug_stream("In read_attr_hardware()")
        #----- PROTECTED REGION ID(PogoTestDevice.read_attr_hardware) ENABLED START -----#
        
        #----- PROTECTED REGION END -----#	//	PogoTestDevice.read_attr_hardware


    # -------------------------------------------------------------------------
    #    PogoTestDevice command methods
    # -------------------------------------------------------------------------
    

    #----- PROTECTED REGION ID(PogoTestDevice.programmer_methods) ENABLED START -----#
    
    #----- PROTECTED REGION END -----#	//	PogoTestDevice.programmer_methods

class PogoTestDeviceClass(PyTango.DeviceClass):
    # -------- Add you global class variables here --------------------------
    #----- PROTECTED REGION ID(PogoTestDevice.global_class_variables) ENABLED START -----#
    
    #----- PROTECTED REGION END -----#	//	PogoTestDevice.global_class_variables


    #    Class Properties
    class_property_list = {
        }


    #    Device Properties
    device_property_list = {
        }


    #    Command definitions
    cmd_list = {
        }


    #    Attribute definitions
    attr_list = {
        }


def main():
    try:
        py = PyTango.Util(sys.argv)
        py.add_class(PogoTestDeviceClass, PogoTestDevice, 'PogoTestDevice')
        #----- PROTECTED REGION ID(PogoTestDevice.add_classes) ENABLED START -----#
        
        #----- PROTECTED REGION END -----#	//	PogoTestDevice.add_classes

        U = PyTango.Util.instance()
        U.server_init()
        U.server_run()

    except PyTango.DevFailed as e:
        print ('-------> Received a DevFailed exception:', e)
    except Exception as e:
        print ('-------> An unforeseen exception occured....', e)

if __name__ == '__main__':
    main()
