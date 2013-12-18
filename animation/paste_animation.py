from difflib import SequenceMatcher
from wishlib.si import si, sisel
import quicklauncher


ratio = lambda x, y: SequenceMatcher(None, x, y). ratio()
target = sisel.GetAsText().split(",")
if hasattr(quicklauncher, "copy_from"):
    for x in quicklauncher.copy_from:
        si.CopyAllAnimation2(x, "siFCurveSource", "siAllParam")
        closest = sorted(target, key=lambda t: ratio(x.FullName, t))[-1]
        si.PasteAllAnimation(closest)
