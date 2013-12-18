from wishlib.si import si, sisel
from riglab.bonetools import chain2curve

sel = list(sisel)
curve = chain2curve(sel)
si.DeleteObj(sel)
si.SelectObj(curve)
