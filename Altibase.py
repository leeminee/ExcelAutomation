import jaydebeapi, jpype, pyodbc
from openpyxl import Workbook

classname = 'Altibase6_5.jdbc.driver.AltibaseDriver'
classfile = 'C:/Users/user/IdeaProjects/lib/Altibase6_5.jar'

dbuser = 'ipageon'
passwd = 'ipageon'

conn, cursor = None, None


def altibase_conn():
    try:
        conn = jaydebeapi.connect(classname, "jdbc:Altibase://10.200.2.130:20300/mydb", [dbuser, passwd], classfile)

        cursor = conn.cursor()
        print(">> Altibase connection")

        select_all(cursor)

        cursor.close()
        conn.close()
    except Exception as msg:
        print('Error Message : %s' % msg)


def select_all(cursor):
    sql = "SELECT * FROM STAT_RES_MEMORY_DAY ORDER BY STIME DESC LIMIT 1"
    cursor.execute(sql)

    data = cursor.fetchall()

    for x in data:
        print(x)
        data_parsing(x)

def data_parsing(data):
    host = data[6]
    usage = data[8]
    total = data[10]
    print("Host : " +host)
    print("Usage : " +str(usage))
    print("Total : " +str(total))



altibase_conn()
# dg4odbc
