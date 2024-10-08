import mysql.connector as conn
from mysql.connector import Error


class Connections:
    def __init__(self , hostname,dbname ,username,password):
        try:
            self.con = conn.connect(host = hostname,database=dbname,user=username,password=password)
            print("connection is succesfully ")
        except Error as E:
            print ("Error")

    def insert_into_table(self,dictForInsert):
        insert_query = "INSERT INTO "+ dictForInsert["tableName"] + "(" + dictForInsert["colmnsOfTable"] + ") VALUES (" + dictForInsert["valuesForColumns"] +")"
        cur = self.con.cursor()
        cur.execute(insert_query)
        self.con.commit()
        print("data insert")

c = Connections('localhost','oops_db','root','sumasoft123')
mydict = {
    "tableName":"employee_new1",
    "colmnsOfTable":"ID,Name",
    "valuesForColumns":"5,'pooja'"
}

mydict2 = {
    'tablename': "employee2",
    'columnofTable': "ID,name",
    "valuesforColumn": "4,'poonam"
}
c.insert_into_table(mydict)