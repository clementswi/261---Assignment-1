
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
    Checks if a StaticArray is sorted in strictly ascending or descending order.

    Args:
        arr (StaticArray): The StaticArray object to check.

    Returns:
        int: 1 if the array is sorted in strictly ascending order,
             -1 if the array is sorted in strictly descending order,
             0 otherwise.
    """

    if arr.length() == 1:
        return 1

        # Check if array is sorted in ascending order
    if all(arr.get(i) <= arr.get(i + 1) for i in range(arr.length() - 1)):
        return 1

        # Check if array is sorted in descending order
    elif all(arr.get(i) >= arr.get(i + 1) for i in range(arr.length() - 1)):
        return -1

        # Array is not sorted
    else:
        return 0

def find_mode(arr: StaticArray) -> tuple[object, int]:
    """
    Find the mode (most-occurring element) and its frequency in a sorted StaticArray.

    Args:
        arr (StaticArray): The StaticArray object to check.

    Returns:
        tuple[object, int]: A tuple of the mode of the array and its frequency.
    """
    length = arr.length()

    # Initialize variables for tracking the mode and frequency
    mode = arr.get(0)
    frequency = 1
    current_element = arr.get(0)
    current_frequency = 1

    # Iterate through the array
    for i in range(1, length):
        element = arr.get(i)

        # If the current element is the same as the previous one, increase its frequency
        if element == current_element:
            current_frequency += 1
        else:
            # If the frequency of the current element is higher than the mode's frequency,
            # update the mode and its frequency
            if current_frequency > frequency:
                mode = current_element
                frequency = current_frequency

            # Reset the current element and its frequency for the new element
            current_element = element
            current_frequency = 1

    # Check the frequency of the last element
    if current_frequency > frequency:
        mode = current_element
        frequency = current_frequency

    return mode, frequency

def remove_duplicates(arr: StaticArray) -> StaticArray:
    """
    Removes duplicate values from a sorted StaticArray and returns a new StaticArray
    without modifying the original array.

    Args:
        arr (StaticArray): The sorted StaticArray object.

    Returns:
        StaticArray: A new StaticArray object without duplicate values.
    """
    length = arr.length()

    # Calculate the maximum possible size of the new array
    max_size = length
    for i in range(1, length):
        if arr.get(i) == arr.get(i - 1):
            max_size -= 1

    # Create a new StaticArray with the maximum possible size
    new_arr = StaticArray(max_size)

    # Copy the non-duplicate elements to the new array
    new_index = 0
    new_arr.set(new_index, arr.get(0))
    new_index += 1
    for i in range(1, length):
        if arr.get(i) != arr.get(i - 1):
            new_arr.set(new_index, arr.get(i))
            new_index += 1

    return new_arr

def count_sort(arr: StaticArray) -> StaticArray:
    """
    Sorts the content of a StaticArray in non-ascending order using the Count Sort algorithm
    and returns a new StaticArray without modifying the original array.

    Args:
        arr (StaticArray): The StaticArray object to be sorted.

    Returns:
        StaticArray: A new StaticArray object with the content sorted in non-ascending order.
    """
    length = arr.length()

    # Find the minimum and maximum values in the array
    min_val = arr.get(0)
    max_val = arr.get(0)
    for i in range(length):
        current_value = arr.get(i)
        if current_value < min_val:
            min_val = current_value
        elif current_value > max_val:
            max_val = current_value

    # Create a count array to store the frequency of each element in the input array
    count_len = max_val - min_val + 1
    count = StaticArray(count_len)
    for i in range(length):
        current_value = arr.get(i)
        count_index = current_value - min_val
        count_value = count.get(count_index)
        count.set(count_index, count_value + 1)

    # Compute the length of the output array
    output_len = sum(count)

    # Create a new output array
    output = StaticArray(output_len)

    # Generate the sorted output array
    output_index = 0
    for i in range(count_len):
        count_value = count.get(i)
        while count_value > 0:
            output.set(output_index, i + min_val)
            output_index += 1
            count_value -= 1

    return output

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
