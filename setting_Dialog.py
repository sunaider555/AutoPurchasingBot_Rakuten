
import os
from PyQt5.QtWidgets import (
    QDialog, QMessageBox
)
from PyQt5.uic import loadUi
from PyQt5 import QtCore
import time
from bs4 import BeautifulSoup
import requests
import shutil

types = ["", "時間指定注文", "価格監視注文", "在庫監視注文"]
class settingDialog(QDialog):
    parents     = ""  
    type        = 1
    edit_flag   = False
    row         = 0
    old_url     = ""
    old_title   = ""
    product_type= ""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.parents = parent

        loadUi("ui/setting.ui", self)
        cur_path = os.path.abspath(os.getcwd())
        self.setUI(cur_path)
      
        self.setModal(True)

    def setUI(self, path):
        self.calendar.hide()        
        self.widget_price.hide()
    
    def init(self):
        curTimes    = time.localtime()
        
        dates       = str(curTimes.tm_year*10000 + curTimes.tm_mon*100 + curTimes.tm_mday)
        date_str    = f"{dates[0:4]}-{dates[4:6]}-{dates[6:8]}"

        qdate       = QtCore.QDate.fromString(date_str, "yyyy-MM-dd")   
        self.old_url = ""

        self.dateEdit.setDate(qdate)
        self.timeEdit.setTime(QtCore.QTime(curTimes.tm_hour, curTimes.tm_min))
        self.lineEdit_url.setText("")        
        self.dateEdit.setDate(qdate)
        self.lineEdit_price.setText("")
        self.spinBox_count.setValue(0)
        self.spinBox_loops.setValue(0)
        self.lineEdit_size.setText("")
        self.lineEdit_color.setText("")
        self.edit_flag = False

    def calendar_show(self):
        if self.calendar.isVisible():
            self.calendar.hide()
        else:    
            self.calendar.show()
            pos_x = self.widget_dateTime.x() + self.dateEdit.x() + 60
            pos_y = self.widget_dateTime.y() + self.dateEdit.y() + self.dateEdit.height() + 91
            self.calendar.move(pos_x, pos_y)
                
    def calendar_click(self, cur_date):
        date    = QtCore.QDate()
        date    = cur_date
        year    = date.year()
        month   = date.month()
        day     = date.day()
        
        if month < 10: month = f"0{month}"
        if day < 10: day = f"0{day}"
        
        str_date = f"{year}/{month}/{day}"
        self.dateEdit.setDate(date)
        self.calendar.hide()

    def type_1_click(self):
        self.type = 1
        self.radioButton_type_1.setChecked(True)
        self.widget_price.hide()
        self.label_dateTime.setText("購入時間")
    def type_2_click(self):
        self.type = 2
        self.radioButton_type_2.setChecked(True)
        self.widget_price.show()
        self.label_dateTime.setText("閉じる時間")
    def type_3_click(self):
        self.type = 3
        self.radioButton_type_3.setChecked(True)
        self.widget_price.hide()
        self.label_dateTime.setText("閉じる時間")

    def setValue(self, data):
        self.show()
        [type, url, price, count, loops, size, color, dates, self.row, title, product_type] = data
        if type == 1: self.type_1_click()
        if type == 2: self.type_2_click()
        if type == 3: self.type_3_click()

        date_str    = f"{dates[0:4]}-{dates[5:7]}-{dates[8:10]}"
        hour        = int(dates[11:13])
        minute      = int(dates[14:16])
        qdate       = QtCore.QDate.fromString(date_str, "yyyy-MM-dd")

        self.old_url        = url
        self.old_title      = title
        self.product_type   = product_type

        self.lineEdit_url.setText(url)        
        self.dateEdit.setDate(qdate)
        self.timeEdit.setTime(QtCore.QTime(hour, minute))
        self.lineEdit_price.setText(price)
        self.spinBox_count.setValue(int(count))
        self.spinBox_loops.setValue(int(loops))
        self.lineEdit_size.setText(size)
        self.lineEdit_color.setText(color)
        self.edit_flag = True

    def save(self):
        dt = self.timeEdit.time()
        dt_string2 = dt.toString(self.timeEdit.displayFormat())

        dt = self.dateEdit.date()
        dt_string1 = dt.toString(self.dateEdit.displayFormat())

        data        = []
        type        = self.type
        type_str    = types[type]
        url         = self.lineEdit_url.text()
        dates_str   = f"{dt_string1} {dt_string2}"        
        date_times  = (self.dateEdit.date().year()*366 + self.dateEdit.date().month()*31 + self.dateEdit.date().day())*24*60 + self.timeEdit.time().hour()*60 + self.timeEdit.time().minute()
        price       = self.lineEdit_price.text()
        count       = str(self.spinBox_count.value())
        loops       = str(self.spinBox_loops.value())
        size        = self.lineEdit_size.text()
        color       = self.lineEdit_color.text()
        status      = "停止状態"
        
        if url == self.old_url:
            title           = self.old_title
            img             = "jpg"
            product_type    = self.product_type
        else:    
            html            = self.parents.get_html(url)
            soup            = BeautifulSoup(html, 'html.parser') 

            try:
                img_div     = soup.find(id="loadingSlider")
                img_tag     = img_div.find("img")
                img_path    = img_tag['src']
                img         = self.image_download(img_path)
                title       = img_tag['alt']
                product_type= 1
            except:    
                img_div     = soup.find(class_="rakutenLimitedId_ImageMain1-3")
                img_tag     = img_div.find("img")
                img_path    = img_tag['src']
                img         = self.image_download(img_path)
                title       = img_tag['alt']
                product_type= 2
            
            if img == "" or title == "":
                QMessageBox.warning(self, "通知", "入力された商品は存在しません。 URLを再入力してください。")
                return

        data        = [type, type_str, "", title, url, dates_str, price, count, loops, size, color, product_type, date_times, status]
        
        

        if self.edit_flag:
            self.hide()
            self.parents.edit_table(data, self.row)
        else:    
            self.parents.append_table(data)

        self.row    += 1    

    def image_download(self, url):
        fileName    = f"resource/thums/{self.row}.jpg"
        try:
            r = requests.get(url, stream = True)
            if r.status_code == 200:
                r.raw.decode_content = True
                with open(fileName,'wb') as f:
                    shutil.copyfileobj(r.raw, f)
                    
                print('Image sucessfully Downloaded: ',fileName)
                return fileName    
        except:
            return ""

    def cancel(self):
        self.hide()
  