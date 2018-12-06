
import os
from flask import Flask, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename


UPLOAD_FOLDER = os.path.dirname(os.path.abspath(__file__))
ALLOWED_EXTENSIONS = set(['pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__, static_folder = "Uploads")
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

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


@app.route('/')
def welcome():
    return render_template('ImageUploadog.html')  # render a template

if __name__ == '__main__':
    app.run(debug=True)
