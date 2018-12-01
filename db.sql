create table Users(userID serial primary key, userName varchar(30) not null, password varchar(100) not null);
insert into Users (userID,userName,password) values(DEFAULT,'user1','123'),(DEFAULT,'user2','password111'),(DEFAULT,'user3','CUBoulder');

create table Pictures(picID serial primary key, picName varchar(50) not null, userID int references Users (userID) on update cascade);
insert into Pictures (picID,picName,userID) values (DEFAULT,'jpeg.jpeg','1'),(DEFAULT,'mom.jpeg','1'),(DEFAULT,'001.jpeg','1'),
                (DEFAULT,'002.jpeg','2'),(DEFAULT,'003.jpeg','2'),(DEFAULT,'004.jpeg','2'),
                (DEFAULT,'005.jpeg','3'),(DEFAULT,'006.jpeg','3'),(DEFAULT,'CU.jpeg','3');


create table Tags(tagID serial primary key, tagName varchar(50) not null);
insert into Tags (TagID, TagName) values (DEFAULT,'mom'),(DEFAULT,'selfie'),(DEFAULT,'me'),(DEFAULT,'Chip');

create table PicturesTags(picID int references Pictures (picID) on update cascade, tagID int references Tags (tagID) on update cascade);
insert into PicturesTags (picID,tagID) values (1,3),(1,4),(2,2),(2,1),(3,3),(4,1),(5,3),(6,1),(6,2),(7,4),(8,3),(9,2);
