if Application.Selection(0).Type == "polySubComponent":
    op = Application.ApplyTopoOp("MeshLocalSubdivision")
else:
    op = Application.ApplyTopoOp("MeshLocalSubdivision", "%s.poly[*]" % Application.Selection(0).FullName)
Application.InspectObj(op)
