from random import randint
from maya import cmds


def createLocator(name="locator", parent=None):
    sh = cmds.createNode("locator")
    xfo = cmds.listRelatives(sh, p=True)[0]
    xfo = cmds.rename(xfo, name)
    sh = cmds.listRelatives(xfo, s=True)
    if parent:
        print cmds.parent(xfo, parent)
    return xfo, sh


def ground(n, w=10, h=10):
    rval = list()
    group = cmds.createNode("transform")
    for _ in range(n):
        loc, _ = createLocator(parent=group)
        cmds.setAttr(loc + ".translateX", randint(-w/2.0, w/2.0))
        cmds.setAttr(loc + ".translateZ", randint(-h/2.0, h/2.0))
        rval.append(loc)
    return rval

ground(10)
