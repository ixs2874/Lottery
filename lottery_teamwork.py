"""
'Powerball Story' program.
Capture the name of the employees entering the numbers.
The first 5 favorite numbers will need to be in the range of 1 to 69 and unique.
6th favorite number will need to be in the range of 1 to 26 and flagged as the 6th Power ball number.
Keep count of each individual favorite number provided to determine which numbers to use in our final winning number.
Retrieve the max count of each unique duplicate number and use them as the Power ball numbers.
If there is a tie based on the max counts randomly select the tied number.
Display all employees with their corresponding number entries.
Display the final Power ball number based on the requirements above

"""
import random

__author__ = "Igor Dean"
__email__ = "igoredean@gmail.com"

class Employee():

    def __init__(self, first, second, numbers, powerball):
        self.first_name = first
        self.second_name = second
        self.numbers = numbers
        self.powerball = powerball

    def get_power_ball(self):
        """Gets power ball
        :return: power ball number
        """

        return self.powerball

    def _get_numbers_as_str(self):
        """Gets lottery numbers as string
        :return: String of lottery numbers
        """

        return ' '.join(str(i) for i in self.numbers)

    def __str__(self):
        """Employee as string
        :return: String representation of an employee
        """

        return "{} {} {} Powerball: {}".format(self.first_name, self.second_name,
                                               self._get_numbers_as_str(), self.powerball)


def get_name():
    """Gets name of the employee from input
    :return: First and second name of the employee
    """

    return input("Enter your first name: "), input("Enter your second name: ")

def get_numbers():
    """Convenience function. Combines two input functions for lottery numbers.
    :return: all entered lottery numbers from one employee
    """

    return capture_numbers(), capture_power_ball()


def capture_numbers(max_limit=69):
    """Gets 5 selected numbers from employee.
    :param max_limit: upper limit of numbers to pick from.
    :return: list of 5 selected numbers.
    """
    numbers = []
    cnt = 1
    while cnt < 6:

        num = input("select {}{} # (1 thru {}{}): ".format(cnt, _num_ending(cnt), max_limit, existing_nums(numbers)))

        if num in numbers:
            print("Error: You entered duplicate number: {}. Please try again.".format(num))
            continue

        if int(num) > max_limit or int(num) < 1:
            print("Error: You entered illegal number: {}. Please try again.".format(num))
            continue

        numbers.append(num)
        cnt += 1

    return numbers


def capture_power_ball(max_limit=26):
    """Gets employee's power ball selection.
    :param max_limit: upper limit.
    :return: power ball number.
    """

    while True:
        num = input("select Power Ball # (1 thru {}): ".format(max_limit))
        if int(num) > max_limit or int(num) < 1:
            print("Error: You entered illegal number: {}. Please try again.".format(num))
            continue
        return num


def _num_ending(num):
    """Returns appropriate strng ending for given number.
   :param num: number to get ending for.
    :return: number ending string.
    """
    switch = {
        1: "st",
        2: "nd",
        3: "rd",
    }
    return switch.get(num, "th")


def existing_nums(nums):
    """Formats a string for existing numbers.
    :param nums: list of numbers.
    :return: formatted string.
    """
    result = ''
    for i, n in enumerate(nums):
        if i == 0:
            result = " excluding " + str(n)
        elif i < len(nums) - 1:
            result += ", " + str(n)
        else:
            result += " and " + str(n) if len(nums) == 2 else ", and " + str(n)
    return result


def get_duplicates(employees):
    """Builds dictionary with a power balls as a key and duplicates count as a value
    :param employees: List of employees to get power balls from
    :return: Dictionary of lottery numbers with counts of duplicates.
    """

    dups_count = {}

    for employee in employees:
        p_ball = employee.get_power_ball()
        if p_ball in dups_count.keys():
            dups_count[p_ball] += 1
        else:
            dups_count[p_ball] = 1
    return dups_count


def calc_and_display_result(employees):
    """Calculate the power ball and print results.
    :param employees: List of employees
    :return: None
    """

    # get count of duplicates
    dups_count = get_duplicates(employees=employees)

    # filter out numbers with max count
    contenders = {k: v for k, v in dups_count.items() if v == max(dups_count.values())}

    # in case of tie randomly pick one power ball number
    the_winner = random.sample(list(contenders.keys()), 1)[0]

    # randomly select 5 numbers from range 1 to 59
    random_5 = random.sample(range(1, 60), 5)

    print()
    print(*employees, sep='\n')
    print("\nPowerball winning number:")
    print("\n{} Powerball: {}\n".format(' '.join(str(n) for n in random_5), the_winner))


def main():

    employees = []  # list of employees with selected lottery numbers

    while True:
        first_name, second_name = get_name()
        numbers, power_ball = get_numbers()
        employees.append(Employee(first=first_name, second=second_name, numbers=numbers, powerball=power_ball))
        if 'y' != input("\nInput next employee? [yes/no] : ")[0]:
            break

    calc_and_display_result(employees)


def test():
    employees = [
        Employee('Wade', 'Wilson', [15,26,33,60,34], 16),
        Employee('Frank', 'Castle', [15,26,34,56,51], 16),
        Employee('Joe', 'Dow', [19, 26, 33, 56, 11], 7),
        Employee('Jim', 'Frizzer', [12, 36, 10, 59, 61], 7),
        Employee('Igor', 'Dean', [12, 3, 4, 45, 46], 9)
    ]
    calc_and_display_result(employees)


import sys
if __name__ == "__main__":

    if len(sys.argv) > 1 and sys.argv[1] == 'test':
        test()
    else:
        main()
