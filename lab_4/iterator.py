import csv
class DataIterator:
    def __init__(self, filename: str) -> None:
        self.filename = filename
        self.index = 0
        self.data = []
        with open(self.filename, 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                data = ' '.join(row[1:7])  
                self.data.append([row[0][:10], data])  
        print(self.data)       
    def __iter__(self):
        return self
    def __next__(self) -> int:
        while self.index < len(self.data):
            date, data = self.data[self.index]
            self.index += 1
            if data:
                return (date, data)
        raise StopIteration

def main() -> None:
    iterator = DataIterator('dataset.csv')
    for date, data in iterator:
        print(f"Дата: {date}, Данные о ветре: {data}")
        
if __name__ == "__main__":
    main()
            