drop table if exists entries;
create table entries (
	id 		serial primary key,
	title 	text not null,
	str 	text not null
);