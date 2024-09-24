import csv
from models.record import Record
from typing import List

class CSVReader:
    """
    A class responsible for reading the CSV file and creating Record objects.
    """
    def __init__(self, file_path: str):
        self.file_path = file_path

    def read_csv(self) -> List[Record]:
        """
        Reads the CSV file and returns a list of Record objects.
        """
        records = [] # This is a list that stores the Record objects
        try:
            with open(self.file_path, mode='r') as file:
                csv_reader = csv.reader(file)
                next(csv_reader)  # Skip the header row
                for row in csv_reader:
                    record = Record(row[0], row[1], row[2])  # Create a Record object
                    records.append(record)
        except FileNotFoundError:
            print("File not found. Please make sure the file path is correct.")
        except Exception as e:
            print(f"An error occurred: {e}")
        return records
