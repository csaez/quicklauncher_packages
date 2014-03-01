from wishlib.qt import QtCore, QtGui
from wishlib.si import *


class BatchSelection(QtGui.QDialog):

    def __init__(self, parent=None):
        super(BatchSelection, self).__init__(parent)
        self.setup_ui()
        self.execute_button.clicked.connect(self.execute_clicked)
        # self.code_plainTextEdit.setPlainText("obj.Name = ")

    def setup_ui(self):
        self.resize(294, 281)
        self.verticalLayout = QtGui.QVBoxLayout(self)
        self.verticalLayout.setSpacing(3)
        self.verticalLayout.setMargin(6)
        self.forloop_label = QtGui.QLabel(self)
        self.forloop_label.setText(
            "from wishlib.si import *\nfor i, obj in enumerate(list(sisel)):")
        self.verticalLayout.addWidget(self.forloop_label)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.indent_label = QtGui.QLabel(self)
        self.indent_label.setText("    ")
        self.horizontalLayout.addWidget(self.indent_label)
        self.code_plainTextEdit = QtGui.QPlainTextEdit(self)
        self.code_plainTextEdit.setTabStopWidth(12)
        self.horizontalLayout.addWidget(self.code_plainTextEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.execute_button = QtGui.QToolButton(self)
        sizePolicy = QtGui.QSizePolicy(
            QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.execute_button.sizePolicy().hasHeightForWidth())
        self.execute_button.setSizePolicy(sizePolicy)
        self.execute_button.setMinimumSize(QtCore.QSize(0, 25))
        self.execute_button.setText("EXECUTE")
        self.verticalLayout.addWidget(self.execute_button)
        self.indent_label.setBuddy(self.code_plainTextEdit)
        self.setTabOrder(self.code_plainTextEdit, self.execute_button)

    def execute_clicked(self):
        code = "from wishlib.si import *\n\n"
        code += "for i, obj in enumerate(list(sisel)):\n    "
        code += str(self.code_plainTextEdit.toPlainText()).replace(
            "\n", "\n    ")
        try:
            exec(code)
        except Exception as err:
            log(err, C.siError)

show_qt(BatchSelection)
