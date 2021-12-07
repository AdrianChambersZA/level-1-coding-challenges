def work_with_two_numbers(number_1, number_2):
    sum_of_numbers = number_1 + number_2
    if (number_1 == 65 or number_2 == 65) or sum_of_numbers == 65:
        return True
    else:
        return False

work_with_two_numbers(11, 55)