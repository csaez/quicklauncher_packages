from difflib import SequenceMatcher
import quicklauncher


ratio = lambda x, y: SequenceMatcher(None, x, y). ratio()
target = Application.Selection.GetAsText().split(",")
if hasattr(quicklauncher, "copy_anim_from"):
    for x in quicklauncher.copy_anim_from:
        Application.CopyAllAnimation2(x, "siFCurveSource", "siAllParam")
        closest = sorted(target, key=lambda t: ratio(x.FullName, t))[-1]
        Application.PasteAllAnimation(closest)
