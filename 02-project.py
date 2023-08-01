def main():
    print("Enter the numbers you want to sum. Press 'q' to exit.")

    total = 0
    while True:
        
        try:
            user_input = input("Enter a number: ")
            if user_input.lower() == 'q':
                break
            number = float(user_input)
            total += number
        except ValueError:
            print("Invalid input. Please enter a number or press 'q' to exit.")

    print("Sum of the entered numbers:", total)

if __name__ == "__main__":
    main()
