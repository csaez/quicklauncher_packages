from wishlib.si import si, sisel, C, simath, project_into_mesh

mesh = si.PickElement(C.siPolyMeshFilter)("PickedElement")
if mesh:
    tgt = si.PickPosition()
    if tgt("ButtonPressed"):
        position = project_into_mesh(mesh, [tgt("Pos" + x) for x in "XYZ"], 4)
        if position:
            tm = sisel(0).Kinematics.Global.Transform
            tm.SetTranslation(simath.CreateVector3(position))
            sisel(0).Kinematics.Global.Transform = tm
