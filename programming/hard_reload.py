import sys
from wishlib.qt import QtGui, widgets
from wishlib.si import sianchor, si


class HardReload(widgets.QDialog):

    def __init__(self, parent=None):
        super(HardReload, self).__init__(parent)
        self.initUI()

    def initUI(self):
        self.ui_lineEdit = QtGui.QLineEdit(self)
        ui_completer = QtGui.QCompleter(
            [i.split(".")[0] for i in sys.modules.keys()], self)
        ui_completer.setCompletionMode(QtGui.QCompleter.InlineCompletion)
        ui_completer.setCaseSensitivity(0)
        self.ui_lineEdit.setCompleter(ui_completer)
        hbox = QtGui.QHBoxLayout()
        hbox.addWidget(self.ui_lineEdit)
        self.setLayout(hbox)
        self.setWindowTitle("Hard Reload")
        self.ui_lineEdit.returnPressed.connect(self.accept)

    def accept(self, *args, **kwds):
        module = str(self.ui_lineEdit.text())
        if len(module):
            for k in sys.modules.keys():
                if k.startswith(module):
                    del sys.modules[k]
        super(HardReload, self).close(*args, **kwds)


HardReload(sianchor()).exec_()
si.UpdatePlugins()
