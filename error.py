#17.Write a Python program to handle the error when someone tries to convert a non-numeric string to an integer (ValueError).     

value = input("Enter a number: ")

try:
    num = int(value)
    print("Converted number:", num)

except ValueError:
    print("Error: You must enter a numeric value!")