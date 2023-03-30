from art import logo
def add(n1,n2):
  return n1 + n2

def subtract(n1,n2):
  return n1 - n2

def multiply(n1,n2):
  return n1 * n2

def divide(n1,n2):
  return n1 / n2

operations = {
  "+" : add,
  "-" : subtract,
  "*" : multiply,
  "/" : divide
}

def cal1():
    print(logo)

  
    num1 = float(input("What is the number? : "))
    for symbol in operations:
      print(symbol)
      
    get_continue = True
  
    while get_continue:
      operation_symbol  = input("Pick an operation!  : ")
      num2 = float(input("What is the number? : "))
      calculation_function = operations[operation_symbol]
      answer = calculation_function(num1, num2)
      
      print(f"{num1} {operation_symbol} {num2} = {answer}")
      
      if input(f"Type 'y' to continue calculating with {answer}, or Type 'n' start a new calculation : ") == "y":
        num1 = answer        
      else:
        get_continued = False
        cal1()
  
cal1()
