from random import randint

number_to_guess = randint(1, 100)
count = 0

while True:
    number = int(input("Enter a number between 1 to 100: "))
    if number != number_to_guess:
        print("Wrong number entered. Please try again.")
        count += 1
        if number > number_to_guess:
            print("Enter a smaller number")
        elif number < number_to_guess:
            print("Enter a greater number")
    elif number == number_to_guess:
        break

print("Number gussed correctly!!")
print(f"Attempts required {count}")