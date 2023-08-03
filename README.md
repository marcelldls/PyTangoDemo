# PyTangoDemo
Based off:
- https://pytango.readthedocs.io/en/stable/howto.html
- https://tango-controls.readthedocs.io/en/latest/tutorials-and-howtos/how-tos/how-to-pytango.html

## Preconditions
- A running Tango system (TangoBox 9.3 virtual machine used here) if you want to use the static database. Otherwise use --nodb argument.

## Procedure to interact with a new device
- Register Tango Device on the Tango database (Needed on first time only - validate with "Jive" application)
- Run the associated Tango Device Server
- Execute the client

## Types of device classes
The following device classes are included:
- A native PyTango device
- A skeleton device made using Pogo
- A programatically built device class using PyTango framework has also been implemented (default).


Selection is done by removing the special characters in the config file.

## Open issues
- test_context (--test argument) seems to be a native PyTango way to execute a no database server but fails to execute a Pogo class (possibly due to python incompatibility 2.7 vs 3.7). Not yet clear why to use this over a --nodb option but I added it.
