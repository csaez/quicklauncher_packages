from wishlib.si import si, sisel
from riglab.utils import curve2chain

curve = sisel(0)
chain = curve2chain(curve)
# si.DeleteObj(sel)
si.SelectObj(curve)
