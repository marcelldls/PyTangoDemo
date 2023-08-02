from tango import server


def device_class_builder(device_type=None,
                         attributes=None,
                         commands=None,
                         properties=None):

    print("Dynamically building device class...")

    class dynamic_class(server.Device):

        for attr in attributes:
            locals()[attr] = server.attribute(
                attributes[attr]["method"],
                dtype=attributes[attr]["dtype"]
                )
        print("Added attributes")

        for cmnd in commands:
            locals()[cmnd] = server.command(
                commands[cmnd],
                )
        print("Added commands")

        print("Skipped properties")

    dynamic_class.__name__ = device_type

    return dynamic_class
