import csv
import os
import datetime

from logging_config import (
    get_info_logger,
    get_value_logger
)


info_logger = get_info_logger()
value_logger = get_value_logger()


def get_info(my_date: datetime.date, path) -> str:
        """
        Получает погоду.
        """
        info_logger.info(
            "Running the get_info function with date %s and file %s",
            my_date, path
            )
        with open (path, 'r', encoding = "utf-8") as f:
            reader = csv.reader(f)
            data = list(reader)
            for row in data:
                if str(row[0][0:10]) == str(my_date):
                    value_logger.info(
                        "The get_info function found the data for %s",
                        my_date
                        )
                    return (row[1]) + ' ' + (row[2]) + ' ' + (row[3]) + ' ' + (row[4]) + ' ' + (row[5]) + ' ' + (row[6])
                if str(my_date) < str(row[0][0:10]):
                    value_logger.info(
                        "The get_info function did not find data for %s",
                        my_date
                        )
                    return None

def get_info_XY(my_date: datetime.date, path) -> str:
    """
    Получает погоду из файлов X и Y.
    """
    info_logger.info(
        "Running the get_info_XY function with date %s and file %s",
        my_date, path
        )
    x_file = os.path.join(path, "X.csv")
    y_file = os.path.join(path, "Y.csv")
    with open(x_file, 'r', encoding = "utf-8") as x, open(y_file, 'r', encoding="utf-8") as y:
        reader_x = csv.reader(x)
        data_x = list(reader_x)
        reader_y = csv.reader(y)
        data_y = list(reader_y)
        counter = 0
        for row in data_x:
            if str(row[0][0:10]) == str(my_date):
                value_logger.info(
                    "The get_info_XY function found the data for %s",
                    my_date
                    )
                return data_y[counter]
            if str(my_date) > str(row[0][0:10]):
                counter+=1 
            if str(my_date) < str(row[0][0:10]):
                    value_logger.info(
                        "The get_info_XY function did not find data for %s",
                        my_date
                        )
                    return None
                



def get_info_year(my_date: datetime.date, path) -> str:
    """
    Получает погоду из файлов с годами.
    """
    info_logger.info(
        "Running the get_info_year function with date %s and file %s",
        my_date, path
        )
    year = my_date.strftime("%Y")
    file_name = os.path.join(path, year + "0101_" + year + "1231.csv")

    with open(file_name, 'r', encoding = "utf-8") as file:
        reader = csv.reader(file)
        data = list(reader)
        for row in data:
            if row[0] == my_date.strftime("%Y-%m-%d"):
                value_logger.info(
                    "The get_info_year function found the data for %s",
                    my_date
                    )
                return ",".join(row)

def get_info_week(my_date: datetime.date, path) -> str:
    """
    Получаем погоду из файлов с неделями.
    """
    info_logger.info(
        "Running the get_info_week function with date %s and file %s",
        my_date, path
        )
    my_week = my_date.weekday()
    start_date = my_date - datetime.timedelta(days=my_week)
    end_date = my_date + datetime.timedelta(days=6 - my_week)

    start_date_str = start_date.strftime("%Y%m%d")
    end_date_str = end_date.strftime("%Y%m%d")

    file_name = os.path.join(path, start_date_str + '_' + end_date_str + '.csv')

    with open(file_name, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        data = list(reader)
        for row in data:
             if row[0] == my_date.strftime("%Y-%m-%d"):
                value_logger.info(
                    "The get_info_week function found data for %s",
                    my_date)
                return ",".join(row)




