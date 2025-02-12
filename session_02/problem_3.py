"""
Created on Sat Feb  1 19:48:06 2025

@author: somai
Replacing Vowels in a String
Explanation:
We can replace characters in a string using loops and conditional statements. This example replaces all vowels in a string with *.

Instructions:
1. Ask the user to enter a sentence.
2. Replace all vowels (a, e, i, o, u) with *.
3. Print the modified sentence.

"""
# Get user input
sentence = input("Enter a sentence: ")

# Define vowels
vowels = "auioeAUIOE"

# Replace vowels with '*'
new_sentence = ""
for char in sentence:
    if char in vowels:
        new_sentence += "*"
    else:
        new_sentence += char

# Print the modified sentence
print("Modified sentence:", new_sentence)
