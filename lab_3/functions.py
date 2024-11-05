import csv
import json


def read_csv_file(file_path:str) -> list[list[str]]:
    """
    Modifying from csv file to the list.
    Args:
    - file_path (str): The path to the file to be modified.
    Returns:
    - list[list[str]]: The content of the file.
    """
    try:
        file_data = []
        with open(file_path, mode = "r", encoding="utf-16") as file:
            file_reader = csv.reader(file, delimiter = ';')
            next(file_reader, None)
            for row in file_reader:
                file_data.append(row)
            return file_data
    except FileNotFoundError as e:
        raise FileNotFoundError(f'"The file {file_path} does not exist') from e
    except Exception as e:
        raise e
        
        
def read_json(file_path: str) -> dict:
    """
    Read JSON from file.
    Args:
    - file_path (str): The path to the JSON file to be read.
    Returns:
    - dict: The JSON data.
    """
    try:
        with open(file_path, mode = "r") as file:
            return json.load(file)
    except FileNotFoundError as e:
        raise FileNotFoundError(f"The file {file_path} does not exist") from e
    except Exception as e:
        raise e
        

