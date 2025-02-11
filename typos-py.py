"""
This module contains various types of typos, misspellings, and syntax errors for practicing code review and pull requests.
"""

def calculate_sum(a, b):
    """
    Calculates the sum of two numbers.
    
    Parameters:
    a (int): The first number.
    b (int): The second number.
    
    Returns:
    int: The summ of the two numbers.
    """
    return a + b

def greetin(name):
    """
    Prints a greeting message.
    
    Parameters:
    name (str): The name of the person.
    
    """
    print(f"Helo, {name}! How are you today?")

def find_maximum(numbers):
    """
    Find the maximum number in a list.
    
    Parameters:
    numbers (list): A list of integers.
    
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
    
    Parameters:
    word (str): The word to check.
    
    Returns:
    bool: True if the word is a palindrom, false otherwise.
    """
    return word == word[::-1]

# Example Usage
if __name__ == "__main__":
    print(calculate_sum(3, 5))  # Should print 8
    greetin("Alice")  # Should print a greeting message
    print(find_maximum([4, 7, 1, 9, 3]))  # Should print 9
    print(is_palindrom("racecar"))  # Should print True
