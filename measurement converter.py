def mm_to_cm(mm):
    return mm / 10

def cm_to_in(cm):
    return cm / 2.54

def in_to_ft(inches):
    return inches / 12

def ft_to_m(ft):
    return ft * 0.3048

def m_to_km(m):
    return m / 1000

def show_menu():
    print("Measurement Converter Menu:")
    print("1. Millimeters to Centimeters")
    print("2. Centimeters to Inches")
    print("3. Inches to Feet")
    print("4. Feet to Meters")
    print("5. Meters to Kilometers")
    print("6. Exit")

def convert_measurement(choice, value):
    if choice == 1:
        return mm_to_cm(value)
    elif choice == 2:
        return cm_to_in(value)
    elif choice == 3:
        return in_to_ft(value)
    elif choice == 4:
        return ft_to_m(value)
    elif choice == 5:
        return m_to_km(value)
    else:
        return None

def main():
    while True:
        show_menu()
        try:
            choice = int(input("Enter your choice (1-6): "))
            if choice == 6:
                print("Exiting the converter. Goodbye!")
                break
            elif choice < 1 or choice > 6:
                print("Invalid choice. Please select a valid option.")
                continue
            
            value = float(input("Enter the value to convert: "))
            result = convert_measurement(choice, value)
            if result is not None:
                print(f"Converted value: {result}\n")
            else:
                print("Invalid conversion.\n")
        except ValueError:
            print("Invalid input. Please enter a number.\n")

if __name__ == "__main__":
    main()
