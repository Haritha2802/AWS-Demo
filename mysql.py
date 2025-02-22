import pymysql

db_host = "database-2.cvgywy4emggl.us-east-1.rds.amazonaws.com" 
db_name = "test_mysql"
db_user = "admin"
db_pass = "progknowledge"

connection = pymysql.connect(host = db_host, database = db_name, user = db_user, password = db_pass)
print("connected to the database")

cursor = connection.cursor()
cursor.execute('SELECT version()')
db_version = cursor.fetchone()
print(db_version)

cursor.close()