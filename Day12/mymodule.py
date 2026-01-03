import random
import string

def random_user_id():
    characters = string.ascii_letters + string.digits
    user_id = ''.join(random.choice(characters) for i in range(6))
    return user_id

def user_id_gen_by_user():
    characters = string.ascii_letters + string.digits
    num_ids = int(input("Enter number of IDs to generate: "))
    id_length = int(input("Enter length of each ID: "))
    ids = []
    for i in range(num_ids):
        user_id = ''.join(random.choice(characters) for j in range(id_length))
        ids.append(user_id)
    return ids
def rgb_color_gen():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return f"rgb({r}, {g}, {b})"
def list_of_hexa_colors(n=3):
    colors = []
    hex_chars = string.hexdigits[:-6]  # Exclude uppercase letters A-F
    for i in range(n):
        color = '#'
        for j in range(6):
            color += random.choice(hex_chars)
        colors.append(color)
    return colors
def list_of_rgb_colors(n=3):
    colors = []
    for i in range(n):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        colors.append(f"rgb({r}, {g}, {b})")
    return colors
def generate_colors(type, n):
    if type == 'hexa':
        return list_of_hexa_colors(n)
    elif type == 'rgb':
        return list_of_rgb_colors(n)
    else:
        return "Invalid color type. Choose 'hexa' or 'rgb'."
def shuffle_list(l):
    random.shuffle(l)
    return l
def generate_numbers():
    numbers = string.digits
    res = []
    for i in range(0, 7):
        num = random.choice(numbers)
        while num in res:
            num = random.choice(numbers)
        res.append(num)
    return res