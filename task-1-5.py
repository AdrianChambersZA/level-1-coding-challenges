def triangle(input_number):
    if input_number < 0:
        number = input_number * -1
        while number > 0:
            line_to_print = "#" * number
            print(line_to_print)
            number -= 1
    else:
        line_to_print = ""
        for number in range(input_number):
            line_to_print += "#"
            print(line_to_print)

triangle(-9)