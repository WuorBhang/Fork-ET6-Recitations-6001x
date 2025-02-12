"""
Created on Mon Feb  10 20:14:40 2025

@author: somai
Bisection Search for a Threshold Value in a Numeric String
Explanation:
Bisection search is not just for characters—it can also help find values in ordered data.

Given a sorted string of numeric values, we can efficiently find the smallest number ≥ a given threshold.
Instead of checking every number one by one (O(n)), we use bisection search (O(log n)) to quickly narrow down the search space.
Instructions:
Create a variable sorted_numbers with the value "134789" (a sorted sequence of numeric characters).
Create a function find_threshold_bisection(sorted_nums, threshold) that searches for the smallest number ≥ threshold using bisection search.
Inside the function, define low as 0 (first index) and high as len(sorted_nums) - 1 (last index).
Use a while loop to repeatedly:
Find the middle index (mid = (low + high) // 2).
If sorted_nums[mid] >= threshold, store it as result and move left (high = mid - 1)` to find a smaller valid number.
Otherwise, move right (low = mid + 1).
If no valid number is found, return -1.
Call the function with sorted_numbers = "134789" and test with different thresholds ("5", "7", "2", "8").

#Test Cases:
print(find_threshold_bisection("134789", "5"))  # Output: 7  
print(find_threshold_bisection("2345679", "3"))  # Output: 3  
print(find_threshold_bisection("2345679", "8"))  # Output: -1  
"""
def find_threshold_bisection(sorted_nums, threshold):
    """Finds the smallest number ≥ threshold in a sorted string of numeric values using bisection search."""
    low = 0
    high = len(sorted_nums) - 1
    result = -1  # Default result if no valid number is found

    while low <= high:
        mid = (low + high) // 2  # Calculate the middle index
        mid_value = sorted_nums[mid]  # Get the character at the middle index

        if mid_value >= threshold:
            result = mid_value  # Store the current value as a candidate
            high = mid - 1  # Move left to find a smaller valid number
        else:
            low = mid + 1  # Move right to search for a larger number

    return int(result) if result != -1 else -1  # Convert the result to an integer if found, otherwise return -1

# Test cases
print(find_threshold_bisection("134789", "5"))  # Output: 7
print(find_threshold_bisection("2345679", "3"))  # Output: 3
print(find_threshold_bisection("2345679", "8"))  # Output: -1
