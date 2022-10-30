def isEmpty(qu):

    if qu == []:
        return True
    else:
        return False

def enqueue(qu,item):
    qu.append(item)
    if len(qu) == 1:
        front = rear = 0
    else:
        rear = len(qu) - 1


def dequeue(qu):
    if isEmpty(qu) == True:
        return "UNDERFLOW\n"
    else:
        popped_item = qu.pop(0)
    if len(qu) == 0:
        front = rear = None
    return popped_item
            

def peek(qu):
    if isEmpty(qu) == True:
        return "UNDERFLOW\n"
    else:
        front = qu[0]
        return front

def display(qu):
    if isEmpty(qu):
        print("QUEUE IS EMPTY\n")
    elif len(qu) == 1:
        print(qu[0],"<------FRONT, REAR")
    else:
        front = 0
        rear = len(qu) - 1
        print(qu[front],"<-----FRONT")
        for i in range(1,rear):
            print(qu[i])
        print(qu[rear],"<-----REAR")




#____MAIN____
Queue = []
front = None

while True:
    print("QUEUE OPERATIONS:")
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Peek")
    print("4. Display")
    print("5. Exit\n")
    choice_for_operation = int(input("Enter your choice (1 - 5):\n"))

    if choice_for_operation == 1:
        item = int(input("Enter the value you want to PUSH: "))
        enqueue(Queue,item)
    
    elif choice_for_operation == 2:
        item = dequeue(Queue)
        if item == "UNDERFLOW":
            print("UNDERFLOW!!!\n")
        else:
            print("De-queued item is",item,"\n")
    
    elif choice_for_operation == 3:
        item = peek(Queue)
        if item == "UNDERFLOW":
            print("QUEUE IS EMPTY\n")
        else:
            print("Frontmost element is",item,"\n")
    elif choice_for_operation == 4:
        display(Queue)
    elif choice_for_operation == 5:
        exit()
    else:
        print("WRONG CHOICE.....CHOOSE AGAIN!!!\n")
