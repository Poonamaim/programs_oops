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

    def select(self, tablename, select_column):
        query_select = "SELECT {1} from {0} ".format (tablename, select_column)
        cur = self.con.cursor ()
        cur.execute (query_select)
        row = cur.fetchall ()
        for i in row:
            print (i)

        print ("table is selected")


c = Connections('localhost','oops_db','root','sumasoft123')
'''mydict3 = {
    "tableName":"employee",
    "colmnsOfTable":"ID,Name",
    "valuesForColumns":"4,'poonam'"
}
c.insert_into_table(mydict3)
'''
'''mydict2 = {
    "tableName":"employee",
    "colmnsOfTable":"ID,Name",
    "valuesForColumns":"6,'seema'"

}
c.insert_into_table(mydict2)'''

mydict2 = {
    "tableName": "employee",
    "colmnsOfTable": "ID,Name",
    "valuesForColumns": "8,'sohit'"

}
c.insert_into_table (mydict2)



