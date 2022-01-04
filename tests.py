import unittest, sqlite3

class TestTesting(unittest.TestCase):
    def setUp(self):
        self.db = sqlite3.connect(":memory:")
        self.cursor = self.db.cursor()
        self.cursor.executescript(
            """
            BEGIN TRANSACTION;
            CREATE TABLE users("id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, "name" TEXT NOT NULL, "surname" TEXT NOT NULL, "login" TEXT UNIQUE NOT NULL, "password" BIGINT NOT NULL, "telephone" TEXT UNIQUE NOT NULL, "date_of_registration" TEXT NOT NULL, "birth_date" TEXT NOT NULL);
            INSERT INTO users VALUES(1,'Ваня','Иванов','vanyaivanov@mail.ru',12312314313,'+79174357634','2019.12.03','1999.12.30');
            INSERT INTO users VALUES(2,'Пётр','Чортов','petya123@mail.ru',542345341,'+79165434565','2016.10.14','1998.05.12');
            INSERT INTO users VALUES(3,'Аделина','Борисова','tebyalublya@mail.ru',92304234233,'+79169876677','2011.01.23','1976.10.24');
            CREATE TABLE products_in_cart("id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, "user_id" INTEGER NOT NULL, "products_id" INTEGER NOT NULL, "quantity" INTEGER NOT NULL, "order_id" INTEGER);
            INSERT INTO products_in_cart VALUES(1,2,1,3,NULL);
            INSERT INTO products_in_cart VALUES(2,1,2,2,2);
            INSERT INTO products_in_cart VALUES(3,1,3,1,2);
            CREATE TABLE products("id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, "name" TEXT NOT NULL, "price" INTEGER NOT NULL, "quantity" INTEGER NOT NULL);
            INSERT INTO products VALUES(1,'RTX3070',100023,1900);
            INSERT INTO products VALUES(2,'RTX3080',120120,809);
            INSERT INTO products VALUES(3,'RTX3090',189999,412);
            CREATE TABLE orders("id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, "user_id" INTEGER NOT NULL, "cost" INTEGER NOT NULL, "provider" TEXT, "status" TEXT NOT NULL);
            INSERT INTO orders VALUES(1,1,189999,'VISA','REJECTED');
            INSERT INTO orders VALUES(2,1,120000,'MASTERCARD','OK');
            INSERT INTO orders VALUES(3,3,100000,'VISA','REJECTED');
            DELETE FROM sqlite_sequence;
            INSERT INTO sqlite_sequence VALUES('users',3);
            INSERT INTO sqlite_sequence VALUES('products_in_cart',3);
            INSERT INTO sqlite_sequence VALUES('products',3);
            INSERT INTO sqlite_sequence VALUES('orders',3);
            COMMIT;
            """
        )
    def test_Login(self):
        login = "vanyaivanov@mail.ru"
        password = 12312314313

        self.cursor.execute('''
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
                    '''.format(login, password))
        # print(self.cursor.fetchall())
        self.assertEqual(str(self.cursor.fetchall()),
                         "[(1, 'Ваня', 'Иванов', 'vanyaivanov@mail.ru', '+79174357634', '2019.12.03', '1999.12.30')]")

    def test_Products(self):
        self.cursor.execute('''
            SELECT
                id AS id,
                name AS name,
                price AS price,
                quantity AS quantity
            FROM products;
            '''
        )
        self.assertEqual(len(self.cursor.fetchall()), 3)

    def test_cart(self):
        user_id = 2
        self.cursor.execute('''
                SELECT
                    id AS id,
                    products_id AS products_id,
                    quantity AS quantity
                FROM products_in_cart
                WHERE products_in_cart.user_id = {0} AND products_in_cart.order_id IS NULL;
                '''.format(user_id)
            )
        self.assertEqual(str(self.cursor.fetchall()), "[(1, 1, 3)]")
        
if __name__ == '__main__':
    unittest.main(failfast=False)