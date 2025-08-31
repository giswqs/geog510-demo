"""
This module contains various types of typos, misspellings, and syntax errors for praticing code review and pull requests.
"""

from typing import Optional


def calculate_sum(a: int, b: int) -> int:
    """
    Calculates the sum of two numbers.

    Parameters:
    a (int): The first number.
    b (int): The second number.

    Returns:

    int: The sum of the two numbers.
    """
    return a + b


def greeting(name: str) -> None:
    """
    Prints a greeting message.

    Parameters:
    name (str): The name of the person.

    """
    print(f"Hello, {name}! How are you today?")


def find_maximum(numbers: list[int]) -> Optional[int]:
    """
    Finds the maximum number in a list.

    Parameters:
    numbers (list): A list of integers.

    Returns:
    int: The largest number in the list.
    """
    if not numbers:
        print("The list is empty.")
        return None

    return max(numbers)


def is_palindorme(word: str) -> str:
    """
    Checks if a word is a palindorme.

    Parameters:
    word (str): The word to check.

    Returns:
    bool: True if the word is a palindorme, false otherwise.
    """
    return word == word[::-1]


# Example Usage
if __name__ == "__main__":
    print(calculate_sum(3, 5))  # Should print 8
    greeting("Alice")  # Should print a greeting message
    print(find_maximum([4, 7, 1, 9, 3]))  # Should print 9
    print(find_maximum([]))  # Should print None
    print(is_palindorme("racecar"))  # Should print True
