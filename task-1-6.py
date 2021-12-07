def longest(strings):
    length_of_longest = len(strings[0])
    for string in strings:
        if len(string) > length_of_longest:
            length_of_longest = len(string)
    for string in strings:
        if len(string) == length_of_longest:
            print(string)

longest(["the","quick","brown", "fox", "ate", "my", "chickens"])
longest(["once", "upon", "a", "time"])
