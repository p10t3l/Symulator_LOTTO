import random


def enter_the_number():
    while True:
        try:
            user_choice = int(input("Choose 6 different numbers between 1 and 49:  "))
            break
        except ValueError:
            print("This is not a number!")
    return user_choice


def choice_number():
    numbers = []
    while len(numbers) < 6:
        number = enter_the_number()
        if number not in numbers and 0 < number <= 49:
            numbers.append(number)
    return sorted(numbers)


def computer_choice():
    num = list(range(1, 50))
    random.shuffle(num)
    return sorted(num[:6])


def comparison():
    user_nuber = choice_number()
    computer_number = computer_choice()
    print("Your choice: ")
    print(user_nuber)
    print(" Computer numbers: ")
    print(computer_number)

    covered = 0
    for nuber in user_nuber:
        if nuber in computer_number:
            covered += 1
    print(f"Numbers that match: {covered}")


if __name__ == '__main__':
    comparison()
    
