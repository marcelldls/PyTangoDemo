import pickle
from src.builder import device_class_builder
from src.util import spin

attributes = {
    "remember_bool": {
        "attribute_type": "Read/Write",
        "data_type": "Bool",
        "data_format": "Scalar",
        },
    "remember_float": {
        "attribute_type": "Read/Write",
        "data_type": "Float",
        "data_format": "Scalar",
        },
}

commands = {
    "spin": spin,
}

properties = {
}

dev_config = {
    "attributes": attributes,
    "commands": commands,
    "properties": properties,
}

my_dev_class = device_class_builder(**dev_config)


# Solve -> AttributeError: Can't pickle local object 'add_attributes.<locals>.dynamic_class'
"""
with open('tango_classes/BuildTestDevice.obj', 'wb') as filehandler:
    pickle.dump(my_dev_class, filehandler)
    print("Sucessfully stored device class")
"""

#####  delete everythinh below before merge #####
"""
with open("tango_classes/BuildTestDevice.obj", 'rb') as filehandler:
    device_class = pickle.load(filehandler)
"""

my_dev_class.run_server(['test', '--nodb', '--dlist', 'nodb/test_device/0', '--port', '8888'])
