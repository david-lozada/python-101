from countries import countries
""" from datetime import datetime

current_year = datetime.now().year

while True:
    try:
        user_age = int(input("What's your age? "))
    except ValueError:
        print("Age must be a number")
    else:
        print(f"You were born in {current_year - user_age}")
        break
else:
    print("Provide a number") """
    
""" number = 10
while number >= 0:
    print(number)
    number -= 1 """
    
""" for num in range(7):
    print("#" * (num + 1)) """

""" num = range(8)
for row in num:
    for col in num:
        print("#", end=" ")
    print() """
    
""" num = range(8)
for row in num:
        print("# " * len(num)) """
        
""" tables = range(10)
for num in tables:
    print(f"{num} x {num} = {num * num}") """
    
""" numbers = range(100)
for num in numbers:
    if num % 2 == 0:
        print(f"{num} is even")
    else:
        print(f"{num} is odd") """
    
numbers = range(101)
""" total = 0
for num in numbers:
    total += num
    print(total) """

""" total_evens = 0
total_odds = 0
for num in numbers:
    if num % 2 == 0:
        total_evens += num
    else:
        total_odds += num
print(f"The sum of all evens is {total_evens}. And the sum of all odds is {total_odds}.") """

print("Findland".find("apple"))