# PyTangoDemo
Based off:
- https://pytango.readthedocs.io/en/stable/howto.html
- https://tango-controls.readthedocs.io/en/latest/tutorials-and-howtos/how-tos/how-to-pytango.html

## Procedure to interact with a new device
- Create a new Tango control system by running `podman-compose up'
- Register Tango Device on the Tango database (Needed on first time only)
- Run the associated Tango Device Server
- Execute the client

### Troubleshooting
Interaction with the database can be validated using the containerised Jive GUI application 
```
docker pull andygotz/tango-jive:7.19
docker run -ti --rm -e DISPLAY=$DISPLAY -e TANGO_HOST=$TANGO_HOST -v /tmp/.X11-unix:/tmp/.X11-unix --net=host andygotz/tango-jive:7.19
```

## Types of device classes
The following device classes are included:
- A native PyTango device
- A skeleton device made using Pogo
- A programatically built device class using PyTango framework has also been implemented (default).

Selection is done by removing the special characters in the config file.

## Open issues
- test_context (--test argument) seems to be a native PyTango way to execute a no database server but fails to execute a Pogo class (possibly due to python incompatibility 2.7 vs 3.7). Not yet clear why to use this over a --nodb option but I added it.
