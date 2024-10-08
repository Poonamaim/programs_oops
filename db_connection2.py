'''import mysql.connector


class Databases:
    def __init__(self, data):
        # print(data)
        self.host = data[0]
        self.user = data[1]
        self.password = data[2]
        self.db = data[3]
        self.query = data[4]
        mydb = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.db
        )
        cursor = mydb.cursor()
        cursor.execute(self.query)
        myresult = cursor.fetchall()
        print(myresult)

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host = self.host,
                user =self.user,
                password =self.password,
                database = self.database
            )
            if self.connection.is_connected():
                print("sucessfuly connected from database")
        except mysql.connector.Error as err:
            print(f"Error: {err}")
'''
# importing required library
import mysql.connector

# connecting to the database
dataBase = mysql.connector.connect(
    host="localhost",
    user="user",
    passwd="sumasoft123",
    database="mydb")

# preparing a cursor object
cursorObject = dataBase.cursor()

# creating table
studentRecord = """CREATE TABLE STUDENT ( 
                   NAME  VARCHAR(20) NOT NULL, 
                   BRANCH VARCHAR(50), 
                   ROLL INT NOT NULL,
                   SECTION VARCHAR(5), 
                   AGE INT
                   )"""

# table created
cursorObject.execute(studentRecord)

# disconnecting from server
dataBase.close()


