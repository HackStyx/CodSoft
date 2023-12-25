# Calculator operations
def add(a, b):
    return a + b  

def subtract(a, b):
   return a - b

def multiply(a, b):
   return a * b

def divide(a, b):
    if b == 0:
        print("Cannot divide by 0!")
        return None
    return a / b

# Operation functions dict  
operations = {
    1: add,
    2: subtract, 
    3: multiply,
    4: divide 
}

def calculate():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
  
    choice = input_number("Enter choice(1-4): ")

    num1 = input_number("Enter first number: ")
    num2 = input_number("Enter second number: ")

    func = operations.get(choice)
    if func:
        result = func(num1, num2)
        if result is not None:
            print(result) 
    else:
        print("Invalid operation")
   
def input_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number")
            continue
               
calculate()