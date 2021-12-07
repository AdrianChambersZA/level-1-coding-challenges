def work_with_two_numbers(number_1, number_2):
    sum_of_numbers = number_1 + number_2
    if (number_1 == 3 or number_2 == 3) and "3" in str(sum_of_numbers):
        return True
    else:
        return False

work_with_two_numbers(3, 131)