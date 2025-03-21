import mysql.connector
import os
# Thiết lập kết nối
conn = mysql.connector.connect(
    host="localhost",      # Địa chỉ MySQL Server
    user="root",           # Tên người dùng MySQL
    password=os.getenv("mysqlpwroot"),  # Mật khẩu MySQL
    database="sql_injection_demo"   # Tên database
)