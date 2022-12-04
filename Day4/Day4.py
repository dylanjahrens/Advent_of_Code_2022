def overlap(input):
   
    with open(input, "r") as input_file:
        file_lines = input_file.readlines()
        input_list = [line.strip().split(',') for line in file_lines]

    assignment_pairs = 0
    overlaps = 0
    
    for p in input_list:
        overlap = False
        counter = 0
        pair = []
        assignment = [s.split('-') for s in p]
        for rng in assignment:
            begin, end = int(rng[0]), int(rng[1])
            rng = [i for i in range(begin, end+1)]
            pair.append(rng)
        pair.sort(key= len) #sorts shorter ranges first in the pair to compare inclusion
        for i in pair[0]:
            if i in pair[1]:
                counter +=1
                overlap = True
            if counter == len(pair[0]):
                assignment_pairs +=1
        if overlap == True:
            overlaps +=1
    
    return print(assignment_pairs, overlaps)


overlap('Day4_input.txt')