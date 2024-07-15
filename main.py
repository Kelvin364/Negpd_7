from patient import Patient
from bmi_calculator import BMICalculator
import google.generativeai as genai
from utils import register, login
import os
from dotenv import load_dotenv

def main():
    load_dotenv()
    # Initialize ChatGPT with the API key
    api_key = os.environ["API_KEY"]
    genai.configure(api_key=api_key)

    print("Welcome to the BMI App")
    try:
        while True:
            print("1. Register")
            print("2. Login")
            print("3. Exit")
            choice = input("Enter your choice: ")

            if choice == '1':
                register()
            elif choice == '2':
                patient = login()
                if patient:
                    while True:
                        print("1. Enter Parameters")
                        print("2. Get BMI Result")
                        print("3. View History")
                        print("4. Health Tips")
                        print("5. Chat with GPT")
                        print("6. Exit")
                        sub_choice = input("Enter your choice: ")

                        if sub_choice == '1':
                            height = float(input("Enter your height in cm: "))
                            weight = float(input("Enter your weight in kg: "))
                            date = input("Enter the date (YYYY-MM-DD): ")
                            patient.save_parameters(height, weight, date)
                        elif sub_choice == '2':
                            if patient.height and patient.weight:
                                bmi = BMICalculator.calculate_bmi(patient.height, patient.weight)
                                print(f"Your BMI is: {bmi}")
                            else:
                                print("Please enter your parameters first.")
                        elif sub_choice == '3':
                            patient.view_history()
                        elif sub_choice == '4':
                            print("Here are some health tips: Stay hydrated, eat balanced meals, and exercise regularly.")
                        elif sub_choice == '5':
                            query = input(f"Hi {patient} I would like to know how to help : ")
                            model = genai.GenerativeModel('gemini-1.5-flash')
                            response = model.generate_content(query)
                            print(response.text)
                        elif sub_choice == '6':
                            break
                        else:
                            print("Invalid choice. Please try again.")
            elif choice == '3':
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please try again.")
    except KeyboardInterrupt:
        print("\nProgram interrupted. Exiting gracefully...")

if __name__ == "__main__":
    main()
