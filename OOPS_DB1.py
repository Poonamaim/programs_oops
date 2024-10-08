import mysql.connector as conn
from mysql.connector import Error


class Connections:
    def __init__(self , hostname,dbname ,username,password):
        try:
            self.con = conn.connect(host = hostname,database=dbname,user=username,password=password)
            print("connection is succesfully ")
        except Error as E:
            print ("Error")

    def create_table(self, tablename , schema):
        query_create= "CREATE TABLE IF NOT EXISTS {0}({1}".format(tablename,schema)
        cur = self.con.cursor()
        cur.execute(query_create)
        self.con.commit()
        print("table is created")



    def insert_into_table(self , ):
        st = schema.split(',')
        print(st)

        st1 = ''

        for i in st:
            b = i.split('  ')
            st1 = st1 + b[0] + ','
            print(st1)

        schema = st1[:len(st1)-1]





        insert_query= "INSERT INTO student (studentName, FirstName, Age) VALUES ('poonam','gosh', 10)"
        cur = self.con.cursor()
        cur.execute(insert_query)
        self.con.commit()
        print("data insert")


    def select(self , tablename, select_column):
        query_select = "SELECT {1} from {0} ". format(tablename,select_column)
        cur = self.con.cursor()
        cur.execute(query_select)
        row =cur.fetchall()
        for i in row:
            print(i)

        print("table is selected")

    def update_table(self , tablename ,set_condition,filter_condition):
        query_update = "UPDATE {0}  SET {1} WHERE {2}".format(tablename,set_condition,filter_condition)
        cur = self.con.cursor()
        cur.execute(query_update)
        self.con.commit()
        print("data update")

    def delete_table(self , tablename,delete_condition):
        query_delete = "DELETE FROM {0} WHERE {1}".format(tablename,delete_condition)
        cur = self.con.cursor()
        cur.execute(query_delete)
        self.con.commit()
        print("table is deleted")



c = Connections('localhost','oops_db','root','sumasoft123')
tablename = 'Employee_new1'
#schema = 'ID int ,Name varchar(30)'
#value = "2, 'shivam'"
#select_column = 'ID, Name'
#set_condition = 'ID =4'
#filter_condition = 'ID =1'
#delete_condition = 'ID =2'
c.create_table(tablename,schema)
c.insert_into_table(tablename,schema,value)
#c.select(tablename,select_column)
#c.update_table(tablename,set_condition,filter_condition)
#c.delete_table(tablename,delete_condition)
#c.select(tablename,select_column)

