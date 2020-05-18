import mysql.connector
from sshtunnel import SSHTunnelForwarder

server = SSHTunnelForwarder(
    'XXX.XXX.XXX.XXX',
    ssh_username='root',
    ssh_password='my_server_password',
    remote_bind_address=('127.0.0.1', 3306)
)
server.start()
cnx = mysql.connector.connect(user='scott', password='password',
                              host='127.0.0.1',
                              database='employees')
cnx.close()
server.close()