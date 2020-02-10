def printList(data):
    output = ""
    for token in data:
        if (token == None):
            output += "_ "
        else :
            output += str(token) + " "
    print(output)

data = [int(x) for x in input().split()]
output_list = [None] * len(data)
myScore = 0

inputData = []
for i in range(5):
    n = int(input())
    inputData += [n]

for i in range(5):
    printList(output_list)
    isInlist = False
    for j in range(len(data)):
        if (inputData[i] == data[j]):
            output_list[j] = inputData[i]
            myScore += 1
            isInlist = True
    if (not isInlist):
        output_list += [inputData[i]]



printList(output_list)
print(myScore)
