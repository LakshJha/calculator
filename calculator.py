#Defining functions

#Function that will add
def add(x,y):
  return x+y
 
#Function that will subtract
def sub(x,y):
  return x-y
 
#Function that will multiply
def mul(x,y):
  return x*y
 
#Function that will divide 
def div(x,y):
  return x/y

#Briefing about the choices the user have
print("Select an operation")
print("1 for addition")
print("2 for subtraction")
print("3 for multiplication")
print("4 for division")

#Taking user inputs
while True:
  choice = input("Enter your choice: ")
  
  if choice in ('1', '2', '3', '4'):
    x = float(input("Enter the first number: "))
    y = float(input("Enter the second number: "))

    #Generating output as per the user
    if(choice=='1'):
      print(x, "+", y, "=", add(x,y))

    elif(choice=='2'):
      print(x, "-", y, "=", sub(x,y))

    elif(choice=='3'):
      print(x, "*", y, "=", mul(x,y))

    elif(choice=='4'):
      print(x, "/", y, "=", div(x,y))
    break
else:
  print("Invalid selection")
