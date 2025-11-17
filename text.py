#16.Write a Python program to open a file named data.txt, read its content, and print it. If the file doesn’t exist, create it and write “Hello QA Trainee” into it.

try:
    with open("data.txt", "r") as file:
        content = file.read()
        print("File content:", content)

except FileNotFoundError:
    with open("data.txt", "w") as file:
        file.write("Hello QA Trainee")
    print("data.txt not found, so it was created with default text.")
