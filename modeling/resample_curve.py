from wishlib.si import si, sisel, sianchor
from PyQt4.QtGui import QInputDialog
from wishlib.qt.QtGui import QDialog


def get_positions(in_curve, in_segs):
    pos = list()
    null = si.ActiveSceneRoot.AddNull()
    cns = null.Kinematics.AddConstraint("Path", in_curve)
    for i in range(in_segs + 1):
        cns.Parameters("perc").Value = 100.0 / in_segs * i
        pos.append(null.Kinematics.Global.Transform.Translation.Get2())
    si.DeleteObj(null)
    return [str(coord) for coord in pos]


def resample_curve(in_curve, in_segs):
    curve = si.SICreateCurve(in_curve.Name, 1, 1)
    si.SISetCurvePoints(curve, ",".join(
        get_positions(in_curve, in_segs)), False)
    return curve


parent = QDialog(sianchor())
segs, ok = QInputDialog.getInteger(parent, "Resample Curve", "Segments", 3)
if ok:
    sel = list()
    result = list()
    for curve in list(sisel):
        if curve.Type != "crvlist":
            continue
        sel.append(curve)
        result.append(resample_curve(curve, segs))
    si.DeleteObj(sel)
    si.SelectObj(result)
parent.close()
