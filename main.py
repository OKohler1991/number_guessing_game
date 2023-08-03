import random

number_lower = 1
number_higher = 100


class NumberOutOfRangeException(Exception):
    pass


def guess_number():
    number = random.randint(number_lower, number_higher)
    return number


def number_in_range(number):
    while True:
        try:
            number = int(number)
            if not (number_lower <= number <= number_higher):
                raise NumberOutOfRangeException
        except ValueError:
            number = input(
                f"You didn't enter a number, please enter a number between {number_lower} and {number_higher}: "
            )
        except NumberOutOfRangeException:
            number = input(
                f"Your number is not in guessing area, please enter a number between {number_lower} and {number_higher}: "
            )
        else:
            return number


def main():
    while True:
        game = "on"
        chosen_number = guess_number()
        print(chosen_number)
        while game == "on":
            player_number = input(
                f"Please enter a number between {number_lower} and {number_higher}: "
            )
            number = number_in_range(player_number)
            if number == chosen_number:
                print(
                    "Congratulation, you guessed the right number, do you want to play another round?"
                )
                player_input = input("Press 'Y' for yes or 'N' for no: ")
                if player_input == "Y":
                    game = "off"
                else:
                    print("Have a nice day!")
                    return False
            else:
                if number < chosen_number:
                    print("You're guessed number is lower than the searched number")
                else:
                    print("You're guessed number is higher than the searched number")


if __name__ == "__main__":
    main()
