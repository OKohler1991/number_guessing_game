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
            if number not in range(number_lower, number_higher + 1):
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
        chosen_number = guess_number()
        print(chosen_number)
        player_number = input(
            f"Please enter a number between {number_lower} and {number_higher}: "
        )
        number = number_in_range(player_number)
        if number == chosen_number:
            pass
            # TODO: Text + question to play a new game or end game
        else:
            if number < chosen_number:
                pass
            else:
                pass


if __name__ == "__main__":
    main()
