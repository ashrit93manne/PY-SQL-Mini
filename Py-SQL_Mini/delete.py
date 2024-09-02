import sqlite3
class deleteData():
    def __init__(self):
        self.conn = sqlite3.connect('sms.db')
        self.curr = self.conn.cursor()

    def deleteStudent(self,sid):
        self.curr.execute(f'''
                            DELETE FROM STUDENT WHERE SID = {sid} 
                        ''')
        self.conn.commit()
        print('Record Deleted Successfully')
    
    def deleteCourse(self,cid):
        self.curr.execute(f'''
                            DELETE FROM COURSE WHERE CID = {cid} 
                        ''')
        self.conn.commit()
        print('Record Deleted Successfully')

    def deleteTrans(self,tid):
        self.curr.execute(f'''
                            DELETE FROM TRANS WHERE TID = {tid} 
                        ''')
        self.conn.commit()
        print('Record Deleted Successfully')