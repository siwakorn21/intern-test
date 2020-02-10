from operator import itemgetter

num = int(input())
result = []
for i in range (num):
    a = input()
    output = ""
    for s in a:
        if (s.isupper()) :
            output += s
    if (len(output) > 0):
         result.append( (-len(output), output) )

result = sorted(result, key=itemgetter(0, 1))

for token in result:
    print(token[1])

