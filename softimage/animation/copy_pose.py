import quicklauncher


data = dict()
for x in Application.Selection:
    pose = dict()
    kine = x.Kinematics.Local
    for p in ("pos", "rot", "scl"):
        for a in "xyz":
            pose[p + a] = kine.Parameters(p + a).Value
    data[x.FullName] = pose

quicklauncher.copy_pose_from = data  # monkeypatch selected poses
