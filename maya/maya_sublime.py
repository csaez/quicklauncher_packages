from maya import cmds

# if it was already open under another configuration
cmds.commandPort(name="127.0.0.1:7002", close=True)

# now open a new port
cmds.commandPort(name="127.0.0.1:7002", sourceType="python")

# or open some random MEL port (make sure you change it to this port in
# your config file)
cmds.commandPort(name="127.0.0.1:10000", sourceType="mel")
