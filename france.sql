create database france;
use	france;

create table player(
kit_number int(2) not null primary key,
player_name char(50),
nationality char(50),
date_of_birth char(50),
staff_position char(50)
);

create table staff(
staff_id char(30) not null primary key,
staff_name char(50),
nationality char(50),
staff_position char(30),
);


create table sponsor(
sponsor_name char(50) not null primary key,
contract_value char(50),
duration int(2),
note char(50)
);

create table activity_log(
activity char(200),
datea char(50)
);


insert into player(kit_number, player_name,nationality, date_of_birth, staff_position) values (01, 'Alphonse Areola', 'France', '27 February 1993', 'Goal Keeper');
insert into player(kit_number, player_name,nationality, date_of_birth, staff_position) values (02, 'Benjamin Pavard', 'France', '28 March 1996', 'Defender');
insert into player(kit_number, player_name,nationality, date_of_birth, staff_position) values (03, 'Presnel Kimpembe', 'France', '13 August 1995', 'Defender');
insert into player(kit_number, player_name,nationality, date_of_birth, staff_position) values (04, 'Raphael Varane', 'France', '25 April 1993 ', 'Defender');
insert into player(kit_number, player_name,nationality, date_of_birth, staff_position) values (05, 'Clément Lenglet', 'France', '17 June 1995', 'Defender');
insert into player(kit_number, player_name,nationality, date_of_birth, staff_position) values (06, 'Tanguy Ndombele', 'France', '28 December 1996', 'Midfielder');
insert into player(kit_number, player_name,nationality, date_of_birth, staff_position) values (07, 'Antoine Griezmann', 'France', '21 March 1991', 'Forward');
insert into player(kit_number, player_name,nationality, date_of_birth, staff_position) values (08, 'Thomas Lemar', 'France', '12 November 1995 ', 'Forward');
insert into player(kit_number, player_name,nationality, date_of_birth, staff_position) values (09, 'Olivier Giroud', 'France', '30 September 1986', 'Forward');
insert into player(kit_number, player_name,nationality, date_of_birth, staff_position) values (10, 'Kylian Mbappé', 'France', '20 December 1998', 'Forward');
insert into player(kit_number, player_name,nationality, date_of_birth, staff_position) values (11, 'Kingsley Coman', 'France', '13 June 1996', 'Forward');
insert into player(kit_number, player_name,nationality, date_of_birth, staff_position) values (12, 'Corentin Tolisso', 'France', '3 August 1994', 'Midfielder');
insert into player(kit_number, player_name,nationality, date_of_birth, staff_position) values (13, 'N Golo Kante', 'France', '29 March 1991', 'Midfielder');
insert into player(kit_number, player_name,nationality, date_of_birth, staff_position) values (14, 'Matteo Guendouzi', 'France', '14 April 1999', 'Midfielder');
insert into player(kit_number, player_name,nationality, date_of_birth, staff_position) values (15, 'Kurt Zouma', 'France', '27 October 1994', 'Defender');
insert into player(kit_number, player_name,nationality, date_of_birth, staff_position) values (16, 'Steve Mandanda', 'France', '28 March 1985', 'Goal Keeper');
insert into player(kit_number, player_name,nationality, date_of_birth, staff_position) values (17, 'Moussa Sissoko', 'France', '16 August 1989', 'Midfielder');
insert into player(kit_number, player_name,nationality, date_of_birth, staff_position) values (18, 'Nabil Fekir', 'France', '18 July 1993', 'Forward');
insert into player(kit_number, player_name,nationality, date_of_birth, staff_position) values (19, 'Lucas Digne', 'France', '20 July 1993', 'Defender');
insert into player(kit_number, player_name,nationality, date_of_birth, staff_position) values (20, 'Wissam Ben Yedder', 'France', '12 August 1990', 'Forward');
insert into player(kit_number, player_name,nationality, date_of_birth, staff_position) values (21, 'Leo Dubois', 'France', '14 September 1994', 'Defender');
insert into player(kit_number, player_name,nationality, date_of_birth, staff_position) values (22, 'Benjamin Mendy', 'France', '17 July 1994', 'Defender');
insert into player(kit_number, player_name,nationality, date_of_birth, staff_position) values (23, 'Mike Maignan', 'France', '3 July 1995', 'Goal Keeper');

insert into staff(staff_id,staff_name, nationality,staff_position,salary ) values ('C1', 'Nguyễn Trọng Chiến','Việt Nam','President','*');


insert into sponsor(sponsor_name, contract_value, duration,note) values ('Kappa','5.000.000.000','5','Kit logo');

