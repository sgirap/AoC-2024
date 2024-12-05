
with open("day1input.txt", "r") as file:
    first = []
    second = []
    for line in file:
        tokens = line.strip().split()
        first.append(int(tokens[0]))
        second.append(int(tokens[1]))
        
    first.sort()
    second.sort()
    
    distance = 0
    for i in range(len(first)):
        distance += abs(first[i] - second[i])
        
    similarity = 0
    for i, num in enumerate(set(first)):
        currSimilarity = 0
        found = False
        for j, num2 in enumerate(second):
            if num == num2:
                currSimilarity += 1
                found = True
            if num != num2 and found:
                break
        
        currSimilarity *= num
        similarity += currSimilarity
                
        
        
    print(distance)
    print(similarity)
