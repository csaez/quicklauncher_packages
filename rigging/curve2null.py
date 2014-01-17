from wishlib.si import si, sisel
from riglab.utils import curve2null

curve = sisel(0)
nulls = curve2null(curve)
# si.DeleteObj(curve)
si.SelectObj(nulls)
