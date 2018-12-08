from flask import Flask, request, render_template, redirect, url_for, session, send_from_directory
import psycopg2
import os

#Connect to database
conn = psycopg2.connect("host='localhost' dbname='webdb' user='postgres' password='postgres'")
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
	return render_template("Images.html")

@app.route('/Tags')
def tags():
	return render_template("Tags.html")

@app.route('/Search', methods = ["POST", "GET"])
def searchpage():
	return render_template("Search.html")

@app.route('/Upload')
def upload():
	return render_template("Upload.html")

#Login page
@app.route("/", methods = ["GET", "POST"])
def login():
	if(request.method == "post"):
		username = request.form("username")
		password = request.form("password")

		#If the username doesn't exist, return error
		if(existingUser(username) == False):
			return render_template("Login.html", error = "Not an account")
		#If the username does exist, check the password and login
		else:
			cur.execute("SELECT * FROM users WHERE username = %s;", [username])
			info = cur.fetchone()
			#If the passwords match
			if(info[2] == password):
				session["username"] = username
				return redirect('/Images')

	return render_template("Login.html")

#Register page
@app.route("/register", methods = ["GET", "POST"])
def register():
	if(request.method == "POST"):
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
			return redirect(url_for("\Register"))

	return render_template("Register.html")

#Uploading the file to a static folder
@app.route('/upload', methods = ['GET', 'POST'])
def upload_file():
  target = os.path.join(UPLOAD_FOLDER, 'static/')

  if not os.path.isdir(target):
    os.mkdir(target)

  for upload in request.files.getlist("file"):
    filename = upload.filename
    destination = "/".join([target,filename])
    upload.save(destination)

  return render_template("ImageDisplay.html", image_name = filename)

#Location of the image
@app.route('/upload/<filename>')
def send_image(filename):
  return send_from_directory("static",filename)

if __name__ == "__main__":
	#Key used for encrypting session data
	app.secret_key = os.urandom(24)
	app.run()