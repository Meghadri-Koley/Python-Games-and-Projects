import os
import copy
import random

#PRINTING THE BOARD
def board(arr):
    print()
    print()
    for i in range(4):
        if(arr[0][i] == 0):
            print("_", end = '\t')
        else:
            print((str(arr[0][i])), end='\t')
    print()
    print()
    for i in range(4):
        if(arr[1][i] == 0):
            print("_", end = '\t')
        else:
            print((str(arr[1][i])), end='\t')
    print()
    print()
    for i in range(4):
        if(arr[2][i] == 0):
            print("_", end = '\t')
        else:
            print((str(arr[2][i])), end='\t')
    print()
    print()
    for i in range(4):
        if(arr[3][i] == 0):
            print("_", end = '\t')
        else:
            print((str(arr[3][i])), end='\t')
    print()
    print()


#CHECK IF BOARD IS FULL
def isFull(arr):
    c = 0
    for i in range(4):
        for j in range(4):
            if arr[i][j] == 0:
                c = 1
                break
        if c == 1:
            break
        
    if(c == 0):
        return True
    else:
        return False


#CHECHKING IF 2048 IS PRESENT
def chck(arr):
    flag = 0
    for i in range(4):
        for j in range(4):
            if arr[i][j] == 2048:
                flag = 1
                break
        if flag == 1:
            break
    
    if(flag == 1):
        return True
    else:
        return False

#YOU WIN
def win():
    print("\nCongratulations!!! You have won!\n")
    os._exit(0)

#YOU LOSS
def loss():
    print("\nYou lost!\n")
    os._exit(0)
    

#FIND FREE SPACES
def find_free(arr):
    c = 0
    l = []
    for i in range(4):
        for j in range(4):
            if arr[i][j] == 0:
                l.append(c)
            c = c+1
    space = random.choice(l)
    num = random.choice([int(2), int(4)])
    return num, space


#ADD RANDOM 2/4 IN FREE SPACES
def adding(arr, space, num):
    c = 0
    for i in range(4):
        for j in range(4):
            if space == c:
                arr[i][j] = num
            c = c+1
    return arr


#POST MOVEMENT CHECKS
def post_movement(arr, l):
    ch = chck(arr)
    if ch == True:
        win()
    
    ch = isFull(arr)
    if ch == True:
        loss()
    
    if(l == arr):
        board(arr)
    else:
        num, space = find_free(arr)
        arr = adding(arr, space, num)
        board(arr)
    inp(arr)    

 
#MOVE LEFT
def left(arr):
    l = copy.deepcopy(arr)
    for i in range(4):
        lst = [0,0,0,0]
        c = 0
        
        for j in range(3):
            if arr[i][j] == 0:
                arr[i][j] = arr[i][j+1]
                arr[i][j+1] = 0
        for j in range(3):
            if arr[i][j] == 0:
                arr[i][j] = arr[i][j+1]
                arr[i][j+1] = 0
                
        for j in range(3):
            if arr[i][j] == 0:
                continue
            elif arr[i][j] == arr[i][j+1] and arr[i][j] != 0:
                lst[c] = 2*arr[i][j]
                c = c+1
                arr[i][j] = arr[i][j+1] = 0
            elif arr[i][j] != arr[i][j+1]:
                lst[c] = arr[i][j]
                c = c+1
                arr[i][j] = 0
        
        if arr[i][3] != 0:
            lst[c] = arr[i][3]
            arr[i][3] = 0       
        arr[i] = lst
    
    post_movement(arr, l)

    
#MOVE RIGHT
def right(arr):
    l = copy.deepcopy(arr)
    for i in range(4):
        lst = [0,0,0,0]
        c = 3
        
        for j in [3, 2, 1]:
            if arr[i][j] == 0:
                arr[i][j] = arr[i][j-1]
                arr[i][j-1] = 0
        for j in [3, 2, 1]:
            if arr[i][j] == 0:
                arr[i][j] = arr[i][j-1]
                arr[i][j-1] = 0
                
        for j in [3, 2, 1]:
            if arr[i][j] == 0:
                continue
            elif arr[i][j] == arr[i][j-1] and arr[i][j] != 0:
                lst[c] = 2*arr[i][j]
                c = c-1
                arr[i][j] = arr[i][j-1] = 0
            elif arr[i][j] != arr[i][j-1]:
                lst[c] = arr[i][j]
                c = c-1
                arr[i][j] = 0
        
        if arr[i][0] != 0:
            lst[c] = arr[i][0]
            arr[i][0] = 0       
        arr[i] = lst
    
    post_movement(arr, l)
    
    
#MOVE UP
def up(arr):
    l = copy.deepcopy(arr)
    for i in range(4):
        lst = [0,0,0,0]
        c = 0
        
        for j in range(3):
            if arr[j][i] == 0:
                arr[j][i] = arr[j+1][i]
                arr[j+1][i] = 0
        for j in range(3):
            if arr[j][i] == 0:
                arr[j][i] = arr[j+1][i]
                arr[j+1][i] = 0
                
        for j in range(3):
            if arr[j][i] == 0:
                continue
            elif arr[j][i] == arr[j+1][i] and arr[j][i] != 0:
                lst[c] = 2*arr[j][i]
                c = c+1
                arr[j][i] = arr[j+1][i] = 0
            elif arr[j][i] != arr[j+1][i]:
                lst[c] = arr[j][i]
                c = c+1
                arr[j][i] = 0
        
        if arr[3][i] != 0:
            lst[c] = arr[3][i]
            arr[3][i] = 0       
        for j in range(4):
            arr[j][i] = lst[j]
    
    post_movement(arr, l)
    

#MOVE DOWN
def down(arr):
    l = copy.deepcopy(arr)
    for i in range(4):
        lst = [0,0,0,0]
        c = 3
        
        for j in [3, 2, 1]:
            if arr[j][i] == 0:
                arr[j][i] = arr[j-1][i]
                arr[j-1][i] = 0
        for j in [3, 2, 1]:
            if arr[j][i] == 0:
                arr[j][i] = arr[j-1][i]
                arr[j-1][i] = 0
                
        for j in [3, 2, 1]:
            if arr[j][i] == 0:
                continue
            elif arr[j][i] == arr[j-1][i] and arr[j][i] != 0:
                lst[c] = 2*arr[j][i]
                c = c-1
                arr[j][i] = arr[j-1][i] = 0
            elif arr[j][i] != arr[j-1][i]:
                lst[c] = arr[j][i]
                c = c-1
                arr[j][i] = 0
        
        if arr[0][i] != 0:
            lst[c] = arr[0][i]
            arr[0][i] = 0       
        for j in range(4):
            arr[j][i] = lst[j]
    
    post_movement(arr, l)
    
    

#INPUT
def inp(arr):
    ch = input()
    if(ch == 'L' or ch == 'l'):
        left(arr)
    elif(ch == 'R' or ch == 'r'):
        right(arr)
    elif(ch == 'U' or ch == 'u'):
        up(arr)
    elif(ch == 'D' or ch == 'd'):
        down(arr)
    else:
        inp(arr)


#MAIN
def main():
    print()
    print("Welcome to 2048 game")
    print("Press L to move left or R to move right or U to move up or D to move down")
    print()
    print("Initial board:")
    print()
    r1 = random.randint(0,15)
    r2 = random.randint(0,15)
    while(r2==r1):
        r2 = random.randint(0,15)

    arr = [[0,0,0,0],
           [0,0,0,0],
           [0,0,0,0],
           [0,0,0,0]]

    c = 0
    for i in range(4):
        for j in range(4):
            if c == r1 or c == r2:
                arr[i][j] = random.choice([int(2), int(4)])
            c = c+1
    
    #arr =[[4,0,0,4],[0,0,0,0],[1,0,0,0],[2,0,0,0]]
    
    board(arr)
    inp(arr)


main()