import os
import csv
import datetime
def write_to_file(file_name, data):
    """
    Записывает данные в отдельный файл.
    """
    with open(file_name, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(data)
def split_csv_by_years(path, output_folder):
    """
    Разбивает исходный csv файл на N файлов, где каждый отдельный файл будет соответствовать одному году.
    Записывает файлы в папку task2.
    """
    with open(path, 'r') as f:
        reader = csv.reader(f)
        data = list(reader)
    years = set()
    for row in data:
        date_str = row[0]
        date = datetime.datetime.strptime(date_str, '%Y-%m-%d')
        years.add(date.year)
    for year in years:
        start_date = datetime.datetime(year, 1, 1).strftime('%Y%m%d')
        end_date = datetime.datetime(year, 12, 31).strftime('%Y%m%d')
        new_file_name = os.path.join(output_folder, f'{start_date}_{end_date}.csv')
        
        filtered_data = [row for row in data if datetime.datetime.strptime(row[0], '%Y-%m-%d').year == year]
        write_to_file(new_file_name, filtered_data)
        

