import sqlite3
class insertData:
    def __init__(self):
        self.conn = sqlite3.connect('sms.db')
        self.curr = self.conn.cursor()
    
    def insertStudent(self,sid,sname,email,city):
        self.curr.execute(f'''
                    INSERT INTO STUDENT VALUES(
                         {sid},
                        '{sname}',
                        '{email}',
                        '{city}'
                        )
                    ''')
        self.conn.commit()
        print('Data Added Successfully')
    
    def insertCourse(self,cid,sid,cname,price):
        self.curr.execute(f'''
                    INSERT INTO COURSE VALUES(
                         {cid},
                         {sid},
                        '{cname}',
                         {price}
                        )
                    ''')
        self.conn.commit()
        print('Data Added Successfully')

    def insertTrans(self,tid,cid,sid,method):
        self.curr.execute(f'''
                        INSERT INTO TRANS VALUES(
                        {tid},
                        {cid},
                        {sid},
                        '{method}'
                        )
                    ''')
        self.conn.commit()
        print('Data Added Successfully')
