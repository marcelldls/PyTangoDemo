'''Command line tool to start a Tango Device Server'''

import argparse
import os

parser = argparse.ArgumentParser(
                            description='Starts a Tango Device Server'
                            )
parser.add_argument('--nodb',
                help='Run device server without a database',
                action='store_true'
                )
args = parser.parse_args()

if args.nodb:
    os.system('echo nodb')
    os.system('python <server_file>.py <instance_name> -nodb -port 10000')
elif ~args.nodb:
    os.system('echo db')
    os.system('python <server_file>.py <instance_name>')
