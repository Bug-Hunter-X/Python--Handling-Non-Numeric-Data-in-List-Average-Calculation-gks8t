def calculate_average(numbers):
    numeric_numbers = [num for num in numbers if isinstance(num, (int, float))]
    if not numeric_numbers:
        return 0  # Handle empty list after removing non-numeric elements
    total = sum(numeric_numbers)
    average = total / len(numeric_numbers)
    return average

my_list = [10, 20, 30, 40, 50]
print(calculate_average(my_list)) #this will run

my_list = []
print(calculate_average(my_list)) #this will run

my_list = [10,20,'a',40,50]
print(calculate_average(my_list)) #this will run without error