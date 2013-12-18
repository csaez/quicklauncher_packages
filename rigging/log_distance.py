import math
from wishlib.si import sisel

pos = [x.Kinematics.Global.Transform.Translation.Get2() for x in sisel]
dist = lambda a, b: math.sqrt(sum([(a[i] - b[i]) ** 2 for i in range(3)]))
print dist(*pos[:2])
