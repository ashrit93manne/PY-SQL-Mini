import sqlite3
class readData:
    def __init__(self):
        self.conn = sqlite3.connect('sms.db')
        self.curr = self.conn.cursor()
    
    def readStudent(self):
        self.curr.execute("SELECT * FROM STUDENT")
        students = self.curr.fetchall()
        if students:
            print("\nStudent Records:")
            print ("{:>10} {:>20} {:>20} {:>10}".format('Student ID','Name','Email','City'))
            for row in students:
                print ("{:>10} {:>20} {:>20} {:>10}".format(row[0], row[1], row[2], row[3]))
        else:
            print("No student records found!")


    def readCourse(self):
        self.curr.execute("SELECT * FROM COURSE")
        courses = self.curr.fetchall()
        if courses:
            print("\nCourse Records:")
            print ("{:>10} {:>20} {:>20} {:>10}".format('Course ID','Student ID','Course Name','Price'))
            for row in courses:
                print ("{:>10} {:>20} {:>20} {:>10}".format(row[0], row[1], row[2], row[3]))
        else:
            print("No Course records found!")

    def readTrans(self):
        self.curr.execute("SELECT * FROM TRANS")
        trans = self.curr.fetchall()
        if trans:
            print("\nTransaction Records:")
            print ("{:>20} {:>20} {:>18} {:>25}".format('Transaction ID','Course ID','Student ID','Method of Transaction'))
            for row in trans:
                print ("{:>20} {:>20} {:>18} {:>25}".format(row[0], row[1], row[2], row[3]))
        else:
            print("No Transaction records found!")