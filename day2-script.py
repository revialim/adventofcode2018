#day2

def getTwiceThree(str):
    charDict = {}
    for i in range(0, len(str)):
        charDict[str[i]] = charDict.get(str[i]) + 1 if charDict.get(str[i]) != None else 1

    twice = False
    three = False

    for k, v in charDict.items():
        if v == 2:
            twice = True
        if v == 3:
            three = True
    
    return twice, three
    
def findChecksum():
    dict = {"2": 0, "3": 0}

    with open('./day2.txt') as f:
        for line in f:
            line = line.rstrip()
            twice, three = getTwiceThree(line)

            if( twice ):
                dict["2"] = dict["2"] + 1
            if( three ):
                dict["3"] = dict["3"] + 1
            
    print('dict', dict)
    print('checksum', dict["2"] * dict["3"])

def diffByOne(str1, str2):
    # assume str1 and str2 have same length
    diffs = [0] * len(str1)
    for i in range(0, len(str1)):
        if str1[i] != str2[i] : 
            diffs[i] = 1
    if sum(diffs) == 1:
        print("diff is one")
        #build abcde abcce -> abce
        new_str = ""
        for i in range(0, len(str1)):
            if(diffs[i] == 0):
                new_str = new_str + str1[i]
        return new_str
    else:
        return ""

def findCommonChars():
    print("findCommonChars")
    inputs = []
    with open('./day2.txt') as f:
        for line in f:
            inputs.append(line.rstrip())
    
    results = []
    for i in range(0, len(inputs)):
        for j in range(0, len(inputs)):
            if(i != j):
                # print("diffByOne(inputs[", i ,"], inputs[", j ,"])", inputs[i], inputs[j] )
                onediff_str = diffByOne(inputs[i], inputs[j])
                if onediff_str != "":
                    results.append(onediff_str)
    
    # return results
    print(results)

findCommonChars()