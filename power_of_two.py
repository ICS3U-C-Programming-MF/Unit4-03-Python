#!/usr/bin/env python3
# Created by Maximiliano Fairman
# Created on Nov 18th, 2025# Create a program that accepts a whole number
# .It then uses a for loop to calculate
# and display the “square”(power of 2)


def main():
    # --- Input ---
    # Ask the user to enter any whole number (as a string for now)
    user_input = input("Enter a whole number: ")
    print("")  # Blank line for cleaner output spacing

    # --- Processing & Output ---
    try:
        # Try converting the input into an integer.
        # If the user types something invalid (like "abc"), it will jump to the except block.
        number = int(user_input)

        # Check if the number is negative
        if number < 0:
            print("Please enter a positive whole number.")
        else:
            # Loop from 0 up to the number the user entered (inclusive)
            for i in range(number + 1):
                # Calculate 2 raised to the power of i
                power_of_two = 2**i

                # Display the result for this value of i
                print(f"2 raised to the power of {i} is {power_of_two}")

    except ValueError:
        # Runs if the conversion to int fails (e.g., user entered letters or symbols)
        print("Invalid entry. Please enter a valid whole number.")


# Only run the program if this file is being executed directly
if __name__ == "__main__":
    main()
