number = 23
guess = int(input("Enter an integer: "))

if guess == number:
    print("Congratulations you guessed it.")


elif guess < number:
    print("No, it is a little higher")

else:
    print("No, it is a little lower")

print("Done")
