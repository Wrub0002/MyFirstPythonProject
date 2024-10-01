import csv
from models.record import Record
from services.csv_reader import CSVReader

records = []

def add_new_record():
    name = input("Enter name:")
    age = input("Enter age:")
    city = input ("Enter city:")
    new_record = Record(name, age, city)
    records.append(new_record)
    print(f"Record for {name} added")

def edit_new_record():
    name_to_edit = input("Enter the name of the record to edit: ")
    for rec in records:
        if rec.get_name() == name_to_edit:
            new_name = input("Enter new name: ")
            new_age = input("enter new age: ")
            new_city = input("Enter new city: ")
            rec.set_name(new_name)
            rec.set_age(new_age)
            rec.set_city(new_city)
            print(f"Record for {new_name} updated.")
            return
        print("Record not found.")

def delete_record():
    name_to_delete = input("Enter the name of record to delete: ")
    for rec in records:
        if rec.get_name() == name_to_delete:
            records.remove(rec)
            print(f"Record for {name_to_delete} deleted.")
            return
        print("Record not found.")

def display_records():
    for rec in records:
        print(rec)

def load_data():
    global records
    reader = CSVReader ('data/data.csv')
    records = reader.read_csv()
    print(f"Loaded {len(records)} records.")

def save_data(filename='new_data.csv'):
    try:
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['name', 'age', 'city'])  # Write the header row
            for rec in records:
                writer.writerow([rec.get_name(), rec.get_age(), rec.get_city()])
        print(f"Data saved successfully to {filename}.")
    except Exception as e:
        print(f"An error occurred while saving the data: {e}")
