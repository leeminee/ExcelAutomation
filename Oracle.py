import cx_Oracle
from openpyxl import Workbook

class Test:
    def __init__(self, uuid, host, msg1, msg2):
        self.uuid = uuid
        self.host = host
        self.msg1 = msg1
        self.msg2 = msg2

def select_all():
    conn = cx_Oracle.connect('system','manager','orcl')
    print(">> Oracle DB connect ")
    try:
        with conn.cursor() as curs:
            sql = "select * from alarm_test"
            print("sql : "+sql)
            curs.execute(sql)
            rs = curs.fetchall()

            wb = Workbook()
            ws = wb.active

            # 첫 행 입력
            ws.append(('UUID','HOST','Massage1','Massage2'))

            for row in rs:
                print(row)
                ws.append(row)
            wb.save('C:/test/Alarm현황.xlsx')
    finally:
        conn.close()

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