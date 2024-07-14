import getpass
from patient import Patient

def register():
    username = input("Enter a username: ")
    password = input("Enter a password: ")
    patient = Patient(username)
    patient.register(password)

def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    return Patient.login(username, password)
