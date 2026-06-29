def still():
  #This is to hold the result up
  while True:
    holder = input("User: Press <ENTER> to close")
    if holder == "":
      quit()
class operations:

  def add():
    num1 = input("User: Insert num1 > ")
    try:
      Num1 = float(num1)
    except ValueError:
      print("ERROR: The input for num1 is incorrect")
    num2 = input("User: Insert num2 > ")
    try:
      Num2 = float(num2)
    except ValueError:
      print("ERROR: The input for num2 is incorrect")
    res = Num1 + Num2
    print(f"Result is {res}")
    still()
    
  def subtract():
    num1 = input("User: Insert num1 > ")
    try:
      Num1 = float(num1)
    except ValueError:
      print("ERROR: The input for num1 is incorrect")
    num2 = input("User: Insert num2 > ")
    try:
      Num2 = float(num2)
    except ValueError:
      print("ERROR: The input for num2 is incorrect")
    res = Num1 - Num2
    print(f"Result is {res}")
    still()
    
  def muliply():
    num1 = input("User: Insert num1 > ")
    try:
      Num1 = float(num1)
    except ValueError:
      print("ERROR: The input for num1 is incorrect")
    num2 = input("User: Insert num2 > ")
    try:
      Num2 = float(num2)
    except ValueError:
      print("ERROR: The input for num2 is incorrect")
    res = Num1 * Num2
    print(f"Result is {res}")
    still()

  def divide():
    num1 = input("User: Insert num1 > ")
    try:
      Num1 = float(num1)
    except ValueError:
      print("ERROR: The input for num1 is incorrect")
    num2 = input("User: Insert num2 > ")
    try:
      Num2 = float(num2)
    except ValueError:
      print("ERROR: The input for num2 is incorrect")
    try:
      res = Num1 / Num2
    except ZeroDivisionError:
      print("ERROR: Cannot Divide By Zero")
    print(f"Result is {res}")
    still()
    
    
def main_app():
  print("BubsProducts Calculator App")
  print()
  print("1 - Addition\n2 - Subtraction\n3 - Mulipalcation\n4 - Division")
  command = input("User: Insert One of the numbers above > ")
  if command == "1":
    operations.add()
  elif command == "2":
    operations.subtract()
  elif command == "3":
    operations.muliply()
  elif command == "4":
    operations.divide()
  elif operations == "":
    quit()
  else:
    print("ERROR: Not A valid input")

main_app()
