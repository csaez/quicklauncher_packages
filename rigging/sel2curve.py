from wishlib.si import si, sisel
from riglab.bonetools import sel2curve

sel = list(sisel)
curve = sel2curve(sel)
si.DeleteObj(sel)
si.SelectObj(curve)
