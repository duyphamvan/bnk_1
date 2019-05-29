import psycopg2

class Lop:
    def __init__(self):
        self.conn = psycopg2.connect(
            host="localhost",
            database="my_first_postgres_databases",
            user="postgres",
            password="123456"
        )
    def insertClass(self):
        cur = self.conn.cursor()
        sql = "insert into lop (malop, tenlop) values (%s, %s)"
        val = ('5', 'B15')
        cur.execute(sql, val)
        self.conn.commit()
        print(cur.rowcount, "record inserted.")

    def deleteClass(self):
        cur = self.conn.cursor()
        sql = "delete from lop where malop = %s"
        sql1 = "delete from sinhvien where lop_id = %s"
        malop = lop_id =('1')
        cur.execute(sql1, lop_id)
        cur.execute(sql, malop)
        self.conn.commit()
        print(cur.rowcount, "record(s) deleted")
    def updateClass(self):
        cur = self.conn.cursor()
        sql = "update lop set tenlop = %s where malop = %s"
        val = ('B20', '3')
        cur.execute(sql, val)
        self.conn.commit()
        print(cur.rowcount, "record(s) affected")

classnew = Lop()
print(classnew.insertClass())
print(classnew.deleteClass())
print(classnew.updateClass())