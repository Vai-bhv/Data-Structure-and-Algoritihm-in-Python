class Stack:
    def __init__(self):
        # Initialize an empty stack
        self.stack = [ ]
        
    def push(self, value):
        # Push a value onto the stack
        self.stack.append(value)
        
    def pop(self):
        # Pop a value from the stack
        return self.stack.pop()
    
    def __str__(self):
        # Return a string representation of the stack
        omega = self.stack[::-1]
        return "[ " + " ".join(map(str, omega)) + " ]"

# Open the input file
with open("VSTUP.TXT", "r") as f:
    # Create a new stack
    stack = Stack()
    
    # Iterate over the lines in the file
    for line in f:
        # Split the line into command and value
        command, *values = line.strip().split()
        
        # Execute the command
        if command == "U":
            value = int(values[0])
            stack.push(value)
            print(line.strip())
        elif command == "O":
            value = stack.pop()
            print(line.strip())
            print(value)
        elif command == "P":
            print(line.strip())
            print(f'{stack}')

