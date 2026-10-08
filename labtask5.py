
# Question 1: Student information tuple
name = input("Enter your name: ")
age = int(input("Enter your age: "))
program = input("Enter your program: ")
marks = float(input("Enter your marks: "))

student = (name, age, program, marks)
print("Student information:", student)


# Question 2: Sentence analysis
sentence = input("Enter a sentence: ")

characters = len(sentence)
words = len(sentence.split())
vowels = sum(1 for char in sentence if char.lower() in "aeiou")
spaces = sentence.count(" ")
digits = sum(1 for char in sentence if char.isdigit())

print("Number of characters:", characters)
print("Number of words:", words)
print("Number of vowels:", vowels)
print("Number of spaces:", spaces)
print("Number of digits:", digits)


# Question 3: Information for three employees
employees = []

for number in range(1, 4):
    print("Employee", number)
    employee_name = input("Enter name: ")
    employee_age = int(input("Enter age: "))
    salary = float(input("Enter salary: "))

    employee = (employee_name, employee_age, salary)
    employees.append(employee)

print("Employees:", employees)


# Question 4: Count even and odd numbers
numbers = (10, 15, 20, 25, 30, 35, 40)

even_count = 0
odd_count = 0

for number in numbers:
    if number % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print("Numbers:", numbers)
print("Even numbers:", even_count)
print("Odd numbers:", odd_count)