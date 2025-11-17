#11. Program to check login credentials.
#Ask for username and password
#If correct → print success
#Else → print failed


username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin" and password == "12345":
    print("Login Successful")
else:
    print("Login Failed")

