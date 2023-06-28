"""Exploring PyTango"""
from __future__ import print_function
from builtins import open
import argparse
import json
import socket
import tango

parser = argparse.ArgumentParser(
                            description="Run a Tango Client"
                            )
parser.add_argument("--nodb",
                help="Connect to a device server without a database",
                action="store_true"
                )
args = parser.parse_args()

with open("config.json", "r", encoding="utf-8") as config_file:
    config = json.load(config_file)
    cl_path = config["device_class_path"]
    dsr_name = config["device_server_name"]
    dev_name = config["device_name"]

if args.nodb:
    hostname = socket.gethostname() + ":10000/"
    nodb_name = "nodb/" + dev_name[dev_name.find('/')+1:]
    dev_name = hostname + nodb_name + "#dbase=no"

print(tango.__version__)
print(tango.ApiUtil.get_env_var("TANGO_HOST"))

test_device = tango.DeviceProxy(dev_name)
print("Ping device:", test_device.ping(), "us")
