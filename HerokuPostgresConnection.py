"""
Dylan Bossie

This script links input from HTML with the Heroku database
"""

import os
import psycopg2
import urllib.parse as urlparse
import pdb

from flask import Flask, render_template, redirect, url_for, request

def databaseConnect():
    #### Heroku database link
    os.environ['DATABASE_URL'] = 'postgres://arefdyrarburam:ee3159df93a3d1dda07edfd5c47f23801ac564f372b36ee4df0dc6816e2b0d27@ec2-54-235-73-241.compute-1.amazonaws.com:5432/daqioekmq4n086'
    url = urlparse.urlparse(os.environ['DATABASE_URL'])
    dbname = url.path[1:]
    user = url.username
    password = url.password
    host = url.hostname
    port = url.port

    #### Open connection and interaction cursor
    conn = psycopg2.connect(dbname=dbname,
                            user=user,
                            password=password,
                            host=host,
                            port=port,sslmode='require')
    cur = conn.cursor()
    return conn,cur

def databaseCreation():
    #### Example of pulling data from table
    cur.execute("select * from users")
    print(cur.fetchall())
    
    #### Example of inserting data into a table
    cur.execute("insert into users (userid,usern,password) values (%s,%s,%s);",
                (6,'thiccboi','123'))
    conn.commit()
    pdb.set_trace()
    
    cur.execute("create table Pictures(picID serial primary key, picName varchar(50) not null);")
    
    cur.execute("create table Tags(tagID serial primary key, tagName varchar(50) not null);")
    
    cur.execute("create table PicturesTags(picID int references Pictures (picID) on update cascade, "
    	"tagID int references Tags (tagID) on update cascade);")
    
def userAuthentication(username,password,cur,conn):
    cur.execute("select * from users where usern=%s",[username])
    userData = cur.fetchall()
    pdb.set_trace()
# create the application object
app = Flask(__name__)

# use decorators to link the function to a url
@app.route('/Login', methods=['GET', 'POST'])
def login():
    receivedUsername = request.args.get('username')
    receivedPassword = request.args.get('password')
    if receivedUsername != None and receivedPassword != None:
        print("Received Username: ", receivedUsername)
        print("Received Password: ", receivedPassword)
        userAuthentication(receivedUsername,receivedPassword,cur,conn)
    return render_template('Login.html')

@app.route('/Login')
def welcome():
    return render_template('Login.html')  # render a template

#### Connect to Heroku database
conn,cur = databaseConnect()

#### Start local server
if __name__ == '__main__':
    app.run(debug=True)