"""Command line tool to start a Tango Device Server"""
from __future__ import print_function
from builtins import open
import argparse
import os
import json
from src.builder import device_class_builder


# Process command line arguments
parser = argparse.ArgumentParser(description="Starts a Tango Device Server")
parser.add_argument(
    "--nodb", help="Run device server without a database", action="store_true"
)
parser.add_argument(
    "--test", help="Run test device server (no database)", action="store_true"
)
args = parser.parse_args()

# Process config file
with open("config/config.json", "r", encoding="utf-8") as config_file:
    config = json.load(config_file)
    host = config["host"]
    port = config["port"]
    dsr_name = config["device_server_name"]
    dev_name = config["device_name"]
    cl_path = config["device_class_path"]
    cl_type = config["device_class_type"]

srvr_instance = [dsr_name[dsr_name.rfind("/")+1:]]
srvr_addr = ["--host", host, "--port", port]

if args.nodb:
    optn = ["--nodb", "--dlist", dev_name]

    print("Start no db device server:", dsr_name)
    print("Include device:", dev_name)

    if cl_type == "BuildClass":
        file_loc = cl_path[:cl_path.rfind(".")].replace("/", ".")
        exec("from %s import dev_config" % file_loc)
        class_name = cl_path[cl_path.find("/") + 1: cl_path.rfind(".")]
        dev_config['device_type'] = class_name
        device_class = device_class_builder(**dev_config)
        device_class.run_server(srvr_instance + optn + srvr_addr)

    else:
        cmnd = ["python", cl_path]
        os.system(" ".join(cmnd + srvr_instance + optn + srvr_addr))

elif args.test:
    class_name = cl_path[cl_path.find("/") + 1: cl_path.rfind(".")]
    python_path = [cl_path[: cl_path.find("/")] + 2 * ("." + class_name)]

    if cl_type == "BuildClass":
        raise NotImplementedError("Dynamically built classes not yet supported here")

    else:
        cmnd = ["python", "-m", "tango.test_context"]
        os.system(" ".join(cmnd + python_path + srvr_addr))

else:
    # Start device server: Python <Server_file>.py <server instance name>
    print("Start device server")

    if cl_type == "BuildClass":
        file_loc = cl_path[:cl_path.rfind(".")].replace("/", ".")
        exec("from %s import dev_config" % file_loc)
        class_name = cl_path[cl_path.find("/") + 1: cl_path.rfind(".")]
        dev_config['device_type'] = class_name
        device_class = device_class_builder(**dev_config)
        device_class.run_server(srvr_instance + srvr_addr)

    else:
        cmnd = ["python", cl_path]
        os.system(" ".join(cmnd + srvr_instance + srvr_addr))
