# PyTangoDemo
Based off:
- https://pytango.readthedocs.io/en/stable/howto.html
- https://tango-controls.readthedocs.io/en/latest/tutorials-and-howtos/how-tos/how-to-pytango.html

## Preconditions
- A running Tango system (TangoBox 9.3 used here) if you want to use the static database. Otherwise use --nodb argument.

## Procedure
- Register Tango Device on the Tango database (On first time)
- Run the associated Tango Device Server
- Execute the client

## Additional
- A device class has been made using native PyTango as well as with Pogo

## Open issues
- test_context (--test argument) seems to be a native PyTango way to execute a no database server but fails to execute a Pogo class (possibly due to python incompatibility 2.7 vs 3.7)
