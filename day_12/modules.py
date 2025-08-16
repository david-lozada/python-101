import random

def generate_full_name(firstname, lastname):
    return firstname + ' ' + lastname

def random_user_id(repeat):
    characters = ""
    for i in range(repeat):
        characters += random.choice("abcdefghijklmnopqrstuvwxyz0123456789")
    return characters

def user_id_gen_by_user():
    while True:
        try:
            cha_nums = int(input("Enter the number of characters for the user ID: "))
            id_nums = int(input("Enter the number of ID's: "))
            if cha_nums <= 0 or id_nums <= 0:
                print("Please enter a positive numbers.")
                continue
            for _ in range(id_nums): 
                print(random_user_id(cha_nums))
            break
        except ValueError:
            print("Please enter a valid number.")
            continue
        
def rgb_color_gen():
    code_1 = random.randint(0, 255)
    code_2 = random.randint(0, 255)
    code_3 = random.randint(0, 255)
    return f"rgb({code_1}, {code_2}, {code_3})"

def generate_colors(type, repeat):
    colors = []
    if type == "hex":
        for _ in range(repeat):
            color = f"#{random.randint(0, 0xFFFFFF)}"
            colors.append(color)
    elif type == "rgb":
        for _ in range(repeat):
            colors.append(rgb_color_gen())
    return colors

def shuffle_list(input_list):
    """Takes a list and returns a shuffled version of it"""
    shuffled = input_list.copy()  # Create a copy to avoid modifying the original
    random.shuffle(shuffled)     # Shuffle the copy in-place
    return shuffled

def generate_unique_random_numbers():
    """Returns an array of seven unique random numbers between 0-9"""
    numbers = list(range(10))     # Create list [0, 1, 2, ..., 9]
    shuffled = shuffle_list(numbers)  # Shuffle the list
    return shuffled[:7]          # Return first 7 elements