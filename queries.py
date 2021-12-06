import sqlite3

login = "vanyaivanov@mail.ru"
password = 12312314313

connection = sqlite3.connect('DataBase.db')

cursor = connection.cursor()

cursor.execute(
    '''
    SELECT 
	id AS id,
	name AS name,
	surname AS surname,
	login AS login,
	telephone AS telephone,
	date_of_registration AS date_of_registration,
	birth_date AS birth_date
    FROM users
    WHERE users.login = "{0}" AND users.password = {1};
    '''.format(login, password)
)

print(cursor.fetchall())

cursor.execute(
    '''
    SELECT
        id AS id,
        name AS name,
        price AS price,
        quantity AS quantity
    FROM products;
    '''
)

print(cursor.fetchall())

user_id = 2

cursor.execute(
    '''
    SELECT
        id AS id,
        products_id AS products_id,
        quantity AS quantity
    FROM products_in_cart
    WHERE products_in_cart.user_id = {0} AND products_in_cart.order_id IS NULL;
    '''.format(user_id)
)

print(cursor.fetchall())

connection.close()