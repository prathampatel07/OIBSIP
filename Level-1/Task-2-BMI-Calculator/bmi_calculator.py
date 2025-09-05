# bmi_calculator.py

def calculate_bmi(weight, height):
    return weight / (height ** 2)

def main():
    try:
        weight = float(input("Enter your weight in kilograms: "))
        height = float(input("Enter your height in meters: "))

        bmi = calculate_bmi(weight, height)
        print("\nYour BMI is:", round(bmi, 2))

        if bmi < 18.5:
            print("Category: Underweight")
        elif 18.5 <= bmi < 24.9:
            print("Category: Normal weight")
        elif 25 <= bmi < 29.9:
            print("Category: Overweight")
        else:
            print("Category: Obesity")

    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
