import psycopg2

#connect to the db

class SinhVien:
    def __init__(self):
        self.conn = psycopg2.connect(
            host="localhost",
            database="my_first_postgres_databases",
            user="postgres",
            password="123456"
        )

    def insertStudent(self):
        cur = self.conn.cursor()
        sql = "insert into sinhvien (masv, hoten, gioitinh, ngaysinh, lop_id) values(%s , %s, %s, %s, %s)"
        val = (input('Enter the masv: '),  input('Enter the name: '), input('Enter the male: '), input('Enter the date of birthday: '), input('Enter the Class-id: '))
        cur.execute(sql, val)
        self.conn.commit()
        print(cur.rowcount, "record inserted.")

    def deleteStudentById(self):

        cur = self.conn.cursor()
        sql = "delete from sinhvien where masv = %s "
        val = input()
        cur.execute(sql, val)
        self.conn.commit()
        print(cur.rowcount, "record(s) deleted")
    # deleteStudentById()
    def updateStudentById(self):

        cur = self.conn.cursor()
        sql = "update sinhvien set hoten = (%s) where masv = (%s) "
        val = (input('Enter the name: '), input('Enter the id: '))
        cur.execute(sql, val)
        self.conn.commit()
        print(cur.rowcount, "record(s) affected")
    # updateStudentById()
    def searchByName(self):
        cur = self.conn.cursor()
        sql = "select * from sinhvien where hoten = (%s) "
        val = input('Enter the name: ')
        cur.execute(sql,(val,))
        result = cur.fetchall()
        for x in result:
            print(x)

    def searchByClass(self):
        cur = self.conn.cursor()
        sql = "select sinhvien.hoten, lop.tenlop from sinhvien inner join lop on sinhvien.lop_id = lop.malop "
        cur.execute(sql)
        result = cur.fetchall()
        for x in result:
            print(x)

    def createNewStudent(self):
        file_name = input('Enter the file name: ')
        file = open(file_name, 'r')
        content = file.read()
        names_list = [y for y in (x.strip() for x in content.splitlines()) if y]
        arr = []
        for i in names_list:
            i = i.split(',')
            i = tuple(i)
            arr.append(i)
        print(arr)
        cur = self.conn.cursor()
        sql = "INSERT INTO sinhvien (masv, hoten, gioitinh, ngaysinh, lop_id) VALUES (%s, %s, %s, %s, %s)"
        cur.executemany(sql, arr)
        self.conn.commit()
        print(cur.rowcount, "student inserted.")
    def importSpecificStudent(self):
        file_name = input('Enter the file name: ')
        file = open(file_name, 'r')
        content = file.read()
        names_list = [y for y in (x.strip() for x in content.splitlines()) if y]
        arr = []
        specific_studen = input('Enter the number: ')
        for i in names_list:
            i = i.split(',')
            i = tuple(i)
            if i[0] == specific_studen:
                arr.append(i)
        cur = self.conn.cursor()
        sql = "INSERT INTO sinhvien (masv, hoten, gioitinh, ngaysinh, lop_id) VALUES (%s, %s, %s, %s, %s)"
        cur.executemany(sql, arr)
        self.conn.commit()
        file.close()
        print(cur.rowcount, "student inserted.")


student = SinhVien()
# print(student.insertStudent())
# print(student.deleteStudentById())
#print(student.updateStudentById())
# print(student.searchByClass())
# print(student.searchByName())
# student.createNewStudent()
student.importSpecificStudent()



