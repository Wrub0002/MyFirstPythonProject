import csv
from models.record import Record

records = []

def add_new_record(name, age, city):
    """Add a new record to the in-memory list."""
    new_record = Record(name, age, city)
    records.append(new_record)

def edit_new_record(name, new_name, new_age, new_city):
    """Edit an existing record in the in-memory list."""
    for rec in records:
        if rec.get_name() == name:
            rec.set_name(new_name)
            rec.set_age(new_age)
            rec.set_city(new_city)
            return

def delete_record(name):
    """Delete a record from the in-memory list."""
    global records
    records = [rec for rec in records if rec.get_name() != name]

def save_data(filename='data/new_data.csv'):
    """Save the in-memory records to a CSV file."""
    try:
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['name', 'age', 'city'])
            for rec in records:
                writer.writerow([rec.get_name(), rec.get_age(), rec.get_city()])
        print(f"Data saved successfully to {filename}.")
    except Exception as e:
        print(f"An error occurred while saving the data: {e}")

def load_records_from_csv(file_path):
    """Load records from CSV file."""
    global records
    records = []
    try:
        with open(file_path, mode='r') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                record = Record(row['name'], row['age'], row['city'])
                records.append(record)
        return records
    except Exception as e:
        print(f"Error reading CSV: {e}")
        return []
