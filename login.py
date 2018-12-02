from flask import Flask, request, render_template
import psycopg2

#Connect to database
conn = psycopg2.connect("dbname = webdb user = postgres password = postgres")
cur = conn.cursor()

#Setup flask
app = Flask(__name__)

#Check if user is in database, True if username already exists
def validateUser(username):
	cur.execute("SELECT * FROM users WHERE username = %s;", [username])
	if(len(cur.fetchall()) > 0):
		return True
	return False

#Adds user entry
def addUser(username, password):
	cur.execute("INSERT INTO users (username, password) VALUES (%s, %s);", [username, password])
	conn.commit()

#Home page
@app.route("/")
def hello():
    return "Hello World!"

#Login page
@app.route("/login", methods = ["POST", "GET"])
def login():
	if(request.method == "GET"):
		if(len(request.args) > 0):
			username = request.args.get("username")
			password = request.args.get("password")

			#If the username doesn't exist, add the new account
			if(validateUser(username) == False):
				addUser(username, password)
	return render_template("Login.html")

if __name__ == "__main__":
    app.run(debug=True)