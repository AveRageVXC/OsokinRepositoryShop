CREATE TABLE users("id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, "name" TEXT NOT NULL, "surname" TEXT NOT NULL, "login" TEXT UNIQUE NOT NULL, "password" BIGINT NOT NULL, "telephone" TEXT UNIQUE NOT NULL, "date_of_registration" TEXT NOT NULL);
CREATE TABLE products_in_cart("id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, "user_id" INTEGER NOT NULL, "products_id" INTEGER NOT NULL, "quantity" INTEGER NOT NULL, "order_id" INTEGER);
CREATE TABLE products("id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, "name" TEXT NOT NULL, "price" INTEGER NOT NULL, "quantity" INTEGER NOT NULL);
CREATE TABLE orders("id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, "user_id" INTEGER NOT NULL, "cost" INTEGER NOT NULL, "provider" TEXT, "status" TEXT NOT NULL);

INSERT INTO users (name, surname, login, password, telephone, date_of_registration) VALUES ("Ваня", "Иванов", "vanyaivanov@mail.ru", 12312314313, "+79174357634", "2019.12.03");
INSERT INTO users (name, surname, login, password, telephone, date_of_registration) VALUES ("Пётр", "Чортов", "petya123@mail.ru", 542345341, "+79165434565", "2016.10.14");
INSERT INTO users (name, surname, login, password, telephone, date_of_registration) VALUES ("Аделина", "Борисова", "tebyalublya@mail.ru", 92304234233, "+79169876677", "2011.01.23");
	
INSERT INTO products_in_cart (user_id, products_id, quantity, order_id) VALUES (2, 1, 3, NULL);
INSERT INTO products_in_cart (user_id, products_id, quantity, order_id) VALUES (1, 2, 2, 2);
INSERT INTO products_in_cart (user_id, products_id, quantity, order_id) VALUES (1, 3, 1, 2);


INSERT INTO products (name, price, quantity) VALUES ("RTX3070", 100023, 1900);
INSERT INTO products (name, price, quantity) VALUES ("RTX3080", 120120, 809);
INSERT INTO products (name, price, quantity) VALUES ("RTX3090", 189999, 412);


INSERT INTO orders (user_id, cost, provider, status) VALUES (1, 189999, "VISA", "REJECTED");
INSERT INTO orders (user_id, cost, provider, status) VALUES (1, 120000, "MASTERCARD", "OK");
INSERT INTO orders (user_id, cost, provider, status) VALUES (3, 100000, "VISA", "REJECTED");