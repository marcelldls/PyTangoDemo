import json


class config_parse():
    def __init__(self, path):
        with open(path, "r", encoding="utf-8") as config_file:
            config = json.load(config_file)
            self.cl_path = config["device_class_path"]
            self.cl_type = config["device_class_type"]
            self.dsr_name = config["device_server_name"]
            self.dev_name = config["device_name"]
            self.host = if_exists(config, "device_server_host", "127.0.0.1")
            self.port = if_exists(config, "device_server_port", 8888)
            self.dev_ptys = if_exists(config, "device_properties", {})
            self.cls_ptys = if_exists(config, "class_properties", {})


def if_exists(dict_, key, otherwise):
    if key in dict_:
        return dict_[key]
    else:
        return otherwise
