class QUEUE:
    def __init__(self):
        self.queue = []
        self.rear = -1
        self.front = -1
    def isempty(self):
        if len(self.queue) == 0:
            return True
        else:
            return False
    def enqueue(self,value):
        self.queue.append(value)
        if self.front == -1:
            self.front = +1
            self.rear = +1
            print("successfully added value:" ,value)
        else:
            self.rear +=1
            print(value,"successfully inserted")
    def dequeue(self,value):
        if len(self.queue) == 0:
            print("queue is empty")
        else:
            temp = self.queue.pop(self.front)
            print("popped item is:",temp)
            self.rear =-1
            if self.isempty()is True:
                self.front = -1
                self.rear = -1
            return
    def display(self):
        if len(self.queue)==0:
            print("queue is empty")
            return
            print("the contents of queue are:")
        if self.front == self.rear:
            print(self.queue[self.front],"<== front <==rear")
            return
            print(self.queue[self.front], "<==front")
            i = self.front + 1
            while i <self.rear:
                print(self.queue[i])
                i +=1
                print(self.queue[self.rear], "<==rear")

a = QUEUE()
while True:
    print("**********************")
    option = int(input("enter your choice\n1:Inster\n2:Delete\n3: Display\n4:Exit\n"))
    if option == 1:
        value = int(input("enter the value you want to add ::"))
        a.enqueue(value)
        continue
    elif option == 2:
        a.dequeue()
        continue
    elif option == 3:
        a.display()
        continue
    elif option == 4:
        print("exiting")
        break
    else:
        print("wrong option")
