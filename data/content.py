from data.config import admins
from loader import db


greatings = """<i>
Напиши мне сообщение и я передам его своему владельцу, который ответит тебе через меня.\n
Помимо текстовых сообщений ты можешь отправлять следующие типы файлов: jpg, jpeg, png, gif,\n
pdf, zip, rar, tar.gz, tar.xz и прочие типы архивов, mp3, ogg, mp4, avi и прочие форматы медиа-файлов.\n
Так же можешь отправлять голосовые сообщения и стикеры. Обрати внимание, что размер любого фала,\n
отправляемого через бот, не должен превышать 20Mb. Лучше всего будет если ты разместишь файлы\n
в облаке и передашь ссылку на скачивание. Ну, как то так) Если же твоя информация строго конфиденциальна,\n
то пиши сюда: shurab@tuta.io Приятного пользования и всего доброго!</i>"""


often_text = """Проверь внимательно, ты не правильно ввел цифры,\nлибо не верный ID пользователя!"""


capture_greatings = """<b>Привет, {user_name}! Мне нужно убедиться в том, что ты человек.
Для этого введи символы с картинки, добавь в конец две буквы, которые я прислал тебе, 
и отправь мне. Должно получиться как на этом примере: YND03L87bn</b>"""


items = db.select_all_users()
list_users_id = db.select_users_id()

def get_item(item_id):
    for item in items:
        if int(item_id) == item[0]:
            return item



def permitted():
    permitted_users = list_users_id
    for admin in admins:
        permitted_users.append(admin)
    return list(set(permitted_users))






