from wishlib import show_qt, inside_softimage
from hard_reload import HardReload

show_qt(HardReload, modal=True)
if inside_softimage():
    from wishlib.si import si
    si.UpdatePlugins()
