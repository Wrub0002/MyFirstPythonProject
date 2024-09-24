class Record:
    """
    A class to represent a record from the CSV file.
    """
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, City: {self.city}"
