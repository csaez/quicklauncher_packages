from wishlib.si import si, sisel
from riglab.utils import curve2chain

sel = list(sisel)
curve = curve2chain(sel)
si.DeleteObj(sel)
si.SelectObj(curve)
