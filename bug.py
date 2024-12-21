def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list
    total = sum(numbers)
    average = total / len(numbers)
    return average

my_list = [10, 20, 30, 40, 50]
print(calculate_average(my_list)) #this will run

my_list = []
print(calculate_average(my_list)) #this will run

my_list = [10,20,'a',40,50]
print(calculate_average(my_list)) #this will cause an error