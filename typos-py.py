"""
This module contains various types of typos, misspellings, and syntax errors for praticing code review and pull requests.
"""


def calculate_sum(a, b):
    """
    Calculates the sum of two numbers.

    Parameters:
    a (int): The first number.
    b (int): The second number.

    Returns:

    int: The sum of the two numbers.
    """
    return a + b


def greeting(name):
    """
    Prints a greeting message.

    Parameters:
    name (str): The name of the person.

    """
    print(f"Hello, {name}! How are you today?")


def find_maximum(numbers):
    """
    Finds the maximum number in a list.

    Parameters:
    numbers (list): A list of integers.

    Returns:
    int: The largest number in the list.
    """
    maximum = numbers[0]
    for nm in numbers:
        if nm > maximum:
            maximum = nm
    return maximum


def is_palindorme(wod):
    """
    Checks if a word is a palindorme.

    Parameters:
    wod (str): The wod to check.

    Returns:
    bool: True if the wod is a palindorme, false otherwise.
    """
    return wod == wod[::-1]


# Example Usage
if __name__ == "__mian__":
    print(calculate_sum(3, 5))  # Should print 8
    greeting("Alice")  # Should print a greeting message
    print(find_maximum([4, 7, 1, 9, 3]))  # Should print 9
    print(is_palindorme("racecar"))  # Should print True
