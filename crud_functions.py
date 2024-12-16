import sqlite3
from itertools import product


def initiate_db():
    connection = sqlite3.connect("Products.db")
    cursor = connection.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products(
            id INTEGER PRIMARY KEY,
            title TEXT NOT NULL,
            description TEXT,
            price INTEGER NOT NULL    
        )
        ''')
    connection.commit()


def get_all_products():
    connection = sqlite3.connect("Products.db")
    cursor = connection.cursor()
    products = cursor.execute("SELECT * FROM Products").fetchall()
    connection.commit()
    connection.close()
    return products


def add_product(id, title, description, price):
    connection = sqlite3.connect("Products.db")
    cursor = connection.cursor()
    check_product = cursor.execute("SELECT * FROM Products WHERE id=?", (id,))

    if check_product.fetchone() is None:
        cursor.execute(f'''
    INSERT INTO Products VALUES(
        '{id}', '{title}', '{description}', '{price}')
''')
    connection.commit()

initiate_db()
add_product(1, 'Набор А', 'Подходит для энергии', 400)
add_product(2, 'Набор Б', "Подходит для силы", 500)
add_product(3, 'Набор В', "Подходит для диеты", 600)
add_product(4, 'Набор Г', 'Подходит для зрения', 200)




