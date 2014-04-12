from pymel import core as pm
from riglab.utils import curve2chain

for c in pm.selected():
    curve2chain(c)
