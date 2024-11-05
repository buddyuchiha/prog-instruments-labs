from functions import (
    read_csv_file,
    read_json_file,
    get_invalid_list
)
from paths import (
    DATA, 
    PATTERNS
)
from checksum import (
    calculate_checksum,
    serialize_result
)


if __name__ == '__main__':
    file_data = read_csv_file(DATA)
    file_patterns = read_json_file(PATTERNS)
    invalid_list = get_invalid_list(file_data, file_patterns)
   
    print(len(invalid_list))
    serialize_result(55, calculate_checksum(invalid_list))