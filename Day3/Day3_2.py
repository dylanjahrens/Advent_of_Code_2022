def rucksacks(input):
   
    with open(input, "r") as input_file:
        file_lines = input_file.readlines()
        rucksacks = [line.strip() for line in file_lines]

    groups = []
    group = []
    counter = 0
    for rucksack in rucksacks:
        group.append(rucksack)
        counter +=1
        if counter == 3:
            groups.append(group)
            group = []
            counter = 0

    dup_items = []
    for group in groups:
        for item in group[0]:
            if item in group[1] and item in group[2]:
                dup_items.append(item)
                break
    
    priority_sum = 0
    for item in dup_items:
        if item.isupper():
            value = ord(item) - 38
        else:
            value = ord(item) - 96
        priority_sum += value

    return print(priority_sum)


rucksacks('Day3_input.txt')