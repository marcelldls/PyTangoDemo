"""Command line tool to start a Tango Device Server"""
from __future__ import print_function
from builtins import open
import argparse
import os
import json

# Process command line arguments
parser = argparse.ArgumentParser(
                            description="Starts a Tango Device Server"
                            )
parser.add_argument("--nodb",
                help="Run device server without a database",
                action="store_true"
                )
args = parser.parse_args()

# Process config file
with open("config.json", "r", encoding="utf-8") as config_file:
    config = json.load(config_file)
    cl_path = config["device_class_path"]
    dsr_name = config["device_server_name"]
    dev_name = config["device_name"]

# Start device server: python <Server_file>.py <instance name>
COMMAND = "python " + cl_path + " test"
if args.nodb:
    nodb_name = "nodb/" + dev_name[dev_name.find('/')+1:]
    print("Start no db device server with device:", nodb_name)
    os.system(COMMAND + " --nodb --dlist " + nodb_name + " --port 8888")
elif ~args.nodb:
    print("Start device server")
    os.system(COMMAND)
