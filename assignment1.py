
# Name:William Clements
# OSU Email:clementsw@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment:1
# Due Date:7/11/23
# Description:Various methods such as sort and min max for a given static array class


import random
from static_array import *

def min_max(arr: StaticArray) -> tuple[int, int]:
    """
    Takes a one-dimensional array of integers and returns a Python
    tuple with two values - the minimum and maximum values of the input array.
    Assumes the input array contains only integers and at least one element.

    Args:
        arr (StaticArray): The StaticArray object to find the minimum and maximum values from.

    Returns:
        A tuple of the minimum and maximum values found in the StaticArray."""

    # Initialize the minimum and maximum values as the first element in the array
    min_value = arr.get(0)
    max_value = arr.get(0)

    # Iterate through the array, comparing the current minimum and maximum values to each element
    for i in range(1, arr.length()):
        element = arr.get(i)
        if element < min_value:
            min_value = element
        elif element > max_value:
            max_value = element

    return min_value, max_value

def fizz_buzz(arr: StaticArray) -> StaticArray:
    """
    receives a StaticArray of integers and returns a new StaticArray object
    with the content of the original array, modified as follows:
    1) If the number in the original array is divisible by 3, the corresponding element in the
    new array will be the string ‘fizz’.
    2) If the number in the original array is divisible by 5, the corresponding element in the
    new array will be the string ‘buzz’.
    3) If the number in the original array is both a multiple of 3 and a multiple of 5, the
    corresponding element in the new array will be the string ‘fizzbuzz’.
    4) In all other cases, the element in the new array will have the same value as in the
    original array."""

    new_arr = StaticArray(arr.length())

    for i in range(arr.length()):
        element = arr.get(i)
        if element % 3 == 0 and element % 5 == 0:
            new_arr.set(i, "fizzbuzz")
        elif element % 3 == 0:
            new_arr.set(i, "fizz")
        elif element % 5 == 0:
            new_arr.set(i, "buzz")
        else:
            new_arr.set(i, element)

    return new_arr

def reverse(arr: StaticArray) -> None:
    """receives a StaticArray and reverses the order of the elements in the array.

        Args: arr (StaticArray): The StaticArray object to reverse.

        Returns: None"""

    for i in range(0, arr.length() // 2):
        temp = arr.get(i)
        #temp represents the current element in the array that will be swapped to its opposing index in the lines below
        arr.set(i, arr.get(arr.length() - i - 1))
        arr.set(arr.length() - i - 1, temp)


def rotate(arr: StaticArray, steps: int) -> StaticArray:
    """
    Rotate the elements of a StaticArray and return a new rotated StaticArray.

    Parameters:
        arr (StaticArray): The original array to be rotated.
        steps (int): The number of steps to rotate the elements.
                     Positive integer for right rotation, negative for left rotation.

    Returns:
        StaticArray: A new StaticArray with the rotated elements.
    """
    # Create a new StaticArray with the same size as the original array
    rotated_array = StaticArray(arr.length())

    # Calculate the effective number of steps (taking modulo of the array length)
    effective_steps = steps % arr.length()

    # Copy the elements from the original array to the rotated array
    for i in range(arr.length()):
        # Calculate the new index for each element based on the rotation direction
        new_index = (i + effective_steps) % arr.length()

        # Set the element at the new index in the rotated array
        rotated_array.set(new_index, arr.get(i))

    # Return the rotated array
    return rotated_array


def sa_range(start: int, end: int) -> StaticArray:
    """
    Create a StaticArray containing consecutive integers between start and end (inclusive).

    Args:
        start (int): The starting integer.
        end (int): The ending integer.

    Returns:
        StaticArray: A StaticArray object that contains all the consecutive integers between start and end.
    """
    # Calculate the size of the StaticArray based on the range
    size = end - start + 1 if end >= start else start - end + 1

    # Create a new StaticArray with the calculated size
    arr = StaticArray(size)

    # Determine the step direction based on the range
    step = 1 if end > start else -1

    # Fill the StaticArray with consecutive integers
    for i in range(size):
        arr.set(i, start)
        start += step

    # Return the StaticArray
    return arr


def is_sorted(arr: StaticArray) -> int:
    """
    Check if a StaticArray is sorted and return an integer describing the order.

    Args:
        arr (StaticArray): The StaticArray object to check.

    Returns:
        int: An integer that describes whether the array is sorted.
             1 if the array is sorted in strictly ascending order,
             -1 if the array is sorted in strictly descending order,
             0 otherwise.
    """
    length = arr.length()

    # Check for ascending order
    is_ascending = True
    for i in range(1, length):
        if arr.get(i) < arr.get(i - 1):
            is_ascending = False
            break

    if is_ascending:
        return 1

    # Check for descending order
    is_descending = True
    for i in range(1, length):
        if arr.get(i) > arr.get(i - 1):
            is_descending = False
            break

    if is_descending:
        return -1

    # The array is not sorted
    return 0

def find_mode(arr: StaticArray) -> tuple[object, int]:
    """
    receives a StaticArray that is sorted in either non-descending or
    non-ascending order. The function will return the mode (the most-occurring element) of the
    array and its frequency (how many times it appears).
    If there is more than one element that has the highest frequency, select the one that occurs
    first in the array.

    Args:
        arr (StaticArray): The StaticArray object to check.

    Returns:
        tuple[object, int]: A tuple of the mode of the array and its frequency.

    """

    max_count = 0
    mode = arr.get(0)
    for i in range(1, arr.length()):
        count = 1
        while i < arr.length() - 1 and arr.get(i) == arr.get(i + 1):
            count += 1
            i += 1

        if count > max_count:
            max_count = count
            mode = arr.get(i - 1)

    return mode, max_count

def remove_duplicates(arr: StaticArray) -> StaticArray:
    """
    Removes duplicate values from a sorted StaticArray and returns a new StaticArray
    without modifying the original array.

    Args:
        arr (StaticArray): The sorted StaticArray object.

    Returns:
        StaticArray: A new StaticArray object without duplicate values.
    """
    size = arr.length()  # Get the size of the input array
    if size <= 1:
        return arr  # If the array has 0 or 1 element, there are no duplicates

    unique_values = []  # List to store unique values
    prev_value = arr.get(0)  # Initialize the previous value with the first element

    # Iterate over the array starting from the second element
    for i in range(1, size):
        current_value = arr.get(i)  # Get the current value

        if current_value != prev_value:
            unique_values.append(current_value)  # Add unique values to the list
            prev_value = current_value  # Update the previous value

    # Create a new StaticArray with the unique values
    result = StaticArray(len(unique_values))
    for i, value in enumerate(unique_values):
        result.set(i, value)

    return result

def count_sort(arr: StaticArray) -> StaticArray:
    """
    Sorts the content of a StaticArray in non-ascending order using the Count Sort algorithm
    and returns a new StaticArray without modifying the original array.

    Args:
        arr (StaticArray): The StaticArray object to be sorted.

    Returns:
        StaticArray: A new StaticArray object with the content sorted in non-ascending order.
    """
    size = arr.length()  # Get the size of the input array

    # Find the maximum value in the array
    max_value = float('-inf')
    for i in range(size):
        value = arr.get(i)
        if value > max_value:
            max_value = value

    # Create a count array with size = max_value + 1
    count = StaticArray(max_value + 1)

    # Count the occurrences of each value in the input array
    for i in range(size):
        value = arr.get(i)
        count.set(value, count.get(value) + 1)

    # Modify the count array to store the starting position of each value in the sorted array
    for i in range(1, max_value + 1):
        count.set(i, count.get(i) + count.get(i - 1))

    # Create a new StaticArray to store the sorted elements
    sorted_arr = StaticArray(size)

    # Populate the sorted array by iterating the input array in reverse order
    for i in range(size - 1, -1, -1):
        value = arr.get(i)
        count_value = count.get(value)
        sorted_arr.set(count_value - 1, value)
        count.set(value, count_value - 1)

    return sorted_arr

def sorted_squares(arr: StaticArray) -> StaticArray:
    """
    Squares the values of a StaticArray in sorted order and returns a new StaticArray
    with the squared values sorted in non-descending order. The original array is not modified.

    Args:
        arr (StaticArray): The sorted StaticArray object.

    Returns:
        StaticArray: A new StaticArray object with the squared values sorted in non-descending order.
    """
    size = arr.length()  # Get the size of the input array

    # Find the index of the first non-negative value in the input array
    first_non_negative = 0
    while first_non_negative < size and arr.get(first_non_negative) < 0:
        first_non_negative += 1

    # Create two pointers: one for negative values and one for non-negative values
    neg_ptr = first_non_negative - 1
    non_neg_ptr = first_non_negative
    result = StaticArray(size)  # Create a new StaticArray to store the squared values

    # Merge the squared values in non-descending order
    for i in range(size):
        if neg_ptr >= 0 and non_neg_ptr < size:
            neg_value = arr.get(neg_ptr)
            non_neg_value = arr.get(non_neg_ptr)
            if abs(neg_value) < non_neg_value:
                result.set(i, neg_value * neg_value)
                neg_ptr -= 1
            else:
                result.set(i, non_neg_value * non_neg_value)
                non_neg_ptr += 1
        elif neg_ptr >= 0:
            result.set(i, arr.get(neg_ptr) * arr.get(neg_ptr))
            neg_ptr -= 1
        else:
            result.set(i, arr.get(non_neg_ptr) * arr.get(non_neg_ptr))
            non_neg_ptr += 1

    return result
