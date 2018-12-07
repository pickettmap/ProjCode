
import os
from flask import Flask, request, url_for, render_template, send_from_directory


UPLOAD_FOLDER = os.path.dirname(os.path.abspath(__file__))
#ALLOWED_EXTENSIONS = set(['pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

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

#Main Function
@app.route('/')
def welcome():
    return render_template('ImageUploadog.html')  # render a template

#Running the file
if __name__ == '__main__':
    app.run(debug=True)
