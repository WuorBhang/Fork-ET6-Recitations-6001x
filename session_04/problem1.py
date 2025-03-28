# 10/10 points (graded)
# Write a Python function that returns the sum of the pairwise products of listA and listB. You should assume that listA and listB have
# the same length and are two lists of integer numbers. For example, if listA = [1, 2, 3] and listB = [4, 5, 6], the dot product is
# 1*4 + 2*5 + 3*6, meaning your function should return: 32

# Hint: You will need to traverse both lists in parallel.

# This function takes in two lists of numbers and returns a number.

def dotProduct(listA, listB):
    '''
    listA: a list of numbers
    listB: a list of numbers of the same length as listA
    Returns: the sum of the pairwise products of listA and listB
    '''
    # Initialize the sum to 0
    total_sum = 0
    # Traverse both lists using their indices
    for i in range(len(listA)):
        # Multiply corresponding elements and add to sum
        total_sum += listA[i] * listB[i]
    # Return the final sum
    return total_sum
  
# examples
listA = [1, 2, 3]
listB = [4, 5, 6]
result = dotProduct(listA, listB)
print("The dot product is:", result) # Output: 32
