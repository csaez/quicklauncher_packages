from wishlib.si import si, sisel, siget, C, project_into_mesh


def get_meshes():
    msj = "Please pick the polymesh you want to draw into."
    meshes = list()
    picked = si.PickElement(C.siPolyMeshFilter, msj)("PickedElement")
    while picked:
        if picked.FullName not in meshes:
            meshes.append(picked.FullName)
        picked = si.PickElement(C.siPolyMeshFilter, msj)("PickedElement")
    return map(siget, meshes)


def get_coord(meshes=None):
    # get meshes
    meshes = meshes or list()
    coord = si.PickPosition()
    if coord("ButtonPressed"):
        # get coord in screen space
        coord = [coord("Pos" + a) for a in "XYZ"]
        if si.GetKeyboardState()("Shift") == 2:  # CTRL key pressed
            return coord
        # raycast to meshes
        coords = filter(lambda x: x is not None,
                        [project_into_mesh(mesh, coord, 4) for mesh in meshes])
        coord = coords[0] if len(coords) else coord
        # return coord, raycast biased
        return coord
    return None


# collect meshes
meshes = list(sisel) if sisel.Count else get_meshes()
# get initial point
coord = get_coord(meshes)
if coord:
    # start drawing
    curve = si.SICreateCurve("crvlist", 1, 1)
    while coord is not None:
        si.SIAddPointOnCurveAtEnd(curve, *coord)
        # get next point
        coord = get_coord(meshes)
