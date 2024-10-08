import mysql.connector


class MysqlDatabase:
    def __init__(self , host,user,password,database,connection):
        self.host ="localhost"
        self.user ="root"
        self.password = "sumasoft123"
        self.database = "mydb"
        connection =connection


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


    def create_table(self, table_name, columns):
        try:
            cursor = self.connection.cursor()
            query = f"create table if not exists {table_name} ({columns})"
            cursor.excute(query)
            print(f"table created sucessfully")
        except mysql.connector.Error as err:
            print(f"Error: {err}")
        finally:
             cursor.close()
    def insert_data(self,table_name,colums,values):
        try:
            cursor = self.connection.cursor()
            query = f"insert into {table_name} ({colums}) values ({values})"
            cursor.excute(query)
            self.connection.commit()
            print("record insert successfully")

        except mysql.connector.Error as err:
            print(f"error: {err}")
        finally:
            cursor.close()

    def select_data(self , table_name, colums ="*",where_clause = ""):
        try:
            cursor = self.connection.cursor()
            query = f"select {colums} from {table_name} values ({where_clause})"
            cursor.execute(query)
            rows = cursor.fetchall()
            for row in rows:
                print(row)



        except mysql.connector.Error as err:
            print(f"error: {err}")
        finally:
            cursor.close()

    def update_data(self , table_name, set_clause, where_clause):
        try:
            cursor = self.connection.cursor()
            query = f"update {table_name} set {set_clause} where {where_clause}"
            cursor.execute(query)
            self.connection.commit()
            print("record update sucessfuly")


        except mysql.connector.Error as err:
            print(f"error: {err}")
        finally:
            cursor.close()

    def delete(self, table_name, where_clause):
        try:
            cursor = self.connection.cursor()
            query = f"delete from  {table_name}  where {where_clause}"
            cursor.excute(query)
            self.connection.commit()
            print("record deleted sucessfully ")


        except mysql.connector.Error as err:
            print(f"error: {err}")
        finally:
            cursor.close()

    def clone(self):
        if self.connection.is_connected():
            self.connection.close()
            print("Database closed")

dbms = MysqlDatabase(
    host = "localhost",
    user = "root",
    password="sumasoft123",
    database = "mydb",
    connection = "MysqlDatabase"
)
dbms.connect()


dbms.create_table(
    "employee_table",
    """
    id int auto increment primary key
    name varchar(255)
    position varchar(255)
    salary decimal(10,2)
    """
)

#insert

dbms.insert_data(
 "employee_table",
 "name, position,salary",
 "'john', 'software devloper',5600"

)

dbms.select_data("employee_table")

#update
dbms.update_data(
    "employee_table",
    "salary = 8000",
    "name = 'john'"

)
dbms.delete_data("employee_table","name= 'john ")

dbms.clone()