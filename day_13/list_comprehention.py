numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]

filtered = [i for i in numbers if i > 0]
flattened = [num for sublist in list_of_lists for subsublist in sublist for num in subsublist]
print(flattened)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(filtered)