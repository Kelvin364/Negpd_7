from patient import Patient
from bmi_calculator import BMICalculator
from chat_gpt import ChatGPT
from utils import register, login

def main():
    print("Welcome to the BMI App")
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
                        bmi = BMICalculator.calculate_bmi(patient.height, patient.weight)
                        print(f"Your BMI is: {bmi}")
                    elif sub_choice == '3':
                        patient.view_history()
                    elif sub_choice == '4':
                        tips = ChatGPT.get_health_tips()
                        print(tips)
                    elif sub_choice == '5':
                        query = input("Enter your query: ")
                        response = ChatGPT.chat(query)
                        print(response)
                    elif sub_choice == '6':
                        break
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
