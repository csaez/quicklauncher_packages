from wishlib.si import sisel
import quicklauncher

quicklauncher.copy_from = list(sisel)  # monkeypatch selected obj
