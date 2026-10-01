class Stack:
    def __init__(self):
        self.stack = []

    # Push an element
    def push(self, value):
        self.stack.append(value)
        print(value, "pushed into stack")

    # Pop an element
    def pop(self):
        if len(self.stack) == 0:
            print("Stack Underflow")
        else:
            print(self.stack.pop(), "popped from stack")

    # Peek at the top element
    def peek(self):
        if len(self.stack) == 0:
            print("Stack is empty")
        else:
            print("Top element:", self.stack[-1])

    # Display the stack
    def display(self):
        if len(self.stack) == 0:
            print("Stack is empty")
        else:
            print("Stack elements:")
            for i in range(len(self.stack) - 1, -1, -1):
                print(self.stack[i])


# Create stack
s = Stack()

s.push(10)
s.push(20)
s.push(30)

s.display()

s.peek()

s.pop()
s.display()
