import re

def lineSum(line, do):
    if not do:
        return 0
    matches = re.findall(r'mul\((\d+),(\d+)\)', line)
    sum = 0
    for match in matches:
        sum += int(match[0]) * int(match[1])
    return sum

with open("day3input.txt", "r") as file:
    total = 0
    do = True
    for line in file:
        while line != "":
            doIndex = line.find("do()")
            dontIndex = line.find("don't()")
            if doIndex != -1 and dontIndex != -1:
                if doIndex < dontIndex:
                    total += lineSum(line[:doIndex], do)
                    do = True
                    total += lineSum(line[doIndex + 4:dontIndex], do)
                    line = line[dontIndex + 7:]
                    do = False
                else:
                    total += lineSum(line[:dontIndex], do)
                    line = line[doIndex + 4:]
                    do = True
            elif doIndex != -1:
                total += lineSum(line[:doIndex], do)
                line = line[doIndex + 4:]
                do = True
            elif dontIndex != -1:
                total += lineSum(line[:dontIndex], do)
                line = line[dontIndex + 7:]
                do = False
            else:
                total += lineSum(line, do)
                line = ""
                
    print(total)
        