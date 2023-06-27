'''Register a device on a Tango database'''

from __future__ import print_function
import tango

dev_info = tango.DbDevInfo()
dev_info.server = 'MyTestDevice/test'  # Device server instance name (Device factory)
dev_info._class = 'MyTestDevice'  # The device server must be named the same
dev_info.name = 'test/test_device/0'  # Device instance name

db = tango.Database()
db.add_device(dev_info)

print('Registered:', dev_info.name)
