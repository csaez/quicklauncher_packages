from wishlib.si import si, sisel

sel = list(sisel)
parents = [x.parent for x in sel]
null = si.ActiveSceneRoot.AddNull()
for x in list(sisel):
    null.AddChild(x)
for axis in "xyz":
    null.Kinematics.Local.Parameters("scl"+axis).Value = -1
null.Kinematics.Local.Parameters("rotx").Value = 180
for i, x in enumerate(sel):
    parents[i].AddChild(x)
si.DeleteObj(null)