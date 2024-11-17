import mysql.connector
import csv
import os
from dotenv import load_dotenv

load_dotenv()

class FileIO:
    """Class to handle MySQL database operations."""

    @staticmethod
    def connect_to_db():
        """Connect to the MySQL database using credentials from .env."""
        return mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME")
        )

    @staticmethod
    def create_table():
        """Create a table in the database if it doesn't exist."""
        query = """
        CREATE TABLE IF NOT EXISTS records (
            id INT AUTO_INCREMENT PRIMARY KEY,
            date VARCHAR(10),
            month VARCHAR(2),
            year VARCHAR(4),
            company VARCHAR(255),
            pipeline VARCHAR(255),
            key_point VARCHAR(255),
            latitude FLOAT,
            longitude FLOAT,
            direction_of_flow VARCHAR(50),
            trade_type VARCHAR(50),
            product VARCHAR(100),
            throughput FLOAT,
            committed_volumes FLOAT,
            uncommitted_volumes FLOAT,
            nameplate_capacity FLOAT,
            available_capacity FLOAT,
            reason_for_variance TEXT
        )
        """
        with FileIO.connect_to_db() as conn:
            cursor = conn.cursor()
            cursor.execute(query)
            conn.commit()

    @staticmethod
    def populate_database_from_csv(file_path):
        """Populate the database from a CSV file."""
        try:
            conn = FileIO.connect_to_db()
            cursor = conn.cursor()

            cursor.execute("SELECT COUNT(*) FROM records;")
            row_count = cursor.fetchone()[0]

            if row_count > 0:
                print(f"Database already contains {row_count} records.")
                conn.close()
                return

            with open(file_path, mode='r') as file:
                csv_reader = csv.DictReader(file)
                for row in csv_reader:
                    cursor.execute(
                        """
                        INSERT INTO records (date, month, year, company, pipeline, key_point, latitude, longitude,
                                             direction_of_flow, trade_type, product, throughput, committed_volumes,
                                             uncommitted_volumes, nameplate_capacity, available_capacity, reason_for_variance)
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                        """,
                        (
                            row.get("Date"),
                            row.get("Month"),
                            row.get("Year"),
                            row.get("Company"),
                            row.get("Pipeline"),
                            row.get("Key Point"),
                            float(row.get("Latitude", 0)) if row.get("Latitude") else None,
                            float(row.get("Longitude", 0)) if row.get("Longitude") else None,
                            row.get("Direction Of Flow"),
                            row.get("Trade Type"),
                            row.get("Product"),
                            float(row.get("Throughput (1000 m3/d)", 0)) if row.get("Throughput (1000 m3/d)") else 0,
                            float(row.get("Committed Volumes (1000 m3/d)", 0)) if row.get(
                                "Committed Volumes (1000 m3/d)") else 0,
                            float(row.get("Uncommitted Volumes (1000 m3/d)", 0)) if row.get(
                                "Uncommitted Volumes (1000 m3/d)") else 0,
                            float(row.get("Nameplate Capacity (1000 m3/d)", 0)) if row.get(
                                "Nameplate Capacity (1000 m3/d)") else 0,
                            float(row.get("Available Capacity (1000 m3/d)", 0)) if row.get(
                                "Available Capacity (1000 m3/d)") else 0,
                            row.get("Reason For Variance", "N/A"),
                        ),
                    )
                conn.commit()
            conn.close()
            print("Database populated successfully.")
        except Exception as e:
            print(f"Error populating database: {e}")

    @staticmethod
    def insert_record(record):
        """Insert a record into the database."""
        query = """
        INSERT INTO records (
            date, month, year, company, pipeline, key_point, latitude, longitude,
            direction_of_flow, trade_type, product, throughput, committed_volumes,
            uncommitted_volumes, nameplate_capacity, available_capacity, reason_for_variance
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        with FileIO.connect_to_db() as conn:
            cursor = conn.cursor()
            cursor.execute(query, (
                record.date, record.month, record.year, record.company, record.pipeline, record.key_point,
                record.latitude, record.longitude, record.direction_of_flow, record.trade_type, record.product,
                record.throughput, record.committed_volumes, record.uncommitted_volumes,
                record.nameplate_capacity, record.available_capacity, record.reason_for_variance
            ))
            conn.commit()

    @staticmethod
    def fetch_all_records():
        """Fetch all records from the database."""
        query = "SELECT * FROM records"
        with FileIO.connect_to_db() as conn:
            cursor = conn.cursor()
            cursor.execute(query)
            rows = cursor.fetchall()
        return rows

    @staticmethod
    def update_record(record_id, updated_data):
        """Update a record in the database."""
        query = """
        UPDATE records
        SET date = %s, month = %s, year = %s, company = %s, pipeline = %s, key_point = %s, 
            latitude = %s, longitude = %s, direction_of_flow = %s, trade_type = %s, 
            product = %s, throughput = %s, committed_volumes = %s, uncommitted_volumes = %s, 
            nameplate_capacity = %s, available_capacity = %s, reason_for_variance = %s
        WHERE id = %s
        """
        with FileIO.connect_to_db() as conn:
            cursor = conn.cursor()
            cursor.execute(query, (
                updated_data.date, updated_data.month, updated_data.year, updated_data.company,
                updated_data.pipeline, updated_data.key_point, updated_data.latitude, updated_data.longitude,
                updated_data.direction_of_flow, updated_data.trade_type, updated_data.product,
                updated_data.throughput, updated_data.committed_volumes, updated_data.uncommitted_volumes,
                updated_data.nameplate_capacity, updated_data.available_capacity, updated_data.reason_for_variance,
                record_id
            ))
            conn.commit()

    @staticmethod
    def delete_record(record_id):
        """Delete a record from the database."""
        query = "DELETE FROM records WHERE id = %s"
        with FileIO.connect_to_db() as conn:
            cursor = conn.cursor()
            cursor.execute(query, (record_id,))
            conn.commit()
