from wishlib.si import si, sisel, C, simath, raycast


def project_volume(max_depth=2):
    geometry = si.PickElement(C.siPolyMeshFilter)("PickedElement")
    pick = si.PickPosition()
    if not geometry or not pick("ButtonPressed"):
        return
    # calculate direction
    cam = si.GetViewCamera(-1)
    position = cam.Kinematics.Global.Transform.Translation
    direction = simath.CreateVector3([pick("Pos" + x) for x in "XYZ"])
    direction.SubInPlace(position)
    direction.NormalizeInPlace()
    position = position.Get2()
    direction = direction.Get2()
    # raycast
    results = list()
    for i in range(max_depth):
        position = raycast(geometry, position, direction).position
        if position == (0, 0, 0):
            break
        results.append(position)
        position = [p + (direction[i] * 0.001) for i, p in enumerate(position)]
    # sum and return average
    return [sum(coord) / len(coord) for i, coord in enumerate(zip(*results))]

position = project_volume(12)
if position:
    tm = sisel(0).Kinematics.Global.Transform
    tm.SetTranslation(simath.CreateVector3(position))
    sisel(0).Kinematics.Global.Transform = tm
