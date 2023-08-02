from tango import server


def device_class_builder(attributes=None,
                         commands=None,
                         properties=None):

    print("Dynamically building device class...")
    device_class = add_attributes(server.Device, attributes)
    device_class = add_commands(device_class, commands)
    device_class = add_properties(device_class, properties)

    return device_class


def add_attributes(device, attributes):

    class dynamic_class(device):

        for attr in attributes:
            locals()[attr] = server.attribute(
                attributes[attr]["method"],
                dtype=attributes[attr]["dtype"]
                )

    print("Added attributes")

    return dynamic_class


def add_commands(device, commands):

    class dynamic_class(device):

        for cmnd in commands:
            locals()[cmnd] = server.command(
                commands[cmnd],
                )

    print("Added commands")
    return dynamic_class


def add_properties(device, properties):
    print("Added properties")
    return device
