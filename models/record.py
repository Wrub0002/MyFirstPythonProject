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

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_city(self):
        return self.city

    def set_name(self, name):
        self.name = name

    def set_age(self, age):
        self.age = age

    def set_city(self,city):
        self.city = city