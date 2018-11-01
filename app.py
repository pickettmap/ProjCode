# import the Flask class from the flask module
from flask import Flask, render_template, redirect, url_for, request
import pdb

# create the application object
app = Flask(__name__)

# use decorators to link the function to a url
@app.route('/Login', methods=['GET', 'POST'])
def login():
    receivedUsername = request.args.get('username')
    receivedPassword = request.args.get('password')
    print("Received Username: ", receivedUsername)
    print("Received Password: ", receivedPassword)
    return render_template('Login.html')

#def home():
#    print('testing 123')
#    return "Hello, World!"  # return a string

@app.route('/Login')
def welcome():
    return render_template('Login.html')  # render a template

# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(debug=True)