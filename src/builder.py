from tango import server, DevState


def device_class_builder(device_type=None,
                         attributes=None,
                         commands=None,
                         properties=None,
                         init_method=None):

    class_body = {}
    print("Dynamically building device class...")

    for attr in attributes:
        class_body[attr] = server.attribute(
            **attributes[attr]
            )
    print("Processed attributes")

    for cmnd in commands:
        class_body[cmnd] = server.command(
            commands[cmnd],
            )
    print("Processed commands")

    for pty in properties:
        class_body[pty] = server.device_property(
            **properties[pty],
            )
    print("Processed properties")

    class_body["init_device"] = init_device
    if init_method is None:
        class_body["init_method"] = lambda *args: None
    else:
        class_body["init_method"] = init_method["init_device"]
    print("Processed device initialisation")

    dynamic_class = type(device_type, (server.Device,), class_body)
    print("Created device class:", dynamic_class.__name__)

    return dynamic_class


def init_device(self):
    server.Device.init_device(self)
    self.init_method()
