# PyTangoDemo
Based off:
- https://pytango.readthedocs.io/en/stable/howto.html
- https://tango-controls.readthedocs.io/en/latest/tutorials-and-howtos/how-tos/how-to-pytango.html

## Creating and interact with a device
- Have a running a Tango control system (vscode task: `local_tangocs`)
- Register Tango Device on the Tango database (This only has to be done once)
- Run the associated Tango Device Server
- Execute the client

Some ways to interact with a device
- Use the `itango` task to start an interactive Tango terminal
- Use the vscode launch configuration `Local TangoCS: Current File` to interact via scripts or `export TANGO_HOST=localhost:10000`

### Troubleshooting
Interaction with the database can be validated using the containerised Jive GUI application 
```
podman pull andygotz/tango-jive:7.19
podman run -ti --rm -e DISPLAY=$DISPLAY -e TANGO_HOST=localhost:10000 -v /tmp/.X11-unix:/tmp/.X11-unix --security-opt label=type:container_runtime_t --net=host andygotz/tango-jive:7.19
```
You may need to run `xhost +local:podman`

## Types of device classes
The following device classes are included:
- A native PyTango test device
- A skeleton test device made using Pogo
- A programatically built test device class using PyTango framework has also been implemented.
- A temperature controller to interact with a simulated device which can be started with the vscode launch configuration `Debug temp controller` (default)

Selection is done by specifying the config file.

## Open issues
- test_context (--test argument) seems to be a native PyTango way to execute a no database server but fails to execute a Pogo class (possibly due to python incompatibility 2 vs 3). Not yet clear why to use this over a --nodb option but I added it.
