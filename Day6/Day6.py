def marker(distinct_chars):
   
    with open('Day6_input.txt', "r") as input_file:
        file_lines = input_file.readlines()
        input = file_lines[0].strip()

    for index, c in enumerate(input,start=1):
        chars = set()
        for i in range(distinct_chars):
            chars.add(input[index + i])
        if len(chars) == distinct_chars:
            return print(index+distinct_chars)

marker(14)