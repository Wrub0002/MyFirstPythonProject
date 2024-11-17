import unittest
from controller.controller import RecordManager
from persitence.file_io import FileIO

class TestAddRecord(unittest.TestCase):
    """
    Test class for adding records to the database.
    """

    def setUp(self):
        """
        Prepares a clean database for each test.
        """
        self.record_manager = RecordManager()
        FileIO.create_table()
        with FileIO.connect_to_db() as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM records;")  # Clear the table
            conn.commit()

    def test_add_new_record(self):
        """
        Verifies a new record is added correctly.
        """
        with FileIO.connect_to_db() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT COUNT(*) FROM records;")
            initial_count = cursor.fetchone()[0]

        # Add a record
        self.record_manager.add_record(
            '2023-09-10', '9', '2023', 'Company A', 'Pipeline A', 'Key Point A', 48.1234, -97.5678,
            'South', 'Export', 'Product X', 1000, 800, 200, 1200, 200, 'Reason X'
        )

        with FileIO.connect_to_db() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT COUNT(*) FROM records;")
            new_count = cursor.fetchone()[0]

            cursor.execute("SELECT * FROM records WHERE company = 'Company A';")
            record = cursor.fetchone()

        # Assertions
        self.assertEqual(new_count, initial_count + 1)
        self.assertIsNotNone(record)
        self.assertEqual(record[4], 'Company A')
        self.assertEqual(record[2], '9')
        self.assertEqual(record[3], '2023')
        self.assertEqual(record[16], 200)
        self.assertEqual(record[17], 'Reason X')

if __name__ == '__main__':
    unittest.main()
