inputs = []
with open('./day1.txt') as input_f:
    for line in input_f:
        inputs.append(int(line.rstrip()))

#print("inputs[:10]", inputs[:10])
#print("len(inputs)", len(inputs))

answer = sum(inputs)

all_sums = set()
i=0
while(True):
    current_sum = sum(inputs[0:i+1])
    
    if current_sum in all_sums:
        answer2 = current_sum
        break

    all_sums.add(current_sum)
    i = (i + 1)%len(inputs)


print("Answer day 1 1:", answer)
#print("all_sums ", all_sums)
print("Answer day 1 2:", answer2)