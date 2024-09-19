#print ("hello, world!")
#name=input



#x = input('Please enter first numbers:')
#x = int(x)
#y = input("Please enter second number")
#print(type(number))
#y = int(y)
#if x > y:
 #   print("X > Y")
#elif x == y:
  #  print("X = Y")
#else:
 #   print("X < Y")

#modify the code to ask for two numbers and compare 

# exmple: Simulate a log in process ( ask for usenrame and password)

# username = input("please enter username >>")
# password = input("please enter your password >>") #123456

# if username == "admin" and password == "123456":
#         print("welcome!")
# else:
#     print("get out of here")

# Loops

# Counter = 3

#while counter > 0 
#     print("Meow")
#     counter = counter - 1


# for I in range (3):
#     print("Meow")

#while True:
 #   print("meow")


# Keep asking user for password intil he enters the right one

while True:
    password = input("enter your password >> ") # password is 123456

    if password == "123456":
        print("Welcome")
        break # stop the loop
    else:
        print("Try one more time")