# Python: Handling Non-Numeric Data in List Average Calculation

This repository demonstrates a common error in Python when calculating the average of a list: attempting to perform arithmetic operations on a list that contains non-numeric elements.  The `bug.py` file shows the erroneous code. The `bugSolution.py` file provides a corrected version.

## Bug Description

The original code lacks proper input validation.  It doesn't check if all elements in the input list are numeric before performing the calculation. This leads to a `TypeError` when non-numeric data is encountered.

## Solution

The solution involves adding input validation to the `calculate_average` function.  We now check the type of each element and handle any non-numeric values appropriately. 
