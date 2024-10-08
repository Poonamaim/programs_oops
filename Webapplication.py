'''from OOPS_DB1 import Connections



c = Connections()
tablename = 'Employee_news'
schema = 'ID int , Name varchar(30)'
values = "1, 'shivam'"
#select_column = 'ID, Name'
#set_condition = 'ID =4'
#filter_condition = 'ID =1'
#delete_condition = 'ID =2'
c.create_table(tablename,schema)
c.insert_into_table(tablename,schema,values)
#c.select(tablename,select_column)
#c.update_table(tablename,set_condition,filter_condition)
#c.delete_table(tablename,delete_condition)
#c.select(tablename,select_column)
'''
from flask import Flask
app = Flask(__name__)
@app.route("/")
def home():
    return "Hello, ukgjugFlask!"