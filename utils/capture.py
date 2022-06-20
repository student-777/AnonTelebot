
from PIL import Image, ImageFont, ImageDraw
import random
import string



def randStr(chars = string.ascii_uppercase + string.digits, chars2 = string.ascii_lowercase, N=8):
    # return ''.join(random.choice(chars) for _ in range(N))
    random_text = ''.join(random.choice(chars) for _ in range(N))
    add_text = ''.join(random.choice(chars2) for _ in range(2))
    x1, x2, x3, x4, x5, x6, x7, x8 = tuple(random_text)
    cap_text = f"{x1} {x2}{x3}{x4} {x5}{x6} {x7} {x8}"
    sum_text = random_text + add_text

    return cap_text, add_text, sum_text

# a = randStr()[0]
# print(a)


def gen_capture():
    img = Image.open('documents/capture.jpg')
    # img.show()
    # print(img.size)
    idraw = ImageDraw.Draw(img)
    font = ImageFont.truetype("documents/Gidole-Regular.ttf", size=40)
    cap_text, add_text, sum_text = randStr()
    # print(text)
    idraw.text((200, 100), cap_text, font=font, fill="black")
    img.save('documents/capture_out.jpg')
    return cap_text, add_text, sum_text


