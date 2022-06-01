from PyQt5.QtWidgets import (
    QFrame,  QLabel, QWidget, QVBoxLayout
)
from PyQt5.uic import loadUi

class progressbar(QWidget):
    bar     = ""
    label   = ""
    frame   = ""

    def __init__(self, parent=None):
        super().__init__(parent)

        self.frame  = QFrame()
        self.frame.setFrameShape(1)
        self.frame.setMaximumHeight(10)
        self.frame.setMinimumHeight(10)
        
        self.bar    = QLabel(self.frame)
        self.bar.setMaximumHeight(10)
        self.bar.setMinimumHeight(10)
                
        sheet       = "background-color: rgba(0, 0, 255, 150)"
        self.bar.setStyleSheet(sheet)
        self.setValue(0)

        layout      = QVBoxLayout()        
        self.label  = QLabel()
        self.label.setText("停止状態")

        self.setLayout(layout)        
        layout.addWidget(self.label)
        layout.addWidget(self.frame)

    def setStyles(self, type):
        if type == "normal":
            sheet       = "background-color: rgba(0, 0, 255, 150)"
        elif type == "success":
            sheet       = "background-color: rgba(255, 0, 0, 150)"
        elif type == "fail":
            sheet       = "background-color: rgba(0, 0, 0, 150)"
            
        self.bar.setStyleSheet(sheet)

    def setValue(self, val):
        width = self.width()
        cur_width = width * val / 100
        self.bar.setMinimumWidth(cur_width)
        self.bar.setMaximumWidth(cur_width)
        self.bar.move(0, 0)

    def setText(self, text):
        self.label.setText(text)

    def getText(self):
        return self.label.text()    