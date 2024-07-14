# models/user.py
import  csv

from Databases.csv_handler import CSVHandler

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.data_file = f"data/{self.username}.csv"

    def register(self, path ,data):
        CSVHandler.write_csv(path, data)
        # with open('users.csv', 'a', newline='') as file:
        #     writer = csv.writer(file)
        #     writer.writerow([self.username, self.password])
         

    def save_data(self, height, weight, date):
        with open(self.data_file, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([date, height, weight, self.calculate_bmi(height, weight)])

    def calculate_bmi(self, height, weight):
        return round(weight / (height/100)**2, 2)

    def view_history(self):
        return CSVHandler.read_csv(self.data_file)
