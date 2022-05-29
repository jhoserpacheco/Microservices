-- Debe creare la base de datos en postgresql con los siguientes parametros,

-- Nombre de base de datos	=any_name
-- Nombre del servidor		=localhost
-- Nombre del usuario		=your_user
-- Contraseña del usuario	=your_password

-- Luego estos mismos definirlos en el archivo .env de la siguiente manera:

-- DBNAME=any_name
-- DBHOST=localhost
-- DBUSER=your_user
-- DBPASS=your_password

-- El proposito es simular la base de datos de la biblioteca

drop table if exists users;
drop table if exists roles;

create table roles(
	role_id SERIAL PRIMARY KEY,
	rol VARCHAR
);

create table programs(
	program_id SERIAL PRIMARY KEY,
	program_name VARCHAR
);

create table users(
	user_id SERIAL PRIMARY KEY,
	role_id INT,
	program_id INT,
	email VARCHAR,
	FOREIGN KEY(role_id) REFERENCES roles(role_id),
	FOREIGN KEY(program_id) REFERENCES programs(program_id)
);

INSERT INTO programs (program_name) VALUES 
('Ingenieria de Sistemas'), 
('Ingenieria de Minas'),
('Ingenieria Civil'),
('Ingenieria Electronica'),
('Ingenieria Industrial');

INSERT INTO roles(rol) VALUES ('STAFF'), ('DOCENTE'), ('PREGRADO'), ('ANY_OTHER');

INSERT INTO users(email, role_id, program_id) VALUES 
('stiwardjherikofcr@ufps.edu.co', 1, 1),
('stiwardjherikofcr@ufps.edu.co', 3, 1),
('ronaldeduardobm@ufps.edu.co', 1, 1),
('ronaldeduardobm@ufps.edu.co', 3, 1),
('jhoserfabianpq@ufps.edu.co', 3, 1),
('rojassachicadf@ufps.edu.co', 3, 1),
('madarme@ufps.edu.co', 1, 1),
('madarme@ufps.edu.co', 2, 1);