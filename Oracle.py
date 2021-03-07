import cx_Oracle

class Test:
    def __init__(self, uuid, host, msg1, msg2):
        self.uuid = uuid
        self.host = host
        self.msg1 = msg1
        self.msg2 = msg2

def select_all():
    conn = cx_Oracle.connect('system', 'manager', '127.0.0.1/orcl')
    print(">>connect ")
    try:
        with conn.cursor() as curs:
            sql = "select * from alarm_test"
            curs.execute(sql)
            rs = curs.fetchall()
            for row in rs:
                print(row)
    finally:
        conn.close()

select_all()
# dg4odbc