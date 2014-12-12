from contextlib import contextmanager
from maya import cmds


@contextmanager
def one_undo():
    cmds.undoInfo(openChunk=True)
    yield
    cmds.undoInfo(closeChunk=True)


def reset(node):
    DEFAULTS = {"translate": [0, 0, 0],
                "rotate": [0, 0, 0],
                "scale": [1, 1, 1]}
    for k, v in DEFAULTS.iteritems():
        for i, axis in enumerate("XYZ"):
            cmds.setAttr(node + "." + k + axis, v[i])

with one_undo():
    for node in cmds.ls(sl=True, type="transform"):
        reset(node)
