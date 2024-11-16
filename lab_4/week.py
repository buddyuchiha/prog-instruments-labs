import os
import csv
import datetime

from logging_config import (
    get_info_logger,
    get_value_logger
)


info_logger = get_info_logger()
value_logger = get_value_logger()


def write_to_file(file_name, data):
    """
    Записывает данные в отдельный файл.
    """
    with open(file_name, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(data)
def split_csv_by_weeks(path, output_folder):
    """
    Разбивает исходный csv файл на файлы по неделям.
    """
    info_logger.info(
        "Running the split_ctv_by_weeks function with input path: %s and output folder: %s", 
        path, output_folder
        )
    with open(path, 'r') as f:
        reader = csv.reader(f)
        data = list(reader)
        
    start_date = datetime.datetime.strptime(data[0][0], '%Y-%m-%d')
    end_date = datetime.datetime.strptime(data[-1][0], '%Y-%m-%d')
    
    current_week_start = datetime.datetime(2008, 1, 10)
    current_week_end = datetime.datetime(2008, 1, 13)
    
    current_week_data = []
    
    for row in data:
        date = datetime.datetime.strptime(row[0], '%Y-%m-%d')
        
        if date >= current_week_start and date <= current_week_end:
            current_week_data.append(row)
        else:
            week_start_str = current_week_start.strftime('%Y%m%d')
            week_end_str = current_week_end.strftime('%Y%m%d')
            file_name = os.path.join(output_folder, f'{week_start_str}_{week_end_str}.csv')
            write_to_file(file_name, current_week_data)
            info_logger.info("he week has been processed: %s - %s ", 
                             week_start_str, week_end_str
                            )
            
            current_week_start = current_week_end + datetime.timedelta(days=1)
            current_week_end = current_week_start + datetime.timedelta(days=6)
            current_week_data = [row]
    
    week_start_str = current_week_start.strftime('%Y%m%d')
    week_end_str = current_week_end.strftime('%Y%m%d')
    file_name = os.path.join(output_folder, f'{week_start_str}_{week_end_str}.csv')
    write_to_file(file_name, current_week_data)
    info_logger.info(
        "The split_csv_by_weeks function is completed."
        )
    

