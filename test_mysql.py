import pymysql

info = {
    "host": "127.0.0.1",
    "port": 3306,
    "db": "my_sales",
    "user": "root",
    "passwd": "admin"
}

conn = pymysql.Connect(**info)
print(conn)
conn.close()
