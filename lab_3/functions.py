import json
import csv
import re


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
        raise FileNotFoundError(f'"The file {file_path} does not exist') \
            from e
    except Exception as e:
        raise e
        
        
def read_json_file(file_path: str) -> dict:
    """
    Read JSON from file.
    Args:
    - file_path (str): The path to the JSON file to be read.
    Returns:
    - dict: The JSON data.
    """
    try:
        with open(file_path, mode = "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError as e:
        raise FileNotFoundError(f"The file {file_path} does not exist") \
            from e
    except Exception as e:
        raise e
        

def write_json_file(file_path: str, file_content: dict) -> None:
    """
    Write a dictionary to a JSON file.
    Args:
    - file_path (str): The path to the file to be written.
    - file_content (dict): The dictionary to write to the file.
    Returns:
    - None
    """
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(file_content, file)
    except FileNotFoundError as e:
        raise FileNotFoundError(f"The file {file_path} does not exist") \
            from e
    except Exception as e:
        raise e
        
        
def check_validation(file_data: list, file_patterns: dict) -> bool:
    """
    Checking file validation by using patterns.
    Args:
    - file_data (list): File whith data.
    - file_patterns (dict): Patterns of regex.
    Returns:
    - bool: Validated or no.
    """
    for key, value in zip(file_patterns.keys(), file_data):
        if not re.match(file_patterns[key], value):
            print(f"Validation failed for {key}: {value}")  
            return False
    return True


def get_invalid_list(file_data: list, file_patterns: dict) -> list[int]:
    """
    Getting invalidated list.
    Args:
    - file_data (list): File with data.
    - file_patterns (dict): Patterns of regex.
    Returns:
    - list (int): Rows with mistakes.
    """
    invalid_list = []
    for i, row in enumerate(file_data):
        if not check_validation(row, file_patterns):
            invalid_list.append(i)
    return invalid_list