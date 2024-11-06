# This is a simple Python script that asks for user's name and age, and prints a greeting.

def main():
    # Ask for user input
    name = input("What's your name? ")
    age = input("How old are you? ")
    
    # Make sure the age input is valid (it should be an integer)
    try:
        age = int(age)
    except ValueError:
        print("Oops! That doesn't seem to be a valid age. Please enter a number.")
        return
    
    # Output a message
    print(f"Hello, {name}! You are {age} years old.")
    
if __name__ == "__main__":
    main()
