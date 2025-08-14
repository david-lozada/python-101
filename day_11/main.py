""" import sys """
from modules import generate_colors, shuffle_list, generate_unique_random_numbers
""" generate_full_name as fullname, user_id_gen_by_user as gen_users_ids, rgb_color_gen """

""" print(fullname(sys.argv[1], sys.argv[2]))
gen_users_ids()
print(rgb_color_gen()) """
print(generate_colors('rgb', 3))
print(shuffle_list([1, 2, 3, 4, 5]))  # Example output: [3, 1, 5, 2, 4]
print(generate_unique_random_numbers())