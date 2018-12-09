from flask import Flask, request, render_template, redirect, url_for, session, send_from_directory
import psycopg2
import os

#Connect to database
conn = psycopg2.connect("dbname='webdb' user='postgres' password='postgres'")
cur = conn.cursor()

#Setup flask
app = Flask(__name__)
UPLOAD_FOLDER = os.path.dirname(os.path.abspath(__file__))
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

#Check if username is in database, True if username exists
def existingUser(username):
	cur.execute("SELECT * FROM users WHERE username = %s;", [username])
	if(len(cur.fetchall()) > 0):
		return True
	return False
	
#Navigation routing
@app.route('/Images')
def images():
	#If user isn't signed in, redirect
		if(session["username"] == ""):
			return redirect(url_for("login"))
	return render_template("Images.html")

@app.route('/Tags')
def tags():
	#If user isn't signed in, redirect
		if(session["username"] == ""):
			return redirect(url_for("login"))
	return render_template("Tags.html")

@app.route('/Search', methods = ["POST", "GET"])
def searchpage():
	#If user isn't signed in, redirect
		if(session["username"] == ""):
			return redirect(url_for("login"))
	return render_template("Search.html")

@app.route('/Upload')
def upload():
	#If user isn't signed in, redirect
		if(session["username"] == ""):
			return redirect(url_for("login"))
	return render_template("Upload.html")

#Login page
@app.route("/", methods = ["GET", "POST"])
def login():
	if(request.method == "POST"):
		username = request.form["username"]
		password = request.form["password"]

		#If the username doesn't exist, return error
		if(existingUser(username) == False):
			return render_template("Login.html", error="Not a username")
		#If the username does exist, check the password and login
		else:
			cur.execute("SELECT * FROM users WHERE username = %s;", [username])
			info = cur.fetchone()
			#If the passwords match
			if(info[1] == password):
				session["username"] = username
				return redirect(url_for("images"))
			else:
				return render_template("Login.html", error="Wrong password")

	return render_template("Login.html")

#Register page
@app.route("/register", methods = ["GET", "POST"])
def register():
	if(request.method == "POST"):
		username = request.form["username"]
		password = request.form["password"]

		#If the username exists, return error
		if(existingUser(username) == True):
			return render_template("Resister.html", error="Already an account")
		#If the username doesn't exist, register
		else:
			cur.execute("INSERT INTO users (username, password) VALUES (%s, %s);", [username, password])
			conn.commit()
			return render_template("Register.html", registered="Created an account")

	return render_template("Register.html")

#Logout page
@app.route("/logout")
def logout():
	session["username"] = ""
	return redirect(url_for("login"))

#Uploading the file to a static folder
@app.route("/upload", methods = ["GET", "POST"])
def upload_file():
	if(request.method == "POST"):
		#If user isn't signed in, redirect
		if(session["username"] == ""):
			return redirect(url_for("login"))

		#Get tags
		tags = request.form["tags"]
		tags = tags.split(",")

		target = os.path.join(UPLOAD_FOLDER, "static/")
		print(target)
		print(tags)

		if not os.path.isdir(target):
			os.mkdir(target)

		for upload in request.files.getlist("file"):
			filename = upload.filename
			#Add the picname and return the id
			cur.execute("INSERT INTO pictures (picname, username) VALUES (%s, %s) RETURNING picid;", [filename, session["username"]])
			id = cur.fetchone()
			conn.commit()

			#For every tag insert with picid
			for tag in tags:
				cur.execute("INSERT INTO tags (picid, tag) VALUES (%s, %s);", [id, tag])
			conn.commit()

			#Save image
			destination = "/".join([target,id + ', ' + session["username"]])
			upload.save(destination)

	return render_template("Login.html")

#Location of the image
@app.route("/upload/<filename>")
def send_image(filename):
  return send_from_directory("static",filename)

if __name__ == "__main__":
	#Key used for encrypting session data
	app.secret_key = os.urandom(24)
	app.run()