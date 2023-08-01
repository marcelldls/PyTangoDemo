"""Command line tool to start a Tango Device Server"""
from __future__ import print_function
from builtins import open
import argparse
import os
import json
import pickle
import pathlib

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
    cl_path = config["device_class_path"]
    dsr_name = config["device_server_name"]
    dev_name = config["device_name"]

# Start device server: Python <Server_file>.py <instance name>
if args.nodb:
    instance_name = ["test"]
    OPTNS = ["--nodb", "--dlist"]
    nodb_name = ["nodb/" + dev_name[dev_name.find("/") + 1:]]
    ADDR = ["--port", "8888"]
    print("Start no db device server with device:", *nodb_name)

    if pathlib.Path(cl_path).suffix == ".obj":
        with open(cl_path, 'rb') as filehandler:
            device_class = pickle.load(filehandler)
        device_class.run_server(instance_name + OPTNS + nodb_name + ADDR)

    else:
        cmnd = ["python", cl_path]
        os.system(" ".join(cmnd + instance_name + OPTNS + nodb_name + ADDR))

elif args.test:
    COMMAND = ["python", "-m", "tango.test_context"]
    class_name = cl_path[cl_path.find("/") + 1: cl_path.rfind(".")]
    python_path = [cl_path[: cl_path.find("/")] + 2 * ("." + class_name)]
    ADDRESS = ["--host", "127.0.0.1"]

    if pathlib.Path(cl_path).suffix == ".obj":
        raise NotImplementedError(".obj files not yet supported for --test")

    else:
        os.system(" ".join(COMMAND + python_path + ADDRESS))

else:
    cmnd = ["python", cl_path]
    instance_name = ["test"]
    print("Start device server")

    if pathlib.Path(cl_path).suffix == ".obj":
        raise NotImplementedError(".obj files not yet supported for --test")

    else:
        os.system(" ".join(cmnd + instance_name))
