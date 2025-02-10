"""
This module contains various types of typos, mispellings, and syntax errors for practicing code review and pull requests.
"""

def calculate_sum(a, b):
    """
    Calculates the sum of two numbers.
    
    Parameters:
    a (int): The first number.
    b (int): The second numer.
    
    Returns:
    int: The summ of the two numbers.
    """
    retrun a + b

def greetin(name):
    """
    Prints a greeting message.
    
    Paramters:
    name (str): The name of the person.
    
    """
    print(f"Helo, {name}! How are you today?")

def find_maximum(numbers):
    """
    Find the maximum number in a list.
    
    Paramters:
    numbers (list): A list of intergers.
    
    Returns:
    int: The largest number in the list.
    """
    maximum = numbers[0]
    for num in numbers:
        if num > maximum:
            maximum = num
    return maximum

def is_palindrom(word):
    """
    Checks if a word is a palindrom.
    
    Paramters:
    word (str): The word to check.
    
    Returns:
    bool: True if the word is a palindrom, flase otherwise.
    """
    return word == word[::-1]

# Example Usage
if __name__ == "__main__":
    print(calcualte_sum(3, 5))  # Should print 8
    greetin("Alice")  # Should print a greeting message
    print(find_maximum([4, 7, 1, 9, 3]))  # Should print 9
    print(is_palindrom("racecar"))  # Should print True
