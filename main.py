from services.csv_reader import CSVReader
from views.record_display import RecordDisplay

if __name__ == "__main__":
    print("Leonardo Wrubleski's Project")

    # Create a CSVReader object to read the CSV file
    csv_reader = CSVReader('data/data.csv')

    # Read the CSV data into a list of Record objects
    records = csv_reader.read_csv()

    # Display the records using the RecordDisplay class
    if records:
        RecordDisplay.display(records)
    else:
        print("No records to display.")
