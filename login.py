from flask import Flask, request, render_template, redirect, url_for, session
import psycopg2
import os

#Connect to database
conn = psycopg2.connect("dbname = webdb user = postgres password = postgres")
cur = conn.cursor()

#Setup flask
app = Flask(__name__)

#Check if username is in database, True if username exists
def existingUser(username):
	cur.execute("SELECT * FROM users WHERE username = %s;", [username])
	if(len(cur.fetchall()) > 0):
		return True
	return False

#Home page
@app.route("/")
def home():
	string = "Logged in as " + session["username"]
	return string

#Login page
@app.route("/login", methods = ["POST", "GET"])
def login():
	if(request.method == "GET"):
		username = request.args.get("username")
		password = request.args.get("password")

		#If the username doesn't exist, return error
		if(existingUser(username) == False):
			print("Hello")
		#If the username does exist, check the password and login
		else:
			cur.execute("SELECT * FROM users WHERE username = %s;", [username])
			info = cur.fetchone()
			#If the passwords match
			if(info[2] == password):
				session["username"] = username
				return redirect(url_for("home"))

	return render_template("Login.html")

#Register page
@app.route("/register", methods = ["POST", "GET"])
def register():
	if(request.method == "GET"):
		username = request.args.get("username")
		password = request.args.get("password")

		#If the username exists, return error
		if(existingUser(username) == True):
			print("Hello")
		#If the username doesn't exist, register
		else:
			cur.execute("INSERT INTO users (username, password) VALUES (%s, %s);", [username, password])
			conn.commit()
			session["username"] = username
			return redirect(url_for("home"))

	return render_template("Register.html")

if __name__ == "__main__":
	#Key used for encrypting session data
	app.secret_key = os.urandom(24)
	app.run()