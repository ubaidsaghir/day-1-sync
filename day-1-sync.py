# DAY 1
# What happens if you try to execute result = 5 + "10" in Python? How would you modify the code to make it output 15, and how would you modify it to output "510
result = 5 + "10"
# You have a variable price = 19.99. What built-in Python function can you use to verify its data type? How would you convert this float into an integer, and what would the resulting value be?

price = 19.99
print(type(price))

# 3. Given the list temperatures = [72.5, 74.1, 71.8, 75.0]:

# - How do you access the value 71.8 using indexing?
# - How do you add a new temperature, 73.2, to the end of this list?

temperatures = [72.5, 74.1, 71.8, 75.0]
print(temperatures[2])
temperatures.append(73.2)
print(temperatures) 

# 4. Create a dictionary called user_profile with the keys "username" (string), "is_active" (boolean), and "login_count" (integer).

# - How do you access the value of "login_count"?

# - How do you add a new key-value pair for "email"?

user_profile = {
    "username": "Ubaid",
    "is_active": True,
    "login_count": 3
}

print(user_profile)

count = user_profile["login_count"]
print(count)

user_profile["email"]="ubaidsaghir4566@gmail.com"
print(user_profile)

# Loops & Logic (for, while)
# 5. Write a for loop that iterates through a list of numbers [1, 2, 3, 4, 5] and prints out the square of each number.

numbers = [1,2,3,4,5]

for num in numbers:
 print(num**2)
print(num)

# 6. Write a while loop that starts with a variable counter = 5 and prints the counter, decreasing it by 1 each time, until it reaches 0 (print "Blastoff!" when it finishes).

counter = 5

while counter > 0:
  print(counter)
  counter -= 1

print("Blastoff!")

# Put it all together: Create a list called students. Inside this list, place three dictionaries. Each dictionary should represent a student and have two keys: "name" (a string) and "gpa" (a float).

# Write a for loop that iterates through the students list.

# Inside the loop, use an if statement to check if the student's GPA is greater than 3.0.

# If it is, print that student's name.

students = [
    {"name":"ubaid","gpa":3.2},
    {"name":"Ali","gpa":2.8}]
for std in students:
  if std["gpa"]>3.0:
    print(std)
