import jaydebeapi, jpype, pyodbc
from openpyxl import Workbook

classname = 'Altibase.jdbc.driver.AltibaseDriver'
classfile = 'C:/Users/user/IdeaProjects/lib/Altibase6_5.jar'
dbuser = 'ipageon'
passwd = 'ipageon'

conn, cursor = None, None


def select_all():
    try:
        # cnxn = pyodbc.connect('DRIVER={Altibase.jdbc.driver.AltibaseDriver}; SERVER=localhost; DATABASE=mbdb; UID=ipageon; PWD=ipageon')
        # cursor = cnxn.cursor()
        # cnxn = pyodbc.connect('DSN=mydb; PWD=ipageon')
        conn = jaydebeapi.connect(classname, ['jdbc:Altibase://10.200.2.130:20300/mydb', '%s' % dbuser, '%s' % passwd],classfile)
        cursor = conn.cursor()
        print("conn : " + conn)
        print(">> Altibase connection")

        sql = "SELECT * FROM STAT_MCPPTT_SUBS ORDER BY STIME DESC LIMIT 1"
        cursor.execute(sql)

        data = cursor.fetchall()

        for x in data:
            print(x[0])
            print(x[1])
            print(x[2])

        cursor.close()
        conn.close()
    except Exception as msg:
        print('Error Message : %s' %msg)

    # cursor = conn.cursor()
    #
    # cursor.execute("select * from alarm_test")
    #
    # row = cursor.fetchone()
    #
    # while row:
    #     print("uuid : "+row[0] + ", host : "+row[1]+", msg1 : "+row[2]+", msg2 : "+row[3])
    #     row = cursor.fetchone()
    # print()
    # conn.close()


select_all()
# dg4odbc
