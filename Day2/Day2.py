def strategy_guide():
   
    with open("Day2_input.txt", "r") as input_file:
        file_lines = input_file.readlines()
        input_list = [line.strip().split(' ') for line in file_lines]

    total_score = 0

    for round in input_list:
        if round[1] == 'X':
            total_score +=1
            if round[0] == 'A':
                total_score += 3
            elif round[0] == 'B':
                total_score += 0
            elif round[0] == 'C':
                total_score += 6
        elif round[1] == 'Y':
            total_score +=2
            if round[0] == 'A':
                total_score += 6
            elif round[0] == 'B':
                total_score += 3
            elif round[0] == 'C':
                total_score += 0
        elif round[1] == 'Z':
            total_score +=3
            if round[0] == 'A':
                total_score += 0
            elif round[0] == 'B':
                total_score += 6
            elif round[0] == 'C':
                total_score += 3
    
    print(total_score)


strategy_guide()