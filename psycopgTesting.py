import psycopg2
import pdb
#This stuff will be changed to connect to username/password database
userConnection = psycopg2.connect("dbname='lab6' user='postgres' \
                                          password='user' host='localhost'")
userCursor = userConnection.cursor()

def authenticateUsernamePassword(userCursor,userInput):
    #Assumption here is that front-end has transmitted a username and password
    #input to this program
    user=userInput.username
    password=userInput.password
    userCursor.execute("select * from username where username=user")
    print(userCursor.fetchone())
    pdb.set_trace()
    
userImageCursor,userImageConnection = openImageSQL()

databaseCursor.execute("select * from course")
print(databaseCursor.fetchone())

#Close connections to SQL database and exit program
databaseCursor.close()
databaseConnection.close()