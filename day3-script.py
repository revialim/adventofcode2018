#day 3
def getMaxFieldSize(dict):
    max_x_key = 0
    max_y_key = 0
    max_width = 0
    max_height = 0

    for k, v in dict.items():
        if k[0] > max_x_key:
            max_x_key = k[0]
        if k[1] > max_y_key:
            max_y_key = k[1]
        
        if v != None:
            for coord in v:
                if coord[0] > max_width:
                    max_width = coord[0]
                if coord[1] > max_height:
                    max_height = coord[1]
        
        else: 
            print("k, v", k, v)

    #okkkk
    #add max_width, and max_height to max_x and y coord, with 5 padding extra
    return (max_x_key + max_width + 5), (max_y_key + max_height + 5)

def occupiedField(dict, width, height):
    field = [None]*width
    for x in range(0, width):
        field[x] = [0]*height

    # format field = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
    for coord, list_size in dict.items():
        for size in list_size:
            for i in range(0, size[0]):
                for j in range(0, size[1]):
                    field[coord[0] + i][coord[1] + j] += 1

    # print("field test", field[0])
    return field

def overLapsField(occ_field, width, height):
    field = [None]*width
    for x in range(0, width):
        field[x] = [0]*height

    for x in range(0, width):
        for y in range(0, height):
            if occ_field[x][y] > 1:
                field[x][y] = 1
    
    return field

def getAllSum(field):
    all_sum = 0
    for line in field:
        all_sum = all_sum + sum(line)
    return all_sum
    
def start():
    inputs = {}
    with open('./day3.txt') as f:
        for line in f:
            line = line[:(len(line)-1)]
            tmp = line.split('@')
            claim_id = int(tmp[0].replace('#', ''))
            tmp2 = tmp[1].split(':')
            coord = tmp2[0].split(',')
            coord_x = int(coord[0])
            coord_y = int(coord[1])
            size_tmp = tmp2[1].split('x')
            size_x = int(size_tmp[0])
            size_y = int(size_tmp[1])
            size = (size_x, size_y, claim_id)

            if inputs.get((coord_x, coord_y)) == None:
                inputs[(coord_x, coord_y)] = [size] 
            else:
                tmp_list = inputs[(coord_x, coord_y)]
                tmp_list.append(size)
                inputs[(coord_x, coord_y)] = tmp_list

    all_width, all_height = getMaxFieldSize(inputs)
    print('all_width, all_height', all_width, all_height)
    occ_field = occupiedField(inputs, all_width, all_height)
    # part 1
    # over_field = overLapsField(occ_field, all_width, all_height)
    # sumsss = getAllSum(over_field)
    # print("sumsss", sumsss)

    # part 2
    # check all claims
    for k,v in inputs.items():
        # check area of claim
        for size in v:
            tmp_sum = 0
            check_sum = 0
            for x in range(k[0], k[0]+size[0]):
                for y in range(k[1], k[1]+size[1]):
                    tmp_sum = tmp_sum + occ_field[x][y]
                    check_sum = check_sum + 1
            if(tmp_sum == check_sum):
                print("ID, no overlap ", size[2])

start()