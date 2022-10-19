-- -----------------------------------------------------
--  WARNING
-- By default, this script is using `asp` database name
-- If it's necessary, change it into #8
-- and don't forget to change ['DB_NAME'] into .env file
-- -----------------------------------------------------

USE asp;

INSERT INTO `post_category`
	(name)
VALUES
    ('Doar'),
    ('Adotar'),
    ('Venda'),
    ('Compra'),
    ('Achado'),
    ('Perdido');

INSERT INTO `post`
	(title, description, post_category)
VALUES
	('Dalmata', 'Atende pelo nome de Jessie, super carinhoso', 1),
    ('Calopsita', 'Bem comunicativo', 1),
    ('Qualquer gatinho', 'Moro sozinho e quero adotar um gatinho', 2),
    ('Caramelo', 'Achei um caramelo perdido na 410 norte', 5),
    ('Scooby-doo', 'Scooby-doo cade voce meu filho?', 6);

INSERT INTO `post_image`
	(image_url, post_id)
VALUES
	('https://i.imgur.com/6F3S5Yz.jpeg', 5);