from flask import Flask, request, render_template, redirect, url_for
import psycopg2

#Connect to database
conn = psycopg2.connect("dbname = webdb user = postgres password = postgres")
cur = conn.cursor()

#Setup flask
app = Flask(__name__)

#Key used for encrypting session data
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

#Check if username is in database, True if username exists
def existingUser(username):
	cur.execute("SELECT * FROM users WHERE username = %s;", [username])
	if(len(cur.fetchall()) > 0):
		return True
	return False

#Home page
@app.route("/")
def home():
    return "Hello World!"

#Login page
@app.route("/login", methods = ["POST"])
def login():
	if(request.method == "POST"):
		username = request.form("username")
		password = request.form("password")

		#If the username doesn't exist, return error
		if(existingUser(username) == False):
			pass
		#If the username does exist, check the password and login
		elif:
			cur.execute("SELECT * FROM users WHERE username = %s;", [username])
			info = cur.fetchone()
			#If the passwords match
			if(info[2] == password):
				session["username"] = username
				return redirect(url_for("home"))

	return render_template("Login.html")

#Register page
@app.route("/register", methods = ["POST"])
def register():
	if(request.method == "POST"):
		username = request.form("username")
		password = request.form("password")

		#If the username exists, return error
		if(existingUser(username) == True):
			pass
		#If the username doesn't exist, register
		elif:
			cur.execute("INSERT INTO users (username, password) VALUES (%s, %s);", [username, password])
			conn.commit()
			session["username"] = username
			return redirect(url_for("home"))

	return render_template("Register.html")

if __name__ == "__main__":
    app.run(debug = True)