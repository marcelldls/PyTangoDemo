"""Command line tool to start a Tango Device Server"""
import argparse
import os
import importlib
from src.builder import device_class_builder
from src.utils import config_parse
from tango.server import run
import re

# Process command line arguments
parser = argparse.ArgumentParser(description="Starts a Tango Device Server")
parser.add_argument(
    "deviceConfig",
    help="Specify a device configuration",
)
parser.add_argument(
    "--nodb", help="Run device server without a database", action="store_true"
)
parser.add_argument(
    "--test", help="Run test device server (no database)", action="store_true"
)
args = parser.parse_args()
cnfg = config_parse(args.deviceConfig)

srvr_instance = re.findall("/(.*)", cnfg.dsr_name)
srvr_addr = ["--host", cnfg.host, "--port", str(cnfg.port)]

if args.nodb:
    print("Starting device:",
          f"tango://{cnfg.host}:{cnfg.port}/{cnfg.dev_name}#dbase=no")
    optn = ["--nodb", "--dlist", cnfg.dev_name]

    if cnfg.cl_type == "BuildClass":
        file_loc = re.findall("(.*).py", cnfg.cl_path)[0].replace("/", ".")
        dev_config = getattr(importlib.import_module(file_loc), "dev_config")
        class_name = re.findall("/(.*).py", cnfg.cl_path)[0]
        dev_config['device_type'] = class_name
        device_class = device_class_builder(**dev_config)
        run((device_class,), [class_name]+srvr_instance+optn+srvr_addr)

    else:
        cmnd = ["python", cnfg.cl_path]
        os.system(" ".join(cmnd + srvr_instance + optn + srvr_addr))

elif args.test:
    class_name = re.findall("/(.*).py", cnfg.cl_path)[0]
    python_path = [re.findall("(.*)/", cnfg.cl_path)[0] + 2*f".{class_name}"]

    if cnfg.cl_type == "BuildClass":
        msg = "Dynamically built classes not yet supported here"
        raise NotImplementedError(msg)

    if cnfg.cl_type == "PogoClass":
        msg = "Pogo devices not yet supported (Python 2 dependancy)"
        raise NotImplementedError(msg)

    else:
        cmnd = ["python", "-m", "tango.test_context"]
        os.system(" ".join(cmnd + python_path + srvr_addr))

else:
    # Start device server: Python <Server_file>.py <server instance name>
    print("Starting device:",
          f"tango://{cnfg.host}:{cnfg.port}/{cnfg.dsr_name}/{cnfg.dev_name}")

    if cnfg.cl_type == "BuildClass":
        file_loc = re.findall("(.*).py", cnfg.cl_path)[0].replace("/", ".")
        dev_config = getattr(importlib.import_module(file_loc), "dev_config")
        class_name = re.findall("/(.*).py", cnfg.cl_path)[0]
        dev_config['device_type'] = class_name
        device_class = device_class_builder(**dev_config)
        run((device_class,), [class_name]+srvr_instance+srvr_addr)

    else:
        cmnd = ["python", cnfg.cl_path]
        os.system(" ".join(cmnd + srvr_instance + srvr_addr))
