
import cgi

form = cgi.FieldStorage()

username = form.getvalue('user')
password = form.getvalue('pass')
