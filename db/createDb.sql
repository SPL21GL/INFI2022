create database if not exists todoApp;
use todoApp;

create table if not exists todoItems (
	itemId int auto_increment unique key primary key,
	title varchar (120),
	description text,
	dueDate date,
	isDone boolean
);

INSERT INTO `todoapp`.`todoitems`
(`title`,
`description`,
`dueDate`,
`isDone`)
VALUES
("mein erstes item",
"das ist ein wichtiges item",
"2022-02-27",
0);
