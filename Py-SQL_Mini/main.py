from insert import insertData
from update import updateData
from delete import deleteData
from read import readData

obj = insertData()
obj1 = updateData()
obj2 = deleteData()
obj3 = readData()

print('------------Student Management System--------------')

print('FOR INSERTION PRESS "1" \nFOR UPDATION PRESS "2" \nFOR DELETION PRESS "3" \nFOR READ PRESS "4"\n')

num = int(input('Enter your choice: \n'))

if num==1:
    print('Choose 1 for Student \nChoose 2 for Course \nChoose 3 for Transaction\n')
    n=int(input('Enter your choice: '))
    if n==1:
        sid = int(input('Enter Student ID: '))
        sname = input('Enter Student Name: ')
        email = input('Enter Student Email: ')
        city = input('Enter Student City: ')
        obj.insertStudent(sid,sname,email,city)
    if n==2:
        cid = int(input('Enter Course ID: '))
        sid = int(input('Enter Student ID: '))
        cname = input('Enter Course Name: ')
        price = float(input('Enter Course Price: '))
        obj.insertCourse(cid,sid,cname,price)
    if n==3:
        tid = int(input('Enter Transaction ID: '))
        cid = int(input('Enter Course ID: '))
        sid = int(input('Enter Student ID: '))
        method = input('Enter Payment Method: ')
        obj.insertTrans(tid,cid,sid,method)

if num==2:
    print('Choose 1 for Student \nChoose 2 for Course \nChoose 3 for Transaction\n')
    n=int(input('Enter your choice: '))
    if n==1:
        print('Enter column you are going to update.\nFor Name Press 1.\nFor Email Press 2. \nFor City Press 3.\n')
        u = int(input('Enter the column: '))
        stid=int(input('Enter Student ID: '))
        newval=input('Enter the New value: ')
        obj1.updateStudent(u,stid,newval)
    if n==2:
        print('Enter column you are going to update.\nFor Course Name  1.\nFor Price Press 2.\n')
        u = int(input('Enter the column: '))
        co_id = int(input('Enter Course ID: '))
        if u==2:
            newval=float(input('Enter the New value: '))
            obj1.updateCourse(u,co_id,newval)
        else:
            newval=input('Enter the New value: ')
            obj1.updateCourse(u,co_id,newval)
    if n==3:
        print('Enter Transaction ID and method\n')
        t_id = int(input('Enter Transaction ID: '))
        newval=float(input('Enter the New value: '))
        obj1.updateTrans(u,t_id,newval)

if num==3:
    print('Choose 1 for Student \nChoose 2 for Course \nChoose 3 for Transaction\n')
    n=int(input('Enter your choice(Table) to delete the record: '))
    if n==1:
        stid=int(input('Enter Student ID of student you are going to delete: '))
        obj2.deleteStudent(stid)
    if n==2:
        co_id=int(input('Enter Course ID of course you are going to delete: '))
        obj2.deleteCourse(co_id)
    if n==3:
        t_id=int(input('Enter Student ID of transaction record you are going to delete: '))
        obj2.deleteCourse(t_id)

if num==4:
    print('Choose 1 for Student \nChoose 2 for Course \nChoose 3 for Transaction\n')
    n=int(input('Enter your choice to read the required table: '))
    if n==1:
        obj3.readStudent()
    if n==2:
        obj3.readCourse()
    if n==3:
        obj3.readTrans()