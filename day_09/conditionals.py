from collections import Counter

""" a = 3
if a < 0:
    print('A is a negative number')
else:
    print('A is a positive number')
     """
""" a = 3
print('A is positive') if a > 0 else print('A is negative') """ # first condition met, 'A is positive' will be printed

""" user_age = int(input('Enter your age: '))
if user_age < 18:
    years_left= 18 - user_age
    print(f'You need {years_left} more years to learn to drive.')
else:
    print('You are old enough to learn to drive.')
    
print(f'You are {user_age - 27} years older than me') if user_age > 27 else print(f'I am {27 - user_age} years older than you') """

""" a = int(input('Enter a number: '))
b = int(input('Enter a number: '))

if a > b: 
    print('A is greater than B')
else:
    print('A is smaller than B') """

""" grade = int(input('Enter your grade: '))
if grade >= 90 and grade <= 100:
    print('You got an A')
elif grade >= 70 and grade <= 89:
    print('You got a B')
elif grade >= 60 and grade <= 69:
    print('You got a C')
elif grade >= 50 and grade <= 59:
    print('You got a D')
else: 
    print('You got an F') """
    
""" autumn = ['September', 'October', 'November']
spring = ['March', 'April', 'May']
winter = ['December', 'January', 'February']
summer = ['June', 'July', 'August']
month = input('Enter a month: ').capitalize()
if month in autumn:
    print('It is autumn')
elif month in spring:
    print('It is spring')
elif month in winter:
    print('It is winter')
else:
    print('It is summer') """
    
""" fruits = ['banana', 'orange', 'mango', 'lemon']
fruit = input('Enter a fruit: ').lower()
if fruit in fruits:
    print('That fruit already exists in the list')
else:
    fruits.append(fruit.lower())
    print(fruits) """
    
person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}
"""frontend = ['JavaScript', 'React']
backend = ['Node', 'MongoDB', 'Python']
fullstack = frontend + backend
if person['skills']:
    print(person['skills']) 
    if Counter(person['skills']) == Counter(fullstack):
        print('He is a fullstack developer')
    elif Counter(person['skills']) == Counter(frontend):
        print('He is a frontend developer')
    elif Counter(person['skills']) == Counter(backend):
        print('He is a backend developer')
    else:
        print('Unknown title')
else:
    print('No skills found')"""

""" + 'married' if person['is_marred'] else 'single' """
print(f"{person['first_name']} {person['last_name']} lives in {person['country']}. He is {'married' if person['is_married'] else 'single'}.")