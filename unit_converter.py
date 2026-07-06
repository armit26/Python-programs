def km_to_miles(kilometers):
    return kilometers * 0.621371


def miles_to_km(miles):
    return miles / 0.621371


def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


def kg_to_pounds(kilograms):
    return kilograms * 2.20462


def pounds_to_kg(pounds):
    return pounds / 2.20462


while True:
    print("------ UNIT CONVERTER ------")
    print("1. Distance")
    print("2. Temperature")
    print("3. Weight")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("--- Distance Converter ---")
        print("1. Kilometers to Miles")
        print("2. Miles to Kilometers")

        dist_choice = int(input("Enter your choice: "))

        if dist_choice == 1:
            km = float(input("Enter kilometers: "))
            print("Miles:", round(km_to_miles(km), 2))

        elif dist_choice == 2:
            miles = float(input("Enter miles: "))
            print("Kilometers:", round(miles_to_km(miles), 2))

        else:
            print("Invalid choice.")

    elif choice == 2:
        print("--- Temperature Converter ---")
        print("1. Celsius to Fahrenheit")
        print("2. Fahrenheit to Celsius")

        temp_choice = int(input("Enter your choice: "))

        if temp_choice == 1:
            c = float(input("Enter Celsius: "))
            print("Fahrenheit:", round(celsius_to_fahrenheit(c), 2))

        elif temp_choice == 2:
            f = float(input("Enter Fahrenheit: "))
            print("Celsius:", round(fahrenheit_to_celsius(f), 2))

        else:
            print("Invalid choice.")

    elif choice == 3:
        print("--- Weight Converter ---")
        print("1. Kilograms to Pounds")
        print("2. Pounds to Kilograms")

        weight_choice = int(input("Enter your choice: "))

        if weight_choice == 1:
            kg = float(input("Enter kilograms: "))
            print("Pounds:", round(kg_to_pounds(kg), 2))

        elif weight_choice == 2:
            pounds = float(input("Enter pounds: "))
            print("Kilograms:", round(pounds_to_kg(pounds), 2))

        else:
            print("Invalid choice.")

    elif choice == 4:
        break

    else:
        print("Invalid choice.")