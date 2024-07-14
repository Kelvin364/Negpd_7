import csv
import os

class Patient:
    def __init__(self, username, height=None, weight=None, date=None):
        self.username = username
        self.height = height
        self.weight = weight
        self.date = date

    def register(self, password):
        with open('data/patients.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([self.username, password])
        print(f"Patient {self.username} registered successfully.")

    @staticmethod
    def login(username, password):
        with open('data/patients.csv', mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == username and row[1] == password:
                    print(f"Patient {username} logged in successfully.")
                    return Patient(username)
            print("Invalid username or password.")
            return None

    def save_parameters(self, height, weight, date):
        self.height = height
        self.weight = weight
        self.date = date
        with open(f'data/{self.username}_data.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([height, weight, date])
        print("Parameters saved successfully.")

    def view_history(self):
        filepath = f'data/{self.username}_data.csv'
        if os.path.exists(filepath):
            with open(filepath, mode='r') as file:
                reader = csv.reader(file)
                for row in reader:
                    print(row)
        else:
            print("No history found.")
