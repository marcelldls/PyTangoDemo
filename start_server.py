"""Command line tool to start a Tango Device Server"""

import argparse
import os

parser = argparse.ArgumentParser(
                            description="Starts a Tango Device Server"
                            )
parser.add_argument("--nodb",
                help="Run device server without a database",
                action="store_true"
                )
args = parser.parse_args()

# Start device server: python <Server_file>.py <instance name>
COMMAND = "python tango_classes/PogoTestDevice.py test"
if args.nodb:
    print("Start device server without database")
    os.system(COMMAND + " --nodb --dlist nodb/test_device/0 --port 10000")
elif ~args.nodb:
    print("Start device server")
    os.system(COMMAND)
