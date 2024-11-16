import os 
import csv

from logging_config import (
    get_info_logger
)


info_logger = get_info_logger()


def split_csv(path, output_folder):
    """
    Разбивает исходный csv файл на файлы X.csv и Y.csv с одинаковым количеством строк.
    Первый файл содержит даты, второй файл содержит данные.
    """
    info_logger.info(
        "Running the split_csv function with input path %s and output path %s",
        path, output_folder
        )
    with open(path, 'r') as file:
        reader = csv.reader(file)
        data = list(reader)
    num_rows = len(data)
    x_file = os.path.join(output_folder, "X.csv")
    y_file = os.path.join(output_folder, "Y.csv")
    with open(x_file, 'w', newline='') as file_x, open(y_file, 'w', newline='') as file_y:
        writer_x = csv.writer(file_x)
        writer_y = csv.writer(file_y)
        writer_x.writerow([data[0][0]])  
        writer_y.writerow(data[0][1:]) 
        for i in range(1, num_rows):
            writer_x.writerow([data[i][0]])  
            writer_y.writerow(data[i][1:]) 
    info_logger.info(
        "The split_csv function is completed. Files: %s, %s",
        x_file, y_file
        )
    

