def open_port(port):
    from maya import cmds
    # close port
    try:
        # if it was already open under another configuration
        cmds.commandPort(name=port, close=True)
    except RuntimeError:
        pass
    cmds.commandPort(name=port, sourceType="python")
    # cmds.commandPort(name=":10000", sourceType="mel")

open_port("127.0.0.1:7002")
