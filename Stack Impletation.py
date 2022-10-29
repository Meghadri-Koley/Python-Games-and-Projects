def isEmpty(stk):

    if stk == []:
        return True
    else:
        return False

def push(stk,item):
    stk.append(item)
    top = len(stk) - 1


def pop(stk):
    if isEmpty(stk) == True:
        return "UNDERFLOW\n"
    else:
        popped_item = stk.pop()
        if len(stk) == 0:
            top = None
        else:
            top = len(stk) - 1
        
        return popped_item

def peek(stk):
    if isEmpty(stk) == True:
        return "UNDERFLOW\n"
    else:
        top = len(stk) - 1
        return stk[top]

def display(stk):
    if isEmpty(stk):
        print("STACK IS EMPTY\n")
    else:
        top = len(stk) - 1
        print(stk[top],"<------- Top")
        for i in range(top-1,-1,-1):
            print(stk[i],"\n")




#____MAIN____
stack = []
top = None

while True:
    print("STACK OPERATIONS:")
    print("1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Display")
    print("5. Exit\n")
    choice_for_operation = int(input("Enter your choice (1 - 5):\n"))

    if choice_for_operation == 1:
        item = int(input("Enter the value you want to PUSH: "))
        push(stack,item)
    
    elif choice_for_operation == 2:
        item = pop(stack)
        if item == "UNDERFLOW":
            print("UNDERFLOW!!!\n")
        else:
            print("Popped item is",item,"\n")
    
    elif choice_for_operation == 3:
        item = peek(stack)
        if item == "UNDERFLOW":
            print("NO TOP AVAILABLE\n")
        else:
            print("Topmost element is",item,"\n")
    elif choice_for_operation == 4:
        display(stack)
    elif choice_for_operation == 5:
        exit()
    else:
        print("WRONG CHOICE.....CHOOSE AGAIN!!!\n")
