import re

def checkPages(rules, pages):
    for rule in rules:
        first = rule[0]
        second = rule[1]
        
        if first not in pages or second not in pages:
            continue
        
        firstIndex = pages.index(first)
        secondIndex = pages.index(second)
        if firstIndex < secondIndex:
            continue
        else:
            return -1
    return pages[int(len(pages)/2)]

def fixPages(rules, pages):
    while checkPages(rules, pages) < 1:
        for rule in rules:
            first = rule[0]
            second = rule[1]
            
            if first not in pages or second not in pages:
                continue
            
            firstIndex = pages.index(first)
            secondIndex = pages.index(second)
            if firstIndex < secondIndex:
                continue
            else:
                temp = pages[firstIndex]
                pages[firstIndex] = pages[secondIndex]
                pages[secondIndex] = temp
    return pages[int(len(pages)/2)]

with open("day5input.txt", "r") as file:
    total = 0
    total2 = 0
    rules = []
    for line in file:
        match = re.findall(r'(\d+)\|(\d+)', line.strip())
        if match != []:
            rules.append((int(match[0][0]), int(match[0][1])))
        else:
            break
        
    for line in file:
        pages = line.strip().split(',')
        pages = [int(page) for page in pages]
        toAdd = checkPages(rules, pages)
        if toAdd != -1:
            total += toAdd
        else:
            total2 += fixPages(rules, pages)
    
    print(total)
    print(total2)