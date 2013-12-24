from difflib import SequenceMatcher
import quicklauncher


ratio = lambda x, y: SequenceMatcher(None, x, y). ratio()
if hasattr(quicklauncher, "copy_pose_from"):
    target = quicklauncher.copy_pose_from.keys()
    for x in Application.Selection:
        if not len(target):
            break
        closest = sorted(target, key=lambda t: ratio(x.FullName, t))[-1]
        target.remove(closest)
        for p, v in quicklauncher.copy_pose_from.get(closest).iteritems():
            x.Kinematics.Local.Parameters(p).Value = v
