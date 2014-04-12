from pymel import core as pm
from riglab.utils import align2curve

align2curve(pm.selected()[:-1], pm.selected()[-1])
