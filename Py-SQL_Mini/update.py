import sqlite3
class updateData:
    def __init__(self):
        self.conn = sqlite3.connect('sms.db')
        self.curr = self.conn.cursor()
    
    def updateStudent(self,col,sid,newval):
        columns=['SID','SNAME','EMAIL','CITY']
        column =columns[col]
        #print(column)
        self.curr.execute(f'''
                            UPDATE STUDENT
                            SET '{column}' = '{newval}'
                            WHERE SID = {sid}
                        ''')
        self.conn.commit()
        print('Data Successfully Updated')
    
    def updateCourse(self,col,cid,newval):
        columns=['CID','SID','COURSENAME','PRICE']
        column =columns[col+1]
        #print(column)
        #print(newval)    
        self.curr.execute(f'''
                            UPDATE COURSE
                            SET '{column}' = '{newval}'
                            WHERE CID = {cid}
                        ''')
        self.conn.commit()
        print('Data Successfully Updated')
    
    def updateTrans(self,tid,newval):
        self.curr.execute(f'''
                            UPDATE COURSE
                            SET METHOD = '{newval}'
                            WHERE TID = {tid}
                        ''')
        self.conn.commit()
        print('Data Successfully Updated')