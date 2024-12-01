class View:
    """Class responsible for user interaction and displaying messages."""

    @staticmethod
    def display_menu():
        """Display the main menu for the Record Management System."""
        print("\n=== Record Management System ===")
        print("1. Populate database from CSV")
        print("2. View all records")
        print("3. Add a new record")
        print("4. Edit an existing record")
        print("5. Delete a record")
        print("6. Generate a Pie Chart")
        print("7. Exit")

    @staticmethod
    def get_user_input(prompt):
        """Get input from the user."""
        return input(prompt)

    @staticmethod
    def display_message(message):
        """Display a message to the user."""
        print(message)

    @staticmethod
    def display_records(records):
        """Display all records from the database."""
        if not records:
            print("No records available.")
        else:
            print("\n=== Records ===")
            for record in records:
                print(f"ID: {record[0]}")
                print(f"Date: {record[1]}")
                print(f"Month: {record[2]}")
                print(f"Year: {record[3]}")
                print(f"Company: {record[4]}")
                print(f"Pipeline: {record[5]}")
                print(f"Key Point: {record[6]}")
                print(f"Latitude: {record[7]}")
                print(f"Longitude: {record[8]}")
                print(f"Direction of Flow: {record[9]}")
                print(f"Trade Type: {record[10]}")
                print(f"Product: {record[11]}")
                print(f"Throughput: {record[12]}")
                print(f"Committed Volumes: {record[13]}")
                print(f"Uncommitted Volumes: {record[14]}")
                print(f"Nameplate Capacity: {record[15]}")
                print(f"Available Capacity: {record[16]}")
                print(f"Reason for Variance: {record[17]}")
                print("-" * 50)  # Separator for better readability

    @staticmethod
    def get_record_data():
        """Get record data from user input."""
        date = input("Enter Date (YYYY-MM-DD): ")
        month = input("Enter Month (1-12): ")
        year = input("Enter Year: ")
        company = input("Enter Company: ")
        pipeline = input("Enter Pipeline: ")
        key_point = input("Enter Key Point: ")
        latitude = input("Enter Latitude: ")
        longitude = input("Enter Longitude: ")
        direction_of_flow = input("Enter Direction of Flow: ")
        trade_type = input("Enter Trade Type: ")
        product = input("Enter Product: ")
        throughput = input("Enter Throughput (1000 m3/d): ")
        committed_volumes = input("Enter Committed Volumes (1000 m3/d): ")
        uncommitted_volumes = input("Enter Uncommitted Volumes (1000 m3/d): ")
        nameplate_capacity = input("Enter Nameplate Capacity (1000 m3/d): ")
        available_capacity = input("Enter Available Capacity (1000 m3/d): ")
        reason_for_variance = input("Enter Reason for Variance: ")

        return (
            date,
            month,
            year,
            company,
            pipeline,
            key_point,
            latitude,
            longitude,
            direction_of_flow,
            trade_type,
            product,
            throughput,
            committed_volumes,
            uncommitted_volumes,
            nameplate_capacity,
            available_capacity,
            reason_for_variance,
        )

    @staticmethod
    def get_record_id():
        """Get the ID of a record from user input."""
        try:
            record_id = int(input("Enter the record ID: "))
            return record_id
        except ValueError:
            print("Invalid input. Please enter a valid numeric ID.")
            return None

    @staticmethod
    def get_column_name():
        """
        Prompt the user for the column name to generate a pie chart.
        """
        return input("Enter the column name to generate a pie chart: ")
