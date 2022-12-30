def parse(input):

    with open(input, "r") as input_file:
        file_lines = input_file.readlines()
        input_list = [line.strip() for line in file_lines]
        input_list.append('')

    pair_list = []
    pair = []
    for packet in input_list:
        if packet == '':
            pair_list.append(pair)
            pair = []
        else:
            pair.append(packet)

    return pair_list

def compare(l, r): 

    for i in range(len(l)):
        
        try: # if the values are ints and not lists
            if l[i] < r[i]:
                return True
            elif l[i] > r[i]:
                return False
        
        except IndexError: #left is longer than right
            return False

        except TypeError: #there are lists to compare
            if type(l[i]) == list and type(r[i]) == list:
                l, r = l[i], r[i]
            elif type(l[i]) == int and type(r[i]) == list:
                l, r = [l[i]], r[i]
            elif type(l[i]) == list and type(r[i]) == int:
                l, r = l[i], [r[i]]
            return compare(l, r) #recursive if values are lists

    #if it makes it the whole way through without being out of order,
        #check to see if left is shorter than
    if len(l) < len(r):
        return True
    return False 

def execute(pairs):
    correct_indices = 0 
    for ind, p in enumerate(pairs, 1):
        
        left, right = eval(p[0]), eval(p[1])
        correct_order = compare(left, right)
        if correct_order == True:
            correct_indices += ind
    return print(correct_indices)


inp = parse('input.txt')
execute(inp)


