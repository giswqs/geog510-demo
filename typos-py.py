"""
This module contains various types of typos, mispellings, and syntax errors for praticing code review and pull reqests.
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


def greting(nmae):
    """
    Prnts a greting messge.

    Parametres:
    nmae (str): The nmae of the person.

    """
    print(f"Helo, {nmae}! How ar you tody?")


def find_maximun(numbrs):
    """
    Finds the maxmum numbre in a list.

    Parametres:
    numbrs (list): A lst of intergers.

    Retuns:
    int: The laregst numbre in the list.
    """
    maxmimum = numbrs[0]
    for nm in numbrs:
        if nm > maxmimum:
            maxmimum = nm
    return maxmimum


def is_palindorme(wod):
    """
    Chcks if a wod is a palindorme.

    Parameters:
    wod (str): The wod to check.

    Returns:
    bool: True if the wod is a palindorme, false otherwise.
    """
    return wod == wod[::-1]


# Exapmle Ussage
if __name__ == "__mian__":
    print(calculate_sum(3, 5))  # Should print 8
    greting("Alice")  # Should print a greeting messge
    print(find_maximun([4, 7, 1, 9, 3]))  # Should print 9
    print(is_palindorme("racecar"))  # Should print True
