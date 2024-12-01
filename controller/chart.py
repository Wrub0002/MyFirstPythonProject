import matplotlib.pyplot as plt
from collections import Counter

class ChartManager:
    @staticmethod
    def generate_pie_chart(data, column_name):
        """
        Generate a pie chart for the given column data.
        """
        if not data:
            print(f"No data available to generate the pie chart for '{column_name}'.")
            return

        # Count occurrences of unique values
        value_counts = Counter(data)
        labels, sizes = zip(*value_counts.items())

        # Create the pie chart
        plt.figure(figsize=(8, 8))
        plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
        plt.title(f"Pie Chart of {column_name}")
        plt.show()
