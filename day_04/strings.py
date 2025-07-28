coding = "coding " + "for " + "all"
sentence = "You cannot end a sentence with because because because is a conjunction"
"""print(coding.find("coding"))
print(coding.replace("coding", "python"))
print(coding.split(" "))
print("Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon".split(", "))
print(coding[9])"""

"""python = "Python For Everyone"
python_list = python.split(" ")
print(python_list)
for word in python_list:
    print(word.capitalize()[0])"""

# Find the starting index of 'because because because'
start_index = sentence.find('because because because')

# Calculate the length of the phrase to remove
phrase_length = len('because because because')

# Slice out the phrase by concatenating the parts before and after it
result = sentence[:start_index] + sentence[start_index + phrase_length:]

print("thirty_days_of_python".isidentifier())