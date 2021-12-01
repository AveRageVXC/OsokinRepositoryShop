UPDATE users SET date_of_registration = substr(date_of_registration, 1, 4) || '-' || substr(date_of_registration, 6, 2) || '-' || substr(date_of_registration, 9, 2);

SELECT login, MAX(date_of_registration) AS 'last_register' FROM users;

SELECT DISTINCT substr(birth_date, 1, 4) FROM users;

SELECT COUNT(*) AS 'total_items' FROM users;

SELECT AVG(2021 - substr(birth_date, 1, 4)) as 'average_age' FROM users WHERE date_of_registration >= date('now', '-2 months');