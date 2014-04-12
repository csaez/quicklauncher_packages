import pymel.core as pm

defaults = {"translate": [0, 0, 0],
            "rotate": [0, 0, 0],
            "scale": [1, 1, 1]}

for x in pm.ls(sl=True, type="transform"):
    for k, v in defaults.iteritems():
        getattr(x, k).set(v)
