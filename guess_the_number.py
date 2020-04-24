from random import randint


def generate_number():
    randomNumber = randint(0, 20)
    return randomNumber


def main():
    theNumber = generate_number()
    print("Guess the number:")
    count = 0
    while True:
        number = input()
        try:
            number = int(number)
        except:
            print("Wrong number")
            continue
        if number == theNumber:
            print("Congradulations! ")
            print("The currect numbeer is " + str(number))
            break
        elif number > theNumber:
            print("Go lower")
            count += 1
        elif number < theNumber:
            print("Go higer")
            count += 1
        if count == 4:
            print("Sorry, You are failed!")
            break


main()