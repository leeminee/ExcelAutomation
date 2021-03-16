import jaydebeapi, jpype, pyodbc
from openpyxl import Workbook

classname = 'Altibase6_5.jdbc.driver.AltibaseDriver'
classfile = 'C:/Users/user/IdeaProjects/lib/Altibase6_5.jar'

dbuser = 'ipageon'
passwd = 'ipageon'

conn, cursor = None, None


def select_all():
    try:
        conn = jaydebeapi.connect(classname, "jdbc:Altibase://10.200.2.130:20300/mydb", [dbuser, passwd], classfile)

        cursor = conn.cursor()
        print(">> Altibase connection")

        sql = "SELECT * FROM STAT_RES_CPU_DAY ORDER BY STIME DESC LIMIT 1"
        cursor.execute(sql)

        data = cursor.fetchall()

        for x in data:
            print(x)

        cursor.close()
        conn.close()
    except Exception as msg:
        print('Error Message : %s' %msg)


select_all()
# dg4odbc
