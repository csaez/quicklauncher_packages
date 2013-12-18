from wishlib.si import sisel


def group(obj):
    grp = obj.Parent.AddNull(obj.Name + "_grp")
    grp.Kinematics.Global.Transform = obj.Kinematics.Global.Transform
    grp.AddChild(obj)
    for param in ("viewvis", "rendvis"):
        grp.Properties("Visibility").Parameters(param).Value = False
    return grp

group(sisel(0))
