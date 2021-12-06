-- Выгрузка данных профиля человека
SELECT 
	id AS id,
	name AS name,
	surname AS surname,
	login AS login,
	telephone AS telephone,
	date_of_registration AS date_of_registration,
	birth_date AS birth_date
FROM users
WHERE users.login = "vanyaivanov@mail.ru" AND users.password = 12312314313;

-- Выгрузка всех имеющихся продуктов

SELECT
	id AS id,
	name AS name,
	price AS price,
	quantity AS quantity
FROM products;

-- Выгрузка корзины человека

SELECT
	id AS id,
	products_id AS products_id,
	quantity AS quantity
FROM products_in_cart
WHERE products_in_cart.user_id = 2 AND products_in_cart.order_id IS NULL;