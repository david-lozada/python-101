countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def to_uppercase(country):
	return country.upper()

def to_square(num):
	return num ** 2

def land_filter(country):
	if 'land' in country:
		return True
	else:
		return False

countries_upper = map(to_uppercase, countries)
numbers_square = map(to_square, numbers)
filtered_countries = filter(land_filter, countries)
print(list(filtered_countries))