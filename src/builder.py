from tango import server


def device_class_builder(device_type=None,
                         attributes=None,
                         commands=None,
                         properties=None):

    print("Dynamically building device class...")

    class_body = {}
    for attr in attributes:
        class_body[attr] = server.attribute(
            attributes[attr]["method"],
            dtype=attributes[attr]["dtype"],
            )
    print("Processed attributes")

    for cmnd in commands:
        class_body[cmnd] = server.command(
            commands[cmnd],
            )
    print("Processed commands")

    print("Skipped properties")

    dynamic_class = type(device_type, (server.Device,), class_body)

    return dynamic_class
