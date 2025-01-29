import sqlite3


class Database:
    def __init__(self, path: str):
        self.path = path

    def create_tables(self):
        with sqlite3.connect(self.path) as connection:
            cursor = connection.cursor()
            cursor.execute('''
            CREATE TABLE IF NOT EXISTS reviews(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                phone_number TEXT,
                date DATE,
                rate INTEGER,
                extra_comments TEXT
            )
            ''')
            cursor.execute('''
            CREATE TABLE IF NOT EXISTS dishes(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                price FLOAT,
                description TEXT,
                category TEXT,
                options TEXT,
                image TEXT
                )
            ''')

    def save_review(self, data: dict):
        with sqlite3.connect(self.path) as connection:
            cursor = connection.cursor()
            cursor.execute(
            '''
            INSERT INTO reviews (name, phone_number, date, rate, extra_comments)
            VALUES(?, ?, ?, ?, ?)
            ''',
                (data['name'], data['phone_number'], data['date'], data['rate'], data['extra_comments'])
            )

    def save_dish(self, data: dict):
        with sqlite3.connect(self.path) as connection:
            cursor = connection.cursor()
            cursor.execute('''
            INSERT INTO dishes (name, price, description, category, options, image)
            VALUES(?, ?, ?, ?, ?, ?)
            ''',
            (data['name'], data['price'], data['description'], data['category'], data['options'], data['image'])
            )

    def get_all_dishes(self):
        with sqlite3.connect(self.path) as connection:
            cursor = connection.cursor()
            result = cursor.execute('SELECT name, price, description, category, options, image FROM dishes')
            result.row_factory = sqlite3.Row
            data = result.fetchall()
            return [dict(row) for row in data]