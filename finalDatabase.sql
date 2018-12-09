create database webdb;
\c myDatabase;

create table users(userName varchar(16) not null, password varchar(16) not null);
insert into Users (userName,password) values('user1','123'),('user2','password111'),('user3','CUBoulder');

create table pictures(picid serial primary key, picname varchar(30), userName varchar(16) not null);
create table tags(picid picID int references pictures (picid) on update cascade, tag varchar(30));
