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

if args.test:
    class_name = re.findall("/(.*).py", cnfg.cl_path)[0]
    python_path = [re.findall("(.*)/", cnfg.cl_path)[0] + 2*f".{class_name}"]
    optn = []

    if cnfg.cl_type in ["BuildClass", "PogoClass"]:
        msg = f"{cnfg.cl_type} not yet supported for 'test'"
        raise NotImplementedError(msg)

    else:
        cmnd = ["python", "-m", "tango.test_context"]
        os.system(" ".join(cmnd + python_path + srvr_addr))

else:
    if args.nodb:
        print("Starting device:",
              f"tango://{cnfg.host}:{cnfg.port}/{cnfg.dev_name}#dbase=no")
        optn = ["--nodb", "--dlist", cnfg.dev_name]

    else:
        print("Starting device:",
              f"tango://{cnfg.host}:{cnfg.port}/{cnfg.dsr_name}/{cnfg.dev_name}")
        optn = []

    if cnfg.cl_type == "BuildClass":
        file_loc = re.findall("(.*).py", cnfg.cl_path)[0].replace("/", ".")
        dev_config = getattr(importlib.import_module(file_loc), "dev_config")
        class_name = re.findall("/(.*).py", cnfg.cl_path)[0]
        dev_config['device_type'] = class_name
        device_class = device_class_builder(**dev_config)
        server_args = [class_name] + srvr_instance + optn + srvr_addr
        run((device_class,), server_args)

    elif cnfg.cl_type == "PyTangoClass":
        cls_dt_pth = re.findall("(.*).py", cnfg.cl_path)[0].replace("/", ".")
        class_name = re.findall("/(.*).py", cnfg.cl_path)[0]
        device_class = getattr(importlib.import_module(cls_dt_pth), class_name)
        server_args = [class_name] + srvr_instance + optn + srvr_addr
        run((device_class,), server_args)

    elif cnfg.cl_type == "PogoClass":
        cmnd = ["python", cnfg.cl_path]
        server_args = srvr_instance + optn + srvr_addr
        os.system(" ".join(cmnd + server_args))

    else:
        msg = "Unrecognised Tango device implementation"
        raise NotImplementedError(msg)
