number = 23
running = True


while running:
    guess = int(input("Enter an integer: "))

    if guess == number:
        print("Congratulations, you guessed the number")

        running = False

    elif guess < number:
        print("The number is higher")
    else:
        print("The number is lower")
