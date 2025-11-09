def inp():
  name1 = str(input("What is your name ?"))
  age = int(input("How old are you ?"))
  wgt = float(input("What is your weight in kgs ?"))
  print(f"Your name is {name1}. You are {age} years old and you are {wgt} kg." )



def sum():
  a = int(input("Enter a number to add : "))
  b = int(input("Enter a number to add  : "))
  sum = a + b
  print(sum)



def sub():
  a = int(input("Enter a number to subtract : "))
  b = int(input("Enter a number to subtract : "))
  sub = a - b
  print(sub)


def mul():
  a = int(input("Enter a number to multiply: "))
  b = int(input("Enter a number to multiply: "))
  mul = a * b
  print(mul)


def div():
  a = int(input("Enter a number to divide: "))
  b = int(input("Enter a number to divide: "))
  div = a / b
  print(div)


def mod():
  a = int(input("Enter a number to get the remainder: "))
  b = int(input("Enter a number to get the remainder: "))
  mod = a % b
  print(mod)


def patt():
  for i in range(1, 5):
    print("*" * i)
patt()