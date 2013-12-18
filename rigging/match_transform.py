from wishlib.si import si, sisel

picked = si.PickObject()("PickedElement")
if picked:
    sisel(0).Kinematics.Global.Transform = picked.kinematics.Global.Transform