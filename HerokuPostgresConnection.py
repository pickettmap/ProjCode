"""
Dylan Bossie

This script sets up the Heroku PostgreSQL database for the squad
"""

import os
import psycopg2
import pdb

def databaseConnect():
    #### Define database to connect with
    
    #### Heroku database link
    #DATABASE_URL = 'postgres://arefdyrarburam:ee3159df93a3d1dda07edfd5c47f23801ac564\
    #f372b36ee4df0dc6816e2b0d27@ec2-54-235-73-241.compute-1.amazonaws.com:5432/daqi\
    #oekmq4n086'
    
    DATABASE_URL = os.environ['DATABASE_URL']
    
    #### Open connection and interaction cursor
    conn = psycopg2.connect(DATABASE_URL,sslmode='require')
    cur = conn.cursor()
    return conn,cur

conn,cur = databaseConnect()

#### Example of pulling data from table
#cur.execute("select * from users")
#print(cur.fetchall())

#### Example of inserting data into a table
cur.execute("insert into users (userid,usern,password) values (%s,%s,%s);",
            (6,'thiccboi','123'))
conn.commit()
pdb.set_trace()

cur.execute("create table Pictures(picID serial primary key, picName varchar(50) not null);")

cur.execute("create table Tags(tagID serial primary key, tagName varchar(50) not null);")

cur.execute("create table PicturesTags(picID int references Pictures (picID) on update cascade, "
	"tagID int references Tags (tagID) on update cascade);")


conn.close()