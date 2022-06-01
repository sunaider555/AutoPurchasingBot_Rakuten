
import os
from PyQt5.QtWidgets import (
    QDialog
)
from PyQt5.uic import loadUi

class accountSettingDialog(QDialog):
    parents         = ""  

    def __init__(self, parent=None):
        super().__init__(parent)
        self.parents = parent

        loadUi("ui/accountSetting.ui", self)
        cur_path = os.path.abspath(os.getcwd())
        self.setModal(True)
        
    def get_account(self):
        ID          = self.lineEdit_id.text()
        password    = self.lineEdit_pass.text()
        return ID, password

    def set_account(self, ID, password):
        self.lineEdit_id.setText(ID)     
        self.lineEdit_pass.setText(password)

    def register(self):
        ID          = self.lineEdit_id.text()
        password    = self.lineEdit_pass.text()
        self.parents.set_account(ID, password)
        self.hide()
        