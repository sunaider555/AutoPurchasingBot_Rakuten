
import os
import requests
import psutil
from PyQt5.QtWidgets import (
    QWidget, QMessageBox
)
from PyQt5 import QtCore
from PyQt5.QtGui import QIcon
from PyQt5.uic import loadUi

from uuid import getnode as get_mac

class loginDialog(QWidget):
    parents         = ""
    area_details1   = []
    area_details2   = []
    datas           = []
    values          = []
    ops             = []

    def __init__(self, mainUI, parent=None):
        super().__init__(parent)
        self.parents = mainUI

        loadUi("ui/login.ui", self)
        cur_path = os.path.abspath(os.getcwd())
        self.setUI(cur_path)      
        
    def setUI(self, path):
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)

        image_path = path.replace("\\", "/") + "/image/license.jpg"         
        sheet = "background-image: url("+image_path+");"
        self.back_label.setStyleSheet(sheet)

        image_path = path.replace("\\", "/") + "/image/buttons/active.png"  
        image_over_path = path.replace("\\", "/") + "/image/buttons/active_over.png"   
        sheet = "QPushButton{border-image: url("+image_path+"); background-color: rgba(255, 255, 255, 0);} QPushButton:hover{border-image: url("+image_over_path+"); background-color: rgba(255, 255, 255, 0);}  QPushButton:pressed{border-image: url("+image_path+"); background-color: rgba(255, 255, 255, 0);}"
        self.login_button.setStyleSheet(sheet)

        image_path = path.replace("\\", "/") + "/image/buttons/logout.png"  
        image_over_path = path.replace("\\", "/") + "/image/buttons/logout_over.png"   
        sheet = "QPushButton{border-image: url("+image_path+"); background-color: rgba(255, 255, 255, 0);} QPushButton:hover{border-image: url("+image_over_path+"); background-color: rgba(255, 255, 255, 0);}  QPushButton:pressed{border-image: url("+image_path+"); background-color: rgba(255, 255, 255, 0);}"
        self.logout_button.setStyleSheet(sheet)

        mIcon = QIcon(path.replace("\\", "/") + "/image/logo.png" )
        self.setWindowIcon(mIcon)
        
        mac = get_mac()
        self.lineEdit_userID.setText(str(mac))
    
    def test_license(self):
        license = ""
        try:
            f       = open("resource/lisence.txt", "r", encoding="utf-8_sig")
            license = f.read()
            f.close() 
        except:
            self.show()
            return
                
        mac     = get_mac()
        url = f"http://xs296172.xsrv.jp/admin-owner/getUser?userID={mac}&password={license}"
        type, validDate = self.getHtml(url)
        
        if type == "network error":
            QMessageBox.warning(self, "警告", f"サーバー接続からエラーが発生しました。")
            self.logout()
        if type == "true":            
            self.parents.show()
            self.hide()
        if type == "expired":   
            QMessageBox.warning(self, "警告", f"許可期間が満了しました。(有効期限: {validDate} )\n プログラムを使用するには、ライセンスキーを新しく発行する必要があります。")
            self.show()
        if type == "fail":   
            self.show()
                      
    def login(self):
        userID      = self.lineEdit_userID.text()                
        password    = self.lineEdit_password.text().upper()
        url = f"http://xs296172.xsrv.jp/admin-owner/getUser?userID={userID}&password={password}"
        type, validDate = self.getHtml(url)
        
        if type == "true":
            QMessageBox.information(self, "お知らせ", f"接続に成功しました。\n プログラムの有効期限は {validDate}です。")
            f       = open("resource/lisence.txt", "w", encoding="utf-8_sig")
            f.write(password)   
            f.close()         
            self.parents.show()
            self.hide()
        if type == "expired":   
            QMessageBox.warning(self, "警告", f"許可期間が満了しました。(有効期限: {validDate} )\n プログラムを使用するには、ライセンスキーを新しく発行する必要があります。")
            self.logout()
        if type == "fail":   
            QMessageBox.warning(self, "警告", f"あなたは登録された加入者ではありません。\n ログイン情報をもう一度入力してください。")
            self.logout()

    def text_change(self):
        password    = self.lineEdit_password.text().upper()
        self.lineEdit_password.setText(password)
        
    def getHtml(self, url):
        try:
            result      = requests.get(url)
        except:
            return ("network error", "")

        html        = result.text
        html        = html.replace("\"", "")
        results     = html.split(",")
        type        = results[0]
        validDate   = results[1]
        
        return (type, validDate)

    def logout(self):
        current_system_pid = os.getpid()
        ThisSystem = psutil.Process(current_system_pid)
        ThisSystem.terminate()   
