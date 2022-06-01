import os
import sys
import csv
from numpy import product
import requests
from PyQt5.QtWidgets import (
    QApplication, QWidget, QMessageBox, QTableWidgetItem, QDesktopWidget, QHBoxLayout, QVBoxLayout, QSpacerItem, QToolButton, QLabel
)

from PyQt5 import QtCore
from PyQt5.QtGui import QIcon
from PyQt5.uic import loadUi
from setting_Dialog import settingDialog
from progressbar import progressbar
from account_setting import accountSettingDialog
from threading import Timer
import psutil
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time
from playsound import playsound
from selenium.webdriver.chrome.service import Service as ChromeService # Similar thing for firefox also!
from subprocess import CREATE_NO_WINDOW
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup
import webbrowser
import timeit


class mainDialog(QWidget):

    setting_Dialog      = ""
    account_Setting     = ""
    play_buttons        = []
    edit_buttons        = []
    delete_buttons      = []
    progressbars        = []
    status_labels       = []
    threads             = []
    pause_state         = []
    state               = []
    oclock_thread       = ""
    progress_values     = []
    drivers             = []
    loops               = []

    ID                  = ""
    Password            = ""    
    
    def __init__(self, parent=None):
        super().__init__(parent)
        loadUi("ui/main.ui", self)     

        self.setWindowState(QtCore.Qt.WindowMaximized) 

        path = os.path.abspath(os.getcwd())
        mIcon = QIcon(path.replace("\\", "/") + "/image/icon.ico" )
        self.setWindowIcon(QIcon("image/icon.ico"))

        self.show()
        
        cur_path = os.path.abspath(os.getcwd())
        self.setUI(cur_path)
        self.show()
        screenShape = QDesktopWidget().screenGeometry()
        dv_width  = screenShape.width() / 2 

        dv_height = screenShape.height() / 2

        self.setting_Dialog = settingDialog(self)
        self.setting_Dialog.hide()
        self.setting_Dialog.move(int(dv_width-self.setting_Dialog.width()/2),int(dv_height-self.setting_Dialog.height()/2))
                          
        self.account_Setting = accountSettingDialog(self)
        self.account_Setting.hide()
        self.account_Setting.move(int(dv_width-self.setting_Dialog.width()/2),int(dv_height-self.setting_Dialog.height()/2)+100)

        self.oclock_thread  = Timer(0.001, self.oclock)        
        self.oclock_thread.start()
        self.append_thread(self.oclock_thread)

        self.open_account()
        self.open_setting()
                  
    def closeEvent(self, event):
        ref =  QMessageBox.question(self, "お問い合わせ", "プログラムを終了しますか？")
        if ref == 65536: 
            event.ignore()
        else:
            self.save_setting()

            current_system_pid = os.getpid()
            ThisSystem = psutil.Process(current_system_pid)
            ThisSystem.terminate()

            event.accept()
                   
    def setUI(self, path):  
        sheet = "color: rgb(255, 255, 255); background-color: rgba(13, 15, 42, 0); gridline-color: rgba(74, 132, 255, 255); selection-background-color: rgba(0, 0, 255, 100);alternate-background-color: rgba(255, 255, 255, 20);"
        self.tableWidget.setStyleSheet(sheet)  
        self.tableWidget.horizontalHeader().setStyleSheet("::section{background-color: rgba(100, 100, 100, 100);}")
        self.tableWidget.verticalHeader().setStyleSheet("::section{background-color: rgba(100, 100, 100, 100);}")
        self.tableWidget.resizeRowsToContents();
        self.tableWidget.setWordWrap(True)
        self.play_buttons = [] 

        self.tableWidget.setColumnWidth(0, 80)
        self.tableWidget.setColumnWidth(1, 100)
        self.tableWidget.setColumnWidth(2, 100)
        self.tableWidget.setColumnWidth(3, 200)
        self.tableWidget.setColumnWidth(4, 250)
        self.tableWidget.setColumnWidth(5, 150)
        self.tableWidget.setColumnWidth(6, 100)
        self.tableWidget.setColumnWidth(7, 100)
        self.tableWidget.setColumnWidth(8, 100)
        self.tableWidget.setColumnWidth(9, 100)
        self.tableWidget.setColumnWidth(10, 100)
        self.tableWidget.setColumnWidth(11, 250)
        self.tableWidget.setColumnWidth(12, 150)
      
        return

    def cell_dbclick(self, row, col):
        url = self.tableWidget.item(row, 4).text()
        ref =  QMessageBox.question(self, "お問い合わせ", f"次のURLをロードしますか？\n{url}")
        if ref == 65536: return  
        self.browser_open(url)
    def oclock(self):
        curTimes = time.localtime()

        dates = curTimes.tm_year*10000 + curTimes.tm_mon*100 + curTimes.tm_mday
        times = curTimes.tm_hour*60 + curTimes.tm_min 

        self.lcdNumber_year.display(curTimes.tm_year)
        self.lcdNumber_month.display(curTimes.tm_mon)
        self.lcdNumber_day.display(curTimes.tm_mday)
        self.lcdNumber_hour.display(curTimes.tm_hour)
        self.lcdNumber_minute.display(curTimes.tm_min)
        
        self.oclock_thread  = Timer(0.1, self.oclock)        
        self.oclock_thread.start()
        self.append_thread(self.oclock_thread)
    
    def sub_progress(self, progressbar, index):
        if self.state[index]:
            progress_value              = (self.progress_values[index]+1) % 101
            self.progress_values[index] = progress_value
            progressbar.setValue(progress_value)
            thread  = Timer(0.05, self.sub_progress, [progressbar, index])        
            thread.start()
            self.append_thread(thread)

    def get_time(eslf):
        curTimes    = time.localtime()
        dateTimes   = (curTimes.tm_year*366 + curTimes.tm_mon*31 + curTimes.tm_mday)*24*60 + curTimes.tm_hour*60 + curTimes.tm_min 
        return dateTimes

    def setting(self):
        self.setting_Dialog.row         = self.tableWidget.rowCount()
        self.setting_Dialog.show()
        self.setting_Dialog.init()

    def account(self):
        self.account_Setting.show()

    def append_table(self, data):
        [type, type_str, img, title, url, dates_str, price, count, loops, size, color, product_type, date_times, status] = data
        table   = self.tableWidget
        row     = table.rowCount()
        table.setRowCount(row+1)
        table.setRowHeight(row, 80)
        
        widget_play     = self.create_play_button()        
        widget_edit     = self.create_edit_button()        
        widget_progress = self.create_progress_bar()    
        widget_thum     = self.create_thum(row)

        for i in range(1, 11):

            item = QTableWidgetItem(data[i])
            if i != 4:  
                item.setTextAlignment(132)
            table.setItem(row, i, item)

        table.setCellWidget(row, 0, widget_play)
        table.setCellWidget(row, 2, widget_thum)
        table.setCellWidget(row, 11, widget_progress)
        table.setCellWidget(row, 12, widget_edit)
        table.item(row, 1).setData(4, type)
        table.item(row, 3).setData(4, product_type)
        table.item(row, 5).setData(4, date_times)
        table.item(row, 10).setData(4, status)

        self.pause_state.append(False)
        self.state.append(False)
        self.progress_values.append(0)
        self.loops.append(int(loops))

        drivers = []
        self.drivers.append(drivers)

        widget_progress.setStyles("normal")
        widget_progress.setValue(0)
        widget_progress.setText(status)

    def edit_table(self, data, row):
        [type, type_str, img, title, url, dates_str, price, count, loops, size, color, product_type, date_times, status] = data
        table   = self.tableWidget
        
        for i in range(1, 11):
            table.item(row, i).setText(data[i])

        widget_thum     = self.create_thum(row)

        table.setCellWidget(row, 2, widget_thum)
        table.item(row, 1).setData(4, type)        
        table.item(row, 3).setData(4, product_type)        
        table.item(row, 5).setData(4, date_times)
        table.item(row, 10).setData(4, status)

        self.play_buttons[row].setEnabled(True)
        
        progressbar = self.progressbars[row]
        progressbar.setStyles("normal")
        progressbar.setValue(0)
        progressbar.setText(status)

    def create_play_button(self):
        play_button         = QToolButton()
        image_path          = os.path.abspath(os.getcwd()).replace("\\", "/") + "/image/play.png"                 
        image_over_path     = os.path.abspath(os.getcwd()).replace("\\", "/") + "/image/play_over.png"                 
        image_check_path    = os.path.abspath(os.getcwd()).replace("\\", "/") + "/image/play_checked.png"                 
        sheet               = "QToolButton{background-image: url("+image_path+");background-color: rgba(255, 255, 255, 0)}QToolButton:hover{background-image: url("+image_over_path+");}QToolButton:checked{background-image: url("+image_check_path+");}"
        play_button.setFixedSize(42,42)
        play_button.setStyleSheet(sheet)
        play_button.setCursor(QtCore.Qt.PointingHandCursor)
        play_button.setCheckable(True)
        play_button.clicked.connect(self.play_clicked)
        self.play_buttons.append(play_button)

        widget              = QWidget()
        layout              = QHBoxLayout()
        spacer1             = QSpacerItem(10,10)
        spacer2             = QSpacerItem(10,10)

        widget.setLayout(layout)
        layout.addSpacerItem(spacer1)
        layout.addWidget(play_button)
        layout.addSpacerItem(spacer2)                

        return widget  

    def create_thum(self, index):
        fileName            = f"resource/thums/{index}.jpg"                
        thum                = QLabel()
        image_path          = os.path.abspath(os.getcwd()).replace("\\", "/") + "/" + fileName                            
        sheet               = "border-image: url("+image_path+");"
        thum.setStyleSheet(sheet)
        thum.setFixedSize(60,60)

        widget              = QWidget()
        layout              = QHBoxLayout()
        spacer1             = QSpacerItem(10,10)
        spacer2             = QSpacerItem(10,10)

        widget.setLayout(layout)
        layout.addSpacerItem(spacer1)
        layout.addWidget(thum)
        layout.addSpacerItem(spacer2)                

        return widget  

    def create_edit_button(self):
        container   = QWidget()
        container.setMaximumWidth(100)

        edit_button         = QToolButton(container)
        image_path          = os.path.abspath(os.getcwd()).replace("\\", "/") + "/image/edit.png"                 
        image_over_path     = os.path.abspath(os.getcwd()).replace("\\", "/") + "/image/edit_over.png"                     
        sheet               = "QToolButton{background-image: url("+image_path+");background-color: rgba(255, 255, 255, 0)}QToolButton:hover{background-image: url("+image_over_path+");}QToolButton:pressed{background-image: url("+image_path+");}"
        edit_button.move(0, 0)
        edit_button.setFixedSize(42,42)
        edit_button.setStyleSheet(sheet)
        edit_button.setCursor(QtCore.Qt.PointingHandCursor)
        edit_button.clicked.connect(self.edit_clicked)

        delete_button        = QToolButton(container)
        delete_button.move(50, 0)
        image_path          = os.path.abspath(os.getcwd()).replace("\\", "/") + "/image/delete.png"                 
        image_over_path     = os.path.abspath(os.getcwd()).replace("\\", "/") + "/image/delete_over.png"                     
        sheet               = "QToolButton{background-image: url("+image_path+");background-color: rgba(255, 255, 255, 0)}QToolButton:hover{background-image: url("+image_over_path+");}QToolButton:pressed{background-image: url("+image_path+");}"
        delete_button.setFixedSize(42,42)
        delete_button.setStyleSheet(sheet)
        delete_button.setCursor(QtCore.Qt.PointingHandCursor)
        delete_button.clicked.connect(self.delete_clicked)

        center_layout       = QVBoxLayout()   
        spacer1             = QSpacerItem(10,10)
        spacer2             = QSpacerItem(10,10)
              
        center_layout.addSpacerItem(spacer1)
        center_layout.addWidget(container)
        center_layout.addSpacerItem(spacer2)

        widget              = QWidget()    
        layout              = QHBoxLayout()   
        spacer1             = QSpacerItem(10,10)
        spacer2             = QSpacerItem(10,10)

        widget.setLayout(layout)        
        layout.addSpacerItem(spacer1)
        layout.addLayout(center_layout)
        layout.addSpacerItem(spacer2)
        
        self.edit_buttons.append(edit_button)
        self.delete_buttons.append(delete_button)

        return widget

    def create_progress_bar(self):        
        progress_bar        = progressbar()   
        self.progressbars.append(progress_bar)

        return progress_bar    

    def play_clicked(self):
        sender = self.sender()
        for obj in self.play_buttons:
            if obj == sender:
                index = self.play_buttons.index(obj)

                if obj.isChecked():
                    self.pause_state[index] = False
                    self.state[index]       = True
                    self.play(index)
                else:                    
                    loops = int(self.tableWidget.item(index, 8).text())
                    if len(self.drivers[index]) < loops:
                        obj.setChecked(True)
                        ref = QMessageBox.warning(self, "お知らせ", "Web閲覧機積載中なので停止操作はできません。しばらくしてからもう一度お試しください。")    
                        return 

                    self.pause_state[index] = True
                    self.state[index]       = False
                    self.pause(index)    
                break

    def edit_clicked(self):
        sender = self.sender()
        for obj in self.edit_buttons:
            if obj == sender:
                index = self.edit_buttons.index(obj)
                if self.state[index] == True:
                    ref = QMessageBox.warning(self, "お知らせ", "実行中は編集操作ができません。")
                    return  
                self.editItem(index)
                break

    def delete_clicked(self):
        sender = self.sender()
        for obj in self.delete_buttons:
            if obj == sender:
                index = self.delete_buttons.index(obj)
                if self.state[index] == True:
                    ref = QMessageBox.warning(self, "お知らせ", "実行中は削除操作はできません。")    
                    return 
                ref = QMessageBox.question(self, "お問い合わせ", "本当に削除しますか？")    
                if ref == 65536:
                    return
                self.deleteItem(index)
                break
                    
    def deleteItem(self, index): 
        self.tableWidget.removeRow(index)
        self.play_buttons.remove(self.play_buttons[index])
        self.edit_buttons.remove(self.edit_buttons[index])
        self.delete_buttons.remove(self.delete_buttons[index])
        self.progressbars.remove(self.progressbars[index])
        # self.threads.remove(self.threads[index])
        self.progress_values.remove(self.progress_values[index])
        self.drivers.remove(self.drivers[index])    
        self.pause_state.remove(self.pause_state[index])
        self.state.remove(self.state[index])

    def editItem(self, index):
        data        = []
        table       = self.tableWidget        
        type        = table.item(index, 1).data(4)        
        title       = table.item(index, 3).text()       
        url         = table.item(index, 4).text()       
        dates       = table.item(index, 5).text()
        price       = table.item(index, 6).text()
        count       = table.item(index, 7).text()
        loops       = table.item(index, 8).text()
        size        = table.item(index, 9).text()
        color       = table.item(index, 10).text()
        product_type= table.item(index, 3).data(4) 
        data        = [type, url, price, count, loops, size, color, dates, index, title, product_type]
        
        self.setting_Dialog.setValue(data)

    def play(self, index):
        table       = self.tableWidget        
        type        = table.item(index, 1).data(4)        
        url         = table.item(index, 4).text()               
        product_type= int(table.item(index, 3).data(4))               
        dates       = table.item(index, 5).data(4)

        price       = ""
        if table.item(index, 6).text() != "": price = int(table.item(index, 6).text())

        count       = int(table.item(index, 7).text())
        loops       = int(table.item(index, 8).text())
        size        = table.item(index, 9).text()
        color       = table.item(index, 10).text()
        data        = [type, url, price, count, loops, size, color, dates, index, product_type]        
        
        progressbar                         = self.progressbars[index]
        self.progress_values[index]         = 0
        progressbar.setValue(0)
        progressbar.setText("閲覧機ロード中...")
        
        thread  = Timer(0.01, self.sub_progress, [progressbar, index])        
        thread.start()
        self.append_thread(thread)
        
        for i in range(0, 5):
            thread = ""    
            if type == 1:
                thread         = Timer(0.001, self.time_order, [data])        
            elif type == 2:
                thread         = Timer(0.001, self.price_order, [data])       
            else:
                thread         = Timer(0.001, self.store_order, [data])        

            thread.start()
            self.append_thread(thread)
        
        for i in range(0, loops):
            thread         = Timer(0.001, self.open_browser, [url, index])   
            thread.start()   
            self.append_thread(thread)


    def get_url(self, url, index, i):
        self.drivers[index][i].get(url)

    def pause(self, index):
        loops                               = int(self.tableWidget.item(index, 8).text())
        progressbar                         = self.progressbars[index]
        self.progress_values[index]         = 0
        # self.threads[index]                 = []
        self.pause_state[index]             = True
        self.state[index]                   = False
        progressbar.setValue(0)
        progressbar.setText("停止状態")         

        for driver in self.drivers[index]:
            driver.close()

        self.drivers[index] = []    

    def product_have_check(self, data, html):
        [type, url, price, count, loops, size, color, dates, index, product_type] = data
        soup            = BeautifulSoup(html, 'html.parser') 
        
        if product_type == 1:
            button = soup.find(class_="new_addToCart")
            if button != None:
                return True
            else:
                return False    
        elif product_type == 2:
            result1 = html.split("この商品は販売期間前です。")
            result2 = html.split("売り切れました")
            
            if len(result1) > 1 or len(result2) > 1:
                return False
            else:
                return True    
            
    def time_order(self, data):
        [type, url, price, count, loops, size, color, dates, index, product_type] = data
        
        cur_time    = self.get_time()
        order_time  = int(dates) 

        print ("===", index)
        progressbar = self.progressbars[index]

        if (cur_time < order_time - 5):            
            progressbar.setText("待機中...")

            if self.pause_state[index]: return
            thread         = Timer(0.001, self.time_order, [data])        
            thread.start()
            self.append_thread(thread)
            return

        html = self.get_html(url)
        while html == "":
            print("error")
            html = self.get_html(url)

        if self.pause_state[index]: return

        status = self.product_have_check(data,  html)

        if status:    
            if (cur_time >= order_time):   
                if self.pause_state[index]: return    
                if len(self.drivers[index]) == loops:           
                    progressbar.setText("購入中(- 1段階 -)")
                    thread         = Timer(0.001, self.cart, [data])        
                    thread.start()       
                    self.append_thread(thread)             
                    return

        if self.pause_state[index]: return

        thread         = Timer(0.001, self.time_order, [data])        
        thread.start()
        self.append_thread(thread)
        # self.append_thread(index, thread)

    def price_order(self, data):
        [type, url, price, count, loops, size, color, dates, index, product_type] = data
        
        cur_time    = self.get_time()
        end_time    = int(dates) 

        progressbar = self.progressbars[index]

        if (cur_time >= end_time):            
            progressbar.setText("監視期限切れ")
            progressbar.setStyles("fail")
            self.pause_state[index] = True
            progressbar.setValue(100)
            self.play_buttons[index].setChecked(False)
            self.play_buttons[index].setEnabled(False)
            return

        html = self.get_html(url)
        while html == "":
            print("error")
            html = self.get_html(url)

        if self.pause_state[index]: return

        product_price = int(self.pick_value(html, "itemprop='price' content='", "'"))
        if product_price <= price:
            if self.pause_state[index]: return    
            if len(self.drivers[index]) < loops: return    
            self.pause_state[index] = True
            self.start = timeit.default_timer() 
            progressbar.setText("購入中(- 1段階 -)")
            self.cart(data)
            return

        progressbar.setText("監視中...")

        if self.pause_state[index]: return        

        thread         = Timer(0.001, self.price_order, [data])        
        thread.start()
        self.append_thread(thread)

    def store_order(self, data):
        [type, url, price, count, loops, size, color, dates, index, product_type] = data
        
        cur_time    = self.get_time()
        end_time    = int(dates)

        progressbar = self.progressbars[index]

        if (cur_time >= end_time):            
            progressbar.setText("監視期限切れ")

            self.pause_state[index] = True
            progressbar.setValue(0)
            self.play_buttons[index].setChecked(False)
            return

        html = self.get_html(url)
        while html == "":
            print("error")
            html = self.get_html(url)

        if self.pause_state[index]: return

        status = self.product_have_check(data,  html)
        if status: 
            if self.pause_state[index]: return    
            if len(self.drivers[index]) < loops: return    
            self.pause_state[index] = True

            progressbar.setText("購入中(- 1段階 -)")
            self.cart(data)
            return

        progressbar.setText("監視中...")

        if self.pause_state[index]: return        

        thread         = Timer(0.001, self.store_order, [data])        
        thread.start()
        self.append_thread(thread)

    def cart(self, data):
        self.start = timeit.default_timer() 
        [type, url, price, count, loops, size, color, dates, index, product_type] = data
        
        while len(self.drivers[index]) < loops:
            True              
        
        if self.pause_state[index] : return

        for i in range(0, int(loops)):
            self.pause_state[index] = True
            thread         = Timer(0.001, self.cart_process, [data, i, url])        
            thread.start()    
            self.append_thread(thread)      

    def cart_process(self, data, i, url):
        [type, url, price, count, loops, size, color, dates, index, product_type] = data

        try:
            driver  = self.drivers[index][i]    
            driver.delete_all_cookies()
            driver.refresh()   
            button = ""
            
            result = True
            while result:
                try:
                    if product_type == 1:
                        try:
                            button = driver.find_element_by_xpath("//button[@class='new_addToCart']")       
                            button.click()    
                            result = False
                        except:
                            result = True    
                    elif product_type == 2:     
                        try:                                 
                            button = driver.find_element_by_xpath("//button[@class='cart-button checkout new-cart-button ']")
                            result = False
                        except:
                            button = driver.find_element_by_xpath("//button[@class='cart-button checkout new-cart-button sku-submit-checkout']")
                            result = False
                        try:    
                            select_tag = driver.find_elements_by_name("choice")
                            select = Select(select_tag[0])
                            select.select_by_value("ご注文から30分以内は、理由の有無を問わず購入履歴からキャンセルすることが可能です。※楽天の一部サービス（楽券やあす楽など）を除くなお、当店では、ご注文から30分以上過ぎた場合、お客様都合によるキャンセルは承っておりません。あらかじめご了承ください。:了解しました。")

                            select = Select(select_tag[1])
                            select.select_by_value("ご注文完了後のプレゼントラッピングの追加/配送先住所変更/配送指定日の変更・追加は承れません。ご注意の上ご注文のほど、よろしくお願い致します。また、こちらを理由にキャンセルを承ることもできません。:了解しました。")                      
                        except:
                            result = True
                except:
                    result = True

            button.click()

            self.progressbars[index].setText("購入中(-2段階-)")

            result = True
          
            while result:
                try:
                    select = Select(driver.find_element_by_name('units[0]'))
                    select.select_by_value(str(count))
                    
                    if product_type == 1:
                        button = driver.find_element_by_id("js-cartBtn")
                    elif product_type == 2:    
                        button = driver.find_element_by_xpath("//input[@class='big-red-button large-button purchaseButton ratTrackingEvent']")

                    button.click()   
                    result = False
                except:
                    result = True      

            self.progressbars[index].setText("購入中(-3段階-)")

            result = True
            while result:
                try:                           
                    self.ID, self.password = self.account_Setting.get_account()
                    inputElement = driver.find_element_by_name("u")
                    inputElement.send_keys(self.ID)
                    inputElement = driver.find_element_by_name("p")
                    inputElement.send_keys(self.password)
                    result = False
                except:
                    driver.refresh()        
                    result = True    

            if product_type == 1:
                button = driver.find_element_by_name("submit")
            elif product_type == 2:
                button = driver.find_element_by_name("login_submit")   

            button.click()
            # driver.delete_cookie('ak_bmsc')

            self.progressbars[index].setText("購入中(-4段階-)")

            result = True
            while result:
                try:
                    if product_type == 1:       
                        button = driver.find_element_by_name("commit_order")
                    elif product_type == 2:
                        button = driver.find_element_by_name("commit")
                    button.click()                    
                    result = False
                except:
                    driver.refresh()        
                    result = True    
         
            result = True
            while result:
                try:
                    index = driver.page_source.index("errorTxt")                     
                    driver.refresh()        
                except:
                    result = False   
            self.progressbars[index].setText("購入中(-5段階-)")

            result = driver.page_source.split("アクセスが集中し、ページを閲覧しにくい状態になっております")
            while len(result) > 1:                 
                driver.refresh()
                result = driver.page_source.split("アクセスが集中し、ページを閲覧しにくい状態になっております")

            result= -1

            if product_type == 1:
                try:
                    result = driver.page_source.index("注文完了")
                except:
                    result = -1
            elif product_type == 2:               
                try:
                    result = driver.page_source.index("お買い上げありがとうございました！")
                except:
                    result = -1

            if result != -1:
                self.progressbars[index].setText(f"注文完了")
                self.progressbars[index].setStyles("success")
                path = os.path.abspath(os.getcwd())
                wavFile = path.replace("\\", "/") + "/resource/Alarm01.wav"
                try:
                    playsound(wavFile)
                except:
                    False     
            else:    
                result = -1
                try:
                    result = driver.page_source.index("お客様のクレジットカードはご利用できませんでした。")
                except:
                    result = -1

                if result != -1:
                    self.progressbars[index].setText(f"注文失敗(クレジットカードの使用不可)")
                else:
                    self.progressbars[index].setText(f"注文失敗")

                self.progressbars[index].setStyles("fail")
            
            self.drivers[index].remove(driver)
            driver.close()
            self.state[index] = False

            self.progressbars[index].setValue(100)
            self.play_buttons[index].setChecked(False)
            self.play_buttons[index].setEnabled(False)
            
        except:
            return

    def set_account(self, ID, password):
        self.ID         = ID
        self.password   = password
        self.save_account(ID, password)

    def append_thread(self, thread):
        # self.threads[index].append(thread)        
        for thread in self.threads:
            if not thread.is_alive():
                self.threads.remove(thread)

    def pick_value(self, tag, start, end, flag=True):
        try:
            if start != "":             
                tags  = tag.split(start)
                tag   = tags[1]                     
            
            if end != "":
                tags    = tag.split(end) 
                tag     = tags[0]
                
            tag     = tags[0].replace("&#039;", "'")            
            tag     = tag.replace("\t", "")
            tag     = tag.replace("\n", "")
            if flag:       
                return tag.replace(" ", "") 
            else:
                return tag
        except:
            return ""

    def get_html(self, URL, times=5): 
        try:       
            # headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'}

            URL     = URL.replace(" ", "")
            headers = {
            'authority': 'www.rakuten.co.jp',
            'method': 'GET',
            'path': '/',
            'scheme': 'https',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'cookie': '',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'en-US,en;q=0.9,ja;q=0.8',
            'cache-control': 'max-age=0',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': 'Windows',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate', 
            'sec-fetch-site': 'none',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'}
            
            result  = requests.get(URL, headers=headers)
            html    = result.text                        
            
            while len(html.split("Reference")) > 1:
                result  = requests.get(URL, headers=headers)
                html    = result.text                        
                
            html    = html.replace("\"", "'")    
        except: 
            print ("error")
            html    = ""
            
        return html   

    def open_browser(self, url, index):        
        options = Options()
        # options.add_argument("--disable-infobars")
        # options.add_argument("--disable-extensions")
        # options.add_argument('--log-level=OFF')
        # options.add_argument("no-default-browser-check")
        # options.add_argument("no-sandbox")
        # options.add_argument('allow-elevated-browser')
        # options.add_argument('--ignore-certificate-errors')    
        # options.add_argument('--ignore-certificate-errors')    
        # options.add_argument('User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36')
        options.add_argument("--disable-infobars")
        options.add_argument("--disable-extensions")
        options.add_argument('--log-level=OFF')
        options.add_argument("--lang=ja")        
        # options.add_argument("--headless");

        # options.add_experimental_option("useAutomationExtension", False)
        # options.add_argument('--ignore-ssl-errors=yes')
        # options.add_argument('--ignore-certificate-errors')
        # options.add_experimental_option("excludeSwitches",["enable-automation"])
        # options.add_experimental_option('excludeSwitches', ['enable-logging'])
        
        # driver = webdriver.Firefox(executable_path=r'c:/geckodriver.exe')
        # options.add_argument('--allow-insecure-localhost') # differ on driver version. can ignore. 
        # caps = options.to_capabilities()
        # caps["acceptInsecureCerts"] = True
        # driver = webdriver.Chrome(ChromeDriverManager().install(), desired_capabilities=caps)

        # capabilities = DesiredCapabilities.CHROME.copy()
        # capabilities["acceptInsecureCerts"] = True
        # driver = webdriver.Chrome(ChromeDriverManager().install(),desired_capabilities=capabilities)

        # options.add_argument('disable-infobars')
        # # options.add_argument('--headless')
        # options.add_argument('--no-sandbox')
        # options.add_argument('--disable-gpu')
        # options.add_argument('--disable-dev-shm-usage')
        # options.add_argument('--disable-extensions')
        # options.add_argument('--log-level=0')
        # options.add_argument('--FontRenderHinting[none]')
        # options.add_argument('--start-maximized')
        # options.add_argument('--proxy-bypass-list=*')
        # options.add_argument("--proxy-server='direct://'")
        # options.add_argument('--allow-runing-insecure-content')
        # options.add_argument('--ignore-certificate-errors')
        # options.add_argument('--disable-background-networking')
        # options.add_argument('--disable-client-side-phishing-detection')
        # options.add_argument('--disable-default-apps')
        # options.add_argument('--disable-hang-monitor')
        # options.add_argument('--disable-popup-blocking')
        # options.add_argument('--disable-prompt-on-repost')
        # options.add_argument('--disable-sync')
        # options.add_argument('--disable-web-resources')
        # options.add_argument('--enable-automation')
        # options.add_argument('--enable-logging')
        # options.add_argument('--force-fieldtrials=SiteIsolationExtensions/Control')
        # options.add_argument('--ignore-certificate-errors')
        # options.add_argument('--metrics-recording-only')
        # options.add_argument('--no-first-run')
        # options.add_argument('--password-store=basic')
        # options.add_argument('--disable-setuid-sandbox')
        # options.add_argument('--disable-accelerated-2d-canvas')
        # options.add_argument('--no-zygote')
    
        # options.add_argument('--test-type=webdriver')
        # options.add_argument('--use-mock-keychain')
        # options.add_argument('window-size=3000,2000')
     

        # options.add_argument("--user-data-dir=/home/username/.config/google-chrome")
        chrome_service = ChromeService(ChromeDriverManager().install())
        chrome_service.creationflags = CREATE_NO_WINDOW

        # driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        result = True
        while result:    
            try:
                driver = webdriver.Chrome(options=options, service=chrome_service)   
                result = False
            except:
                result = True


        driver.get(url) 
        self.drivers[index].append(driver)    

        progressbar                         = self.progressbars[index]
        self.progress_values[index]         = 0
        progressbar.setValue(0)
        progressbar.setText("監視中...")
          
    def save_account(self, account_id, account_pass):  
        header = ["ID", "password"]       
        try:              
            with open(f'resource/account.csv', 'w', encoding='utf-8_sig', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(header)
                writer.writerow([account_id, account_pass])
            f.close()
        except:
            return

    def open_account(self):         
        try:              
            with open(f'resource/account.csv', 'r', encoding='utf-8_sig', newline='') as f:
                reader = csv.DictReader(f)                           
                for row in reader:  
                    self.account_Setting.set_account(row["ID"], row["password"]) 
            f.close()
        except:
            return

    def save_setting(self):       
        header = ["type", "type_str", "img", "title", "url", "dates_str", "price", "count", "loops", "size", "color", "product_type", "date_times", "status"]  
        try:              
            with open(f'resource/setting.csv', 'w', encoding='utf-8_sig', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(header)
                table = self.tableWidget
                for row in range(0, table.rowCount()):     
                    data = []               
                    data.append(table.item(row, 1).data(4)) 
                    data.append(table.item(row, 1).text())
                    data.append(table.item(row, 2).text())
                    data.append(table.item(row, 3).text())
                    data.append(table.item(row, 4).text())
                    data.append(table.item(row, 5).text())
                    data.append(table.item(row, 6).text())
                    data.append(table.item(row, 7).text())
                    data.append(table.item(row, 8).text())                           
                    data.append(table.item(row, 9).text())                           
                    data.append(table.item(row, 10).text())                           
                    data.append(table.item(row, 3).data(4)) 
                    data.append(table.item(row, 5).data(4))                                            
                    data.append(self.progressbars[row].getText()) 
        
                    writer.writerow(data)
            f.close()
        except:
            return

    def open_setting(self):   
        header = ["type", "type_str", "img", "title", "url", "dates_str", "price", "count", "loops", "size", "color", "product_type", "date_times", "status"]  
             
        try:              
            with open(f'resource/setting.csv', 'r', encoding='utf-8_sig', newline='') as f:
                reader = csv.DictReader(f)                           
                for row in reader:         
                    data = []
                    data.append(int(row[header[0]]))
                    data.append(row[header[1]])
                    data.append(row[header[2]])
                    data.append(row[header[3]])
                    data.append(row[header[4]])
                    data.append(row[header[5]])
                    data.append(row[header[6]])
                    data.append(row[header[7]])
                    data.append(row[header[8]])
                    data.append(row[header[9]])
                    data.append(row[header[10]])
                    data.append(row[header[11]])
                    data.append(row[header[12]])
                    data.append(row[header[13]])
                    self.append_table(data)    
            f.close()
        except:
            return

    def browser_open(self, url):               
        webbrowser.open(url) 

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = mainDialog()    
    
    sys.exit(app.exec())
        