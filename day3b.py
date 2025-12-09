from collections import deque

"""
High-Level Hints
Understand the problem: You need to select exactly 12 digits from each 15-digit sequence to maximize the resulting number. 
Think about which digits you should remove rather than which to keep.

Greedy approach: To maximize the number, you want larger digits toward the left (most significant positions). 
Consider processing the string from left to right and making locally optimal choices.

Key insight: If you need to remove 3 digits from a 15-digit sequence, think about when you should remove a digit to 
make room for a larger digit that comes later.

Python Methods You'll Need
String iteration & indexing: for i in range(len(string)), string[i]
String slicing: string[start:end] to extract portions
List/String building: Consider using a list or deque to build your result, or str.join()
Comparison operators: >, < to compare digit values
Type conversion: int() and str() to convert between numbers and strings
File I/O: open(), .readlines(), or .read() to load your input
Aggregation: sum() to add up your final results
Collections module: collections.deque might be useful for an efficient algorithm

Python method you need:

deque.pop() - to remove from the end of your stack
deque.append() - to add to the end
stack[-1] - to peek at the last element

Algorithm Strategy

Think about using a stack-based or sliding window approach: as you iterate through each digit, 
decide whether to keep it or remove previously selected digits if a larger digit appears.
"""

data = """
987654321111111
811111111111119
234234234234278
818181911112111
"""

challengeInput = data.strip().split('\n'); 
total = 0
largestDigits = []

def findLargestDigit(input): 
    largestDigit = input[0]
    for i in range(1, len(input)):
        if input[i] > largestDigit: 
            largestDigit = input[i]
    return largestDigit

for line in input: 
    for i in line: 
        largestDigit = findLargestDigit(line) 

    largestDigits.append(largestDigit)
