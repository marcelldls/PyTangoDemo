from tango.server import Device


def device_class_builder(attributes=None,
                         commands=None,
                         properties=None):

    print("Create device class")
    device_class = Device
    add_attributes(device_class, attributes)
    add_commands(device_class, attributes)
    add_properties(device_class, attributes)

    return device_class


def add_attributes(device, attributes):
    pass


"""
setattr(Foo, 'print_v', my_new_method)
    @attribute(dtype=float)
    def voltage(self):
        return 1.23
"""


def add_commands(device, commands):
    pass


def add_properties(device, properties):
    pass
