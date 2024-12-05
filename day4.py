import numpy as np

def checkHorizontalForwards(puzzle):
    total = 0
    for i in range(137):
        for j in range(140):
            if puzzle[i][j] == 'X':
                if puzzle[i+1][j] == 'M' and puzzle[i+2][j] == 'A' and puzzle[i+3][j] == 'S':
                    total += 1
    return total

def checkHorizontalBackwards(puzzle):
    total = 0
    for i in range(137):
        for j in range(140):
            if puzzle[i][j] == 'S':
                if puzzle[i+1][j] == 'A' and puzzle[i+2][j] == 'M' and puzzle[i+3][j] == 'X':
                    total += 1
    return total

def checkVerticalForwards(puzzle):
    total = 0
    for i in range(140):
        for j in range(137):
            if puzzle[i][j] == 'X':
                if puzzle[i][j+1] == 'M' and puzzle[i][j+2] == 'A' and puzzle[i][j+3] == 'S':
                    total += 1
    return total

def checkVerticalBackwards(puzzle):
    total = 0
    for i in range(140):
        for j in range(137):
            if puzzle[i][j] == 'S':
                if puzzle[i][j+1] == 'A' and puzzle[i][j+2] == 'M' and puzzle[i][j+3] == 'X':
                    total += 1
    return total

def checkDiagonalDownRightForwards(puzzle):
    total = 0
    for i in range(137):
        for j in range(137):
            if puzzle[i][j] == 'X':
                if puzzle[i+1][j+1] == 'M' and puzzle[i+2][j+2] == 'A' and puzzle[i+3][j+3] == 'S':
                    total += 1
    return total

def checkDiagonalDownRightBackwards(puzzle):
    total = 0
    for i in range(137):
        for j in range(137):
            if puzzle[i][j] == 'S':
                if puzzle[i+1][j+1] == 'A' and puzzle[i+2][j+2] == 'M' and puzzle[i+3][j+3] == 'X':
                    total += 1
    return total

def checkDiagonalDownLeftForwards(puzzle):
    total = 0
    for i in range(137):
        for j in range(3, 140):
            if puzzle[i][j] == 'X':
                if puzzle[i+1][j-1] == 'M' and puzzle[i+2][j-2] == 'A' and puzzle[i+3][j-3] == 'S':
                    total += 1
    return total

def checkDiagonalDownLeftBackwards(puzzle):
    total = 0
    for i in range(137):
        for j in range(3, 140):
            if puzzle[i][j] == 'S':
                if puzzle[i+1][j-1] == 'A' and puzzle[i+2][j-2] == 'M' and puzzle[i+3][j-3] == 'X':
                    total += 1
    return total



def checkXofMAS(puzzle):
    total = 0
    for i in range(1, 139):
        for j in range(1, 139):
            if puzzle[i][j] == 'A':
                if puzzle[i-1][j-1] == 'M' and puzzle[i+1][j+1] == 'S' and puzzle[i-1][j+1] == 'M' and puzzle[i+1][j-1] == 'S':
                    total += 1
                elif puzzle[i-1][j-1] == 'M' and puzzle[i+1][j+1] == 'S' and puzzle[i-1][j+1] == 'S' and puzzle[i+1][j-1] == 'M':
                    total += 1
                elif puzzle[i-1][j-1] == 'S' and puzzle[i+1][j+1] == 'M' and puzzle[i-1][j+1] == 'M' and puzzle[i+1][j-1] == 'S':
                    total += 1
                elif puzzle[i-1][j-1] == 'S' and puzzle[i+1][j+1] == 'M' and puzzle[i-1][j+1] == 'S' and puzzle[i+1][j-1] == 'M':
                    total += 1
    return total
    

with open("day4input.txt", "r") as file:
    puzzle = np.array([['.' for i in range(140)] for j in range(140)])
    x = 0
    for line in file:
        y = 0
        for char in line.strip():
            if char not in ['X', 'M', 'A', 'S']:
                puzzle[x][y] = ('.')
            else:
                puzzle[x][y] = (char)
            y += 1
        x += 1
        
    total = 0
    # total += checkHorizontalForwards(puzzle) + checkHorizontalBackwards(puzzle) + checkVerticalForwards(puzzle) + checkVerticalBackwards(puzzle) + checkDiagonalDownRightForwards(puzzle) + checkDiagonalDownRightBackwards(puzzle) + checkDiagonalDownLeftForwards(puzzle) + checkDiagonalDownLeftBackwards(puzzle)
    total = checkXofMAS(puzzle)
    print(total)
    
"""{"@timestamp":"2024-12-04T19:53:15.202Z","log.level": "INFO","message":"The user in the permission request:sai.girap@motorolasolutions.com", "ecs.version": "1.2.0","service.name":"location-provisioning","event.dataset":"location-provisioning","process.thread.name":"http-nio-8080-exec-3","log.logger":"com.msi.ccadmin.services.PermissionService","hostName":"PGFK34-JWN6XHW4VP","msg":"The user in the permission request:sai.girap@motorolasolutions.com","log":{"origin":{"file":{"name":"PermissionService.java","line":95},"function":"getPermissions"}}}
{"@timestamp":"2024-12-04T19:53:15.241Z","log.level": "WARN","message":"Resolved [org.springframework.web.HttpRequestMethodNotSupportedException: Request method 'POST' is not supported]", "ecs.version": "1.2.0","service.name":"location-provisioning","event.dataset":"location-provisioning","process.thread.name":"http-nio-8080-exec-3","log.logger":"org.springframework.web.servlet.mvc.support.DefaultHandlerExceptionResolver","hostName":"PGFK34-JWN6XHW4VP","msg":"Resolved [org.springframework.web.HttpRequestMethodNotSupportedException: Request method 'POST' is not supported]","log":{"origin":{"file":{"name":"AbstractHandlerExceptionResolver.java","line":247},"function":"logException"}}}
"""