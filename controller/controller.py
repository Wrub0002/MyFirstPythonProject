from persitence.file_io import FileIO
from model.model import Record
from view.view import View

class RecordManager:
    """Controller class to manage the operations on records."""

    def __init__(self):
        """Initialize the RecordManager."""
        pass

    def load_records(self):
        """Load all records from the database and send them to the view for display."""
        try:
            records = FileIO.fetch_all_records()
            View.display_records(records)
        except Exception as e:
            View.display_message(f"Error loading records: {e}")

    def add_record(self, *data):
        """Add a new record to the database."""
        try:
            new_record = Record(*data)
            FileIO.insert_record(new_record)
            View.display_message("Record added successfully.")
        except Exception as e:
            View.display_message(f"Error adding record: {e}")

    def edit_record(self, record_id, updated_data):
        """Edit an existing record in the database."""
        try:
            updated_record = Record(*updated_data)
            FileIO.update_record(record_id, updated_record)
            View.display_message("Record updated successfully.")
        except Exception as e:
            View.display_message(f"Error updating record: {e}")

    def delete_record(self, record_id):
        """Delete a record from the database by its ID."""
        try:
            FileIO.delete_record(record_id)
            View.display_message("Record deleted successfully.")
        except Exception as e:
            View.display_message(f"Error deleting record: {e}")
