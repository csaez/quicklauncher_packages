def align():
    from pymel import core as pm
    sel = pm.ls(sl=True)
    xfo = sel[-1].getMatrix(worldSpace=True)
    for x in sel[:-1]:
        x.setMatrix(xfo, worldSpace=True)

align()
