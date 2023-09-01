import json


class config_parse():
    def __init__(self, path):
        with open(path, "r", encoding="utf-8") as config_file:
            config = json.load(config_file)
            self.host = config["host"]
            self.port = config["port"]
            self.cl_path = config["device_class_path"]
            self.cl_type = config["device_class_type"]
            self.dsr_name = config["device_server_name"]
            self.dev_name = config["device_name"]
            self.dev_ptys = config["device_properties"]
            self.cls_ptys = config["class_properties"]