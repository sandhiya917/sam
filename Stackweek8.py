class Stack:
    def __init__(self,maxSize,top):
        self.maxSize = maxSize
        self.tops = top
        self.list = []
#modifying the __str__ function to return the desired string version of stack
    def __str__(self):
        values =self.list.reverse()
        values = [str(x) for x in self.list]
        return '\n'.join(values)
#push function to insert elements
    def push(self,value):
        if self.tops == self.maxSize:
            print("The stack is full.")
        else:
            self.list.append(value)
            self.tops +=1
            print(value, "has been successfully added to the stack.")
#pop function to remove elements
    def pop(self):
        if self.tops == -1:
           print("The stack is empty.")
        else:
            print("Popped item = ", self.list.pop())
            self.tops -=1
#display function to display elements
    def display(self):
        if self.tops == -1:
            print("The stack is empty")
        else:
            print("Contents of the stack are")
            print(self)
#example
tempStack = Stack(3,-1)
tempStack.push(50)
tempStack.push(60)
tempStack.push(70)
tempStack.display()
tempStack.pop()
tempStack.pop()
tempStack.display()