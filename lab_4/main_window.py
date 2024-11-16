import sys
import datetime

import week
import year
import functions
import split

from datetime import datetime
from os import path
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget, QMainWindow
from design import Ui_MainWindow


class Weather(QMainWindow):
    def __init__(self):
        super(Weather, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.button_chose_file.clicked.connect(self.get_file_path)
        self.ui.button_weather.clicked.connect(self.get_weather_info)
        self.ui.split_csv_x_y.clicked.connect(self.cut_datatset_x_y)
        self.ui.split_csv_year.clicked.connect(self.cut_datatset_years)
        self.ui.split_csv_weeks.clicked.connect(self.cut_datatset_weeks)
        self.ui.get_folder_split_csv_x_y.clicked.connect(self.get_weather_x_y_info)
        self.ui.get_folder_button_split_csv_year.clicked.connect(self.get_weather_years_info)
        self.ui.get_folder_button_split_csv_weeks.clicked.connect(self.get_weather_weeks_info)
        self.chose_file_path = ""
        self.chose_x_y_path = ""
        self.chose_years_path = ""
        self.chose_weeks_path = ""
        
        
    def get_file_path(self) -> None:
        try:
            self.chose_file_path = QtWidgets.QFileDialog.getExistingDirectory(self, 'Выберите папку с датасетом')
            QtWidgets.QMessageBox.information(self, 'Папка с датасетом выбрана', self.chose_file_path)
            self.chose_file_path += "/dataset.csv"
        except:
            QtWidgets.QMessageBox.information(self, 'Ошибка', 'Выбран невозможный датасет')
        
    def get_weather_info(self):
        try:
            selected_date = self.ui.button_chose_weather.date().toString("yyyy-MM-dd")
            print(selected_date)
            info = functions.get_info(selected_date, self.chose_file_path)
            QtWidgets.QMessageBox.information(self, 'Данные за этот год', info)
        except:
            QtWidgets.QMessageBox.information(self, 'Ошибка', 'Вы не выбрали датасет')
    
    def get_weather_x_y_info(self):
        try: 
            selected_date = self.ui.button_chose_weather.date().toString("yyyy-MM-dd")
            print(selected_date)
            info = functions.get_info_XY(selected_date, self.chose_x_y_path)
            if not isinstance(info, list):
                info = [info]
            info_str = "\n".join(info)
            QtWidgets.QMessageBox.information(self, 'Данные за этот год', info_str)
        except:
            QtWidgets.QMessageBox.information(self, 'Ошибка', 'Разбейте файл и выберите верную дату')

 

    def get_weather_years_info(self):
        try:
            selected_date_str = self.ui.button_chose_weather.date().toString("yyyy-MM-dd")
            selected_date = datetime.strptime(selected_date_str, "%Y-%m-%d").date()
            info = functions.get_info_year(selected_date, self.chose_years_path)
            QtWidgets.QMessageBox.information(self, 'Данные за этот год', info[11:])
        except:
            QtWidgets.QMessageBox.information(self, 'Ошибка', 'Разбейте файл и выберите верную дату')

    def get_weather_weeks_info(self):
        try:
            selected_date_str = self.ui.button_chose_weather.date().toString("yyyy-MM-dd")
            selected_date = datetime.strptime(selected_date_str, "%Y-%m-%d").date()
            info = functions.get_info_week(selected_date, self.chose_weeks_path)
            QtWidgets.QMessageBox.information(self, 'Данные за этот год', info[11:])
        except:
            QtWidgets.QMessageBox.information(self, 'Ошибка', 'Разбейте файл и выберите верную дату')

    def cut_datatset_x_y(self) -> None:
        if not (self.chose_file_path):
            self.chose_file_path = QtWidgets.QFileDialog.getExistingDirectory(
            self, 'Выберите папку с датасетом')
            QtWidgets.QMessageBox.information(self, 'Папка с датасетом выбрана', self.chose_file_path)
            self.chose_file_path += "/dataset.csv"
            self.chose_x_y_path = QtWidgets.QFileDialog.getExistingDirectory(self, 'Выберите папку для выгрузки файлов X и Y')
            QtWidgets.QMessageBox.information(self, 'Папка для выгрузки файлов X и Y выбрана', self.chose_x_y_path)
            split.split_csv(self.chose_file_path, self.chose_x_y_path)
        elif (self.chose_file_path):
            self.chose_x_y_path = QtWidgets.QFileDialog.getExistingDirectory(self, 'Выберите папку для выгрузки файлов X и Y')
            QtWidgets.QMessageBox.information(self, 'Папка для выгрузки файлов X и Y выбрана', self.chose_x_y_path)
            split.split_csv(self.chose_file_path, self.chose_x_y_path)
            
    def cut_datatset_years(self) -> None:
        if not (self.chose_file_path):
            self.chose_file_path = QtWidgets.QFileDialog.getExistingDirectory(
            self, 'Выберите папку с датасетом')
            QtWidgets.QMessageBox.information(self, 'Папка с датасетом выбрана', self.chose_file_path)
            self.chose_file_path += "/dataset.csv"
            self.chose_years_path = QtWidgets.QFileDialog.getExistingDirectory(self, 'Выберите папку для выгрузки файлов по годам')
            QtWidgets.QMessageBox.information(self, 'Папка для выгрузки файлов по годам', self.chose_years_path)
            year.split_csv_by_years(self.chose_file_path, self.chose_years_path)
        elif (self.chose_file_path):
            self.chose_years_path= QtWidgets.QFileDialog.getExistingDirectory(self, 'Выберите папку для выгрузки файлов по годам')
            QtWidgets.QMessageBox.information(self, 'Папка для выгрузки файлов по годам', self.chose_years_path)
            year.split_csv_by_years(self.chose_file_path, self.chose_years_path)
        
    def cut_datatset_weeks(self) -> None:
        if not (self.chose_file_path):
            self.chose_file_path = QtWidgets.QFileDialog.getExistingDirectory(
            self, 'Выберите папку с датасетом')
            QtWidgets.QMessageBox.information(self, 'Папка с датасетом выбрана', self.chose_file_path)
            self.chose_file_path += "/dataset.csv"
            self.chose_weeks_path = QtWidgets.QFileDialog.getExistingDirectory(self, 'Выберите папку для выгрузки файлов по неделям')
            QtWidgets.QMessageBox.information(self, 'Папка для выгрузки файлов по неделям выбрана',  self.chose_weeks_path)
            week.split_csv_by_weeks(self.chose_file_path,  self.chose_weeks_path)
        else:
            self.chose_weeks_path = QtWidgets.QFileDialog.getExistingDirectory(self, 'Выберите папку для выгрузки файлов по неделям')
            QtWidgets.QMessageBox.information(self, 'Папка для выгрузки файлов по неделям выбрана',  self.chose_weeks_path)
            week.split_csv_by_weeks(self.chose_file_path,  self.chose_weeks_path)
        
        


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Weather()
    window.show()
    sys.exit(app.exec())