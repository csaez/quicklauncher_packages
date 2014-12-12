from contextlib import contextmanager
from maya import cmds


@contextmanager
def one_undo():
    cmds.undoInfo(openChunk=True)
    yield
    cmds.undoInfo(closeChunk=True)


def align(node, target):
    for cns_type in ("parent", "scale"):
        cns = getattr(cmds, cns_type + "Constraint")(target, each)
        cmds.delete(cns)

with one_undo():
    selection = cmds.ls(sl=True)
    target = selection[-1]
    for each in selection[:-1]:
        align(each, target)
