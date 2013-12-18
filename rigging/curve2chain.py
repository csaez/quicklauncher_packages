from wishlib.si import si, sisel
from riglab.bonetools import curve2chain

sel = list(sisel)
curve = curve2chain(sel)
si.DeleteObj(sel)
si.SelectObj(curve)
