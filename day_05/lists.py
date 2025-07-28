# Day 05 python 
from countries import COUNTRIES

"""countries = ["India", "USA", "Canada", "Australia", "Germany"]
print(f"first country: {countries[0]} and last country: {countries[-1]}")"""

""" mixed_data_types = ["David Lozada", 1.70, 27, "Single", "Mene Grande"]
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
new_it_companies = []
new_it_companies.append(it_companies[0])
new_it_companies.append(it_companies[3])
new_it_companies.append(it_companies[-1])
new_it_companies.insert(1, "Xiaomi")
it_companies[2] = it_companies[2].upper()
for company in it_companies:
    print(company, end="# ")
it_companies.sort(reverse=True)
it_companies.reverse()
first_three_companies = it_companies[:3]
first_half_countries = COUNTRIES[:len(COUNTRIES)//2]
second_half_countries = COUNTRIES[len(COUNTRIES)//2:]
print(f"First half of second_half_countries: {len(first_half_countries)}")
print(f"Second half of second_half_countries: {len(first_half_countries)}") """
# print(len(COUNTRIES))

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
unique_ages = set(ages)
ages = list(unique_ages)
print(ages)