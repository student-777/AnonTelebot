Этот бот создан для анонимного общения в telegram. По сути он является прокладкой между вашим акаунтом и тем абонентом с которым вы ведете чат.

Вы видете id абонента, его full name, но для абонента вы анонимны.

Бот написан на aiogram версии 2.10.1 (возможно применение версий < 3.0)  и использует шаблон https://github.com/student-777/aiogram-bot-template

Для защиты от спама абоненту нужно решить простейшую задачу: ввести капчу плюс 2-ва рандомных символа. 

Бот может пересылать текстовые сообщения, файлы изображений, документы и архивы различного формата, видео и аудио файлы, голосовые сообщения. Но при этом нужно учесть, что telegram установил лимит на передаваемые файлы: размер файла не может превышать 20Мб.

Выбор абонента производится через клавиатуру, которая вызывается командой /users. Регистрация и запись абонентов в базу данных происходит автоматически при решении капчи.

Команды, доступные ТОЛЬКО АДМИНИСТРАТОРУ по команде /help:

/broadcast - Отправка сообщения всем пользователям.

/countusr - Колличество пользователей в БД.

/users - Список пользователей для отправки сообщений.

/lock - Блокировать пользователя.

/unlock - Разблокировать пользователя.

/usersdb - Чтение БД.

/deluser - Удаление пользователя из БД.

/cleardb - Полная очистка БД.

Для работы бота требуется версия python 3.8 - 3.9, на 3.10 не проверял. Бот запускается командой: python3 app.py

**ЗАПУСК БОТА В ВИРТУАЛЬНОМ ОКРУЖЕНИИ:**

cd AnonTelebot

python3 -m venv venv

source venv/bin/activate

pip3 install --upgrade pip

pip3 install --upgrade setuptools

pip3 install -r requirements.txt

python3 app.py

**ЗАПУСК БОТА В docker:**

cd AnonTelebot

sudo docker-compose build

docker-compose up -d

**ЗАПУСК ЧЕРЕЗ systemd:**
Создайте файл /etc/systemd/system/anontelebot.service

Скопируйте в него следующее содержание:

[Unit]

Description=Anonimous Bot
After=network.target

[Service]

User=tgbot
Group=tgbot
Type=simple
WorkingDirectory=/opt/AnonTelebot
ExecStart=/opt/tgbot/venv/bin/python3 bot.py
Restart=always

[Install]

WantedBy=multi-user.target


Скопируйте каталог AnonTelebot в /opt/

Далее выполните следующие команды:

cd /opt/AnonTelebot

python3 -m venv venv

source venv/bin/activate

pip3 install --upgrade pip

pip3 install --upgrade setuptools

pip3 install -r requirements.txt

sudo systemctl daemon-reload

sudo systemctl enable anontelebot.service

sudo systemctl start anontelebot.service

Проверьте работу юнита:

systemctl status anontelebot.service


Файл фона капчи capture.jpg находится в каталоге /documents проекта. Вы можете заменить его на любой другой файл изображения, размером примерно 555х260 px.

Там же находятся и шрифты для капчи: Gidole-Regular.ttf и Gidolinya-Regular.otf.

По желанию вы можете установить и другие шрифты, прописав их в файле /utils/capture.py проекта.

Вставьте свой токен бота в файл env.dist проекта, затем измените его название на .env

В файл /data/config.py в словарь admins = [] вставьте ваш chat_id и chat_id других администраторов через запятую.

Файл /handlers/users/test.py оставил, может кому-то понадобится.

Если есть какие-либо конструктивные предложения по улучшения бота пишите, буду рад.











