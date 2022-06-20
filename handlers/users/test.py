import string
import random

a = [6789, 678901, 12345, 2345678]
b = ('serge', 'tanya', 'dima', '123')

def foo(*args):
    for item in a:
        if item in args:
            print(f'Число {args[0]} входит в состав списка a')
            print(type(args[0]))

# foo(678901)

# (c, d, f, e) = b
# print(c, d)
def randStr(chars = string.ascii_uppercase + string.digits, chars2 = string.ascii_lowercase, N=8):
    # return ''.join(random.choice(chars) for _ in range(N))
    random_text = ''.join(random.choice(chars) for _ in range(N))
    add_text = ''.join(random.choice(chars2) for _ in range(2))
    x1, x2, x3, x4, x5, x6, x7, x8 = tuple(random_text)
    cap_text = f"{x1} {x2}{x3}{x4} {x5}{x6} {x7} {x8}"
    sum_text = random_text + add_text

    return cap_text, add_text, sum_text


# chars = string.ascii_lowercase
# random_text = ''.join(random.choice(chars) for _ in range(2))
# print(random_text)

# a = randStr()[0]
# print(a)


# text = """Привет! Меня зовут {name}, мне {age} лет."""
# my_text = text.format(name='Serge', age=42)
# print(my_text)

