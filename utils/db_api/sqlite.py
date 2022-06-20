import sqlite3


class Database:
    def __init__(self, path_to_db="main.db"):
        self.path_to_db = path_to_db



    @property # Декоратор позволяет обращаться к ф-ции без скобок
    def connection(self):
        """Создание и соединение с БД"""
        return sqlite3.connect(self.path_to_db)




    def execute(self, sql: str, parameters: tuple = None, fetchone=False, fetchall=False, commit=False):
        """Исполнение команд. sql - команда; parameters - параметры команды."""
        if not parameters:
            parameters = ()
        connection = self.connection
        connection.set_trace_callback(logger)
        cursor = connection.cursor()
        data = None
        cursor.execute(sql, parameters)

        if commit:
            connection.commit()
        if fetchall:
            data = cursor.fetchall()
        if fetchone:
            data = cursor.fetchone()
        connection.close()
        return data



    def create_table_users(self):
        """Создание таблицы Users"""
#         sql = """
#         CREATE TABLE Users (
#             user_number INTEGER PRIMARY KEY AUTOINCREMENT,
#             id int NOT NULL UNIQUE,
#             Name varchar(255) NOT NULL,
#             email varchar(255)
#             );
# """
        sql = """
                CREATE TABLE Users (
                    id int NOT NULL,
                    Name varchar(255) NOT NULL,
                    date_time varchar(255),
                    user_state varchar(255),
                    PRIMARY KEY (id)
                    );
        """
        self.execute(sql, commit=True)




    def create_table_current_user(self):
        """Создание таблицы Currentuser - аналог ячейки памяти для
        записи id одного пользователя"""
        sql = """
                        CREATE TABLE Currentuser (
                            id int NOT NULL,
                            PRIMARY KEY (id)
                            );
                """
        self.execute(sql, commit=True)




    def create_table_capture(self):
        """Создание таблицы Capture для записи кода капчи
        при его генерации"""
        sql = """CREATE TABLE Capture (
                    sum_text varchar(255)
                    );"""
        self.execute(sql, commit=True)




    @staticmethod
    def format_args(sql, parameters: dict):
        """Метод форматирования строки команды с защитой от SQL-инъекции"""
        sql += " AND ".join([
            f"{item} = ?" for item in parameters
        ])
        return sql, tuple(parameters.values())




    def add_user(self, id: int, name: str, date_time: str = None, user_state: bool = False):
        """Добавление пользователя в таблицу"""
        # SQL_EXAMPLE = "INSERT INTO Users(id, Name, email) VALUES(1, 'John', 'John@gmail.com')"

        sql = """
        INSERT INTO Users(id, Name, date_time, user_state) VALUES(?, ?, ?, ?)
        """
        self.execute(sql, parameters=(id, name, date_time, user_state), commit=True)




    def add_current_user(self, id: int):
        """Добавление пользователя в таблицу Currentuser"""
        sql = """INSERT INTO Currentuser(id) VALUES(?)"""
        self.execute(sql, parameters=(id,), commit=True)




    def add_capture(self, sum_text: str):
        """Добавление кода капчи в таблицу Capture"""
        sql = """INSERT INTO Capture(sum_text) VALUES(?)"""
        self.execute(sql, parameters=(sum_text,), commit=True)




    def select_all_users(self):
        """Чтение всей таблицы Users"""
        sql = """
        SELECT * FROM Users
        """
        return self.execute(sql, fetchall=True)




    def select_all_current_user(self):
        """Чтение всей таблицы Currentuser"""
        sql = """
                SELECT * FROM Currentuser
                """
        result = self.execute(sql, fetchall=True)
        return result[0][0]



    def select_all_capture(self):
        """Чтение всей таблицы Capture"""
        sql = """SELECT * FROM Capture"""
        result = self.execute(sql, fetchall=True)
        return result[0][0]







    def select_block_users(self):
        """Вывод заблокированных пользователей - возвращает список id"""
        sql = """
        SELECT * FROM Users WHERE user_state=True
        """
        list_tup = self.execute(sql, fetchall=True)
        list_id = [item[0] for item in list_tup]
        return list_id





    def select_users_id(self):
        """Выборка всех id пользователей в список"""
        sql = "SELECT id FROM Users;"
        list_tup = self.execute(sql, fetchall=True)
        list_id = [item[0] for item in list_tup]
        return list_id




    def select_user(self, **kwargs):
        """Выбор одной колонки из таблицы"""
        # SQL_EXAMPLE = "SELECT * FROM Users where id=1 AND Name='John'"
        sql = "SELECT * FROM Users WHERE "
        sql, parameters = self.format_args(sql, kwargs)

        return self.execute(sql, parameters=parameters, fetchone=True)




    def count_users(self):
        """Подсчет пользователей в таблице"""
        count = self.execute("SELECT COUNT(*) FROM Users;", fetchone=True)
        return count[0]




    def update_user_name(self, Name, id):
        """Изменяем имя пользователя Name в таблице"""
        # SQL_EXAMPLE = "UPDATE Users SET Name=name WHERE id=12345"

        sql = f"""
        UPDATE Users SET Name=? WHERE id=?
        """
        return self.execute(sql, parameters=(Name, id), commit=True)




    def update_user_state(self, id, state: bool = False):
        """Изменяем состояние (block/unblock) пользователя id в таблице"""
        # SQL_EXAMPLE = "UPDATE Users SET user_state=state WHERE id=12345"

        sql = f"""
        UPDATE Users SET user_state=? WHERE id=?
        """
        return self.execute(sql, parameters=(state, id), commit=True)



    def delete_one_user(self, id):
        """Удаляем запись отдельного пользователя по id"""
        sql = f"""DELETE FROM Users WHERE id=?"""
        return self.execute(sql, parameters=(id,), commit=True)




    def delete_users(self):
        """Очистка таблицы Users"""
        self.execute("DELETE FROM Users WHERE TRUE", commit=True)




    def delete_current_user(self):
        """Очистка таблицы Currentuser"""
        self.execute("DELETE FROM Currentuser WHERE TRUE", commit=True)




    def delete_capture(self):
        """Очистка таблицы Capture"""
        self.execute("DELETE FROM Capture WHERE TRUE", commit=True)




def logger(statement):
    """Логирование"""
    print(f"""
_____________________________________________________        
Executing: 
{statement}
_____________________________________________________
""")
