import pymysql
pymysql.install_as_MySQLdb()

db = pymysql.connect("localhost", "root", "1234", "blogdata")

cursor = db.cursor()

cursor.execute("SELECT VERSION()")

data = cursor.fetchone()

print("Database version : {}".format(data))

db.close()