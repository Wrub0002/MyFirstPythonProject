from controller.controller import RecordManager
from view.view import View
from persitence.file_io import FileIO
from controller.chart import ChartManager
import os

def main():
    """
    Main function to manage records.
    Provides options to populate, view, add, edit, delete records, and generate a pie chart.
    """
    controller = RecordManager()
    base_dir = os.path.dirname(os.path.abspath(__file__))
    csv_file = os.path.join(base_dir, "data", "keystone-throughput-and-capacity.csv")

    while True:  # Keep looping until the user chooses to exit
        View.display_menu()
        choice = View.get_user_input("Enter your choice: ")

        if choice == '1':  # Populate database
            try:
                FileIO.populate_database_from_csv(csv_file)
            except Exception as e:
                View.display_message(f"Error populating database: {e}")
        elif choice == '2':  # View records
            controller.load_records()
        elif choice == '3':  # Add record
            record_data = View.get_record_data()
            controller.add_record(*record_data)
        elif choice == '4':  # Edit record
            record_id = View.get_record_id()
            if record_id:
                updated_data = View.get_record_data()
                controller.edit_record(record_id, updated_data)
        elif choice == '5':  # Delete record
            record_id = View.get_record_id()
            if record_id:
                controller.delete_record(record_id)
        elif choice == '6':  # Generate Pie Chart
            try:
                column_name = View.get_column_name()
                data = controller.get_column_data(column_name)
                if data:
                    ChartManager.generate_pie_chart(data, column_name)
                    View.display_message("Pie chart generated successfully!")
                else:
                    View.display_message(f"No data available for column '{column_name}'.")
            except Exception as e:
                View.display_message(f"Error generating pie chart: {e}")
        elif choice == '7':  # Exit
            View.display_message("Exiting the system. Goodbye!")
            break  # Exit the loop
        else:
            View.display_message("Invalid choice. Please try again.")


if __name__ == '__main__':
    main()
