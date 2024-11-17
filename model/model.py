class Record:
    """Model class representing a record from the CSV file."""

    def __init__(self, date, month, year, company, pipeline, key_point, latitude, longitude, direction_of_flow,
                 trade_type, product, throughput, committed_volumes, uncommitted_volumes, nameplate_capacity,
                 available_capacity, reason_for_variance):
        self.date = date
        self.month = month
        self.year = year
        self.company = company
        self.pipeline = pipeline
        self.key_point = key_point
        self.latitude = latitude
        self.longitude = longitude
        self.direction_of_flow = direction_of_flow
        self.trade_type = trade_type
        self.product = product
        self.throughput = throughput
        self.committed_volumes = committed_volumes
        self.uncommitted_volumes = uncommitted_volumes
        self.nameplate_capacity = nameplate_capacity
        self.available_capacity = available_capacity
        self.reason_for_variance = reason_for_variance

    def __str__(self):
        return (f"Date: {self.date}, Month: {self.month}, Year: {self.year}, Company: {self.company}, "
                f"Pipeline: {self.pipeline}, Key Point: {self.key_point}, Latitude: {self.latitude}, "
                f"Longitude: {self.longitude}, Direction Of Flow: {self.direction_of_flow}, Trade Type: {self.trade_type}, "
                f"Product: {self.product}, Throughput: {self.throughput}, Committed Volumes: {self.committed_volumes}, "
                f"Uncommitted Volumes: {self.uncommitted_volumes}, Nameplate Capacity: {self.nameplate_capacity}, "
                f"Available Capacity: {self.available_capacity}, Reason For Variance: {self.reason_for_variance}")
