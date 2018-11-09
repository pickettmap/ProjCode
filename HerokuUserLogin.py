"""
Dylan Bossie

This script links input from HTML with the Heroku database
"""

import os
import psycopg2
import urllib.parse as urlparse
import pdb

from flask import Flask, render_template, redirect, url_for, request


########################################################
###### Sample Scripts (not used in deployment)
########################################################
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
########################################################


###### Step 1: Connect with Heroku database
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

###### Create new user
def addUser(newuser,newpass):
    maxid = cur.execute("select max(userid) from users;")
    maxid = cur.fetchall()
    maxid = maxid[0][0]
    cur.execute("insert into users (userid,usern,password) values (%s,%s,%s);",
                (maxid+1,newuser,newpass))
    conn.commit()
    return
    
###### Step 2. Receive user input from login HTML page
app = Flask(__name__)
app.run(environ.get('PORT'))

@app.route('/Login', methods=['GET', 'POST'])
def login():
    receivedUsername = request.args.get('username')
    receivedPassword = request.args.get('password')
    if receivedUsername != None and receivedPassword != None:
        print("Received Username: ", receivedUsername)
        print("Received Password: ", receivedPassword)
        userCheck = userAuthentication(receivedUsername,receivedPassword,cur,conn)
        if userCheck == True:
            print('Login accepted. Accessing image upload page...')
            return render_template('ImageUpload.html')
    return render_template('Login.html')

###### Step 3. Authenticate user input through Heroku user database
def userAuthentication(username,password,cur,conn):
    cur.execute("select * from users where usern=%s",[username])
    userData = cur.fetchall()
    if userData == []:
        while True:
            createUser = input("Username not found. Create new user? [Y/N]")
            if createUser == 'Y' or createUser == 'N':
                break
        if createUser == 'Y':
            addUser(username,password)
            return False
        else:
            return False
    if userData[0][1] == username and userData[0][2] == password:
        print("User authenticated. Logging into user page...")
        return True
    print("Incorrect password.")


###### Render login page
@app.route('/Login')
def welcome():
    return render_template('Login.html')  # render a template

###### Step 0. Initialize server
if __name__ == '__main__':
    #### Connect to Heroku database
    conn,cur = databaseConnect()
    app.run(debug=True)