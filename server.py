from flask import Flask
from markupsafe import escape
import pymysql

host = "cse-hackathon-mysql5.cydmwhbjjajj.us-west-2.rds.amazonaws.com"
port = 3308
dbname = "csusb"
user = "root"
password = "nullvoid"

conn = pymysql.connect(host, user=user, port=port, passwd=password, db=dbname)
cursor = conn.cursor()

app = Flask(__name__)

@app.route('/')
def check():
    return "hello test"

@app.route('/checkuser/<SF>/<userid>/<password>')
def checkUser(SF, userid, password):
    try:
        int(userid)

        #return "user id is acceptable"
    except ValueError:
        return "user id is not acceptable"
    print(SF, userid, password)
    #return "SELECT password FROM faculty WHERE username='"+str(userid)+"'"
    cursor.execute("SELECT password FROM faculty WHERE username='"+str(userid)+"'")
    data = cursor.fetchall()
    return data[0][0]
    if SF == "faculty":
        pass

