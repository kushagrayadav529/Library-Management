#Owner:KUSHAGRA YADAV

import mysql.connector as a

con = a.connect(host="localhost", user="root", passwd="232004", database="library1")

def addbook():
    try:
        bn = input("Enter Book Name:")
        c = input("Enter Book Code:")
        t = input("Total Books:")
        s = input("Enter Category:")
        data = (bn, c, t, s)
        sql = "insert into books values(%s, %s, %s, %s)"
        c = con.cursor()
        c.execute(sql, data)
        con.commit()
        print("*" * 100)
        print("Book added successfully")
        main()
    except:
        main()

def issueb():
    try:
        n = input("Enter Your Name:")
        r = input("Enter Your RegNo:")
        co = input("Enter Book Code:")
        d = input("Enter Date:")
        a = "insert into issue values(%s, %s, %s, %s)"
        data = (n, r, co, d)
        c = con.cursor()
        c.execute(a, data)
        print("*" * 100)
        print("Book issued to:", n)
        print("Kindly return the book in 15 days")
        bookup(co, -1)
        main()
    except:
        main()

def submitb():
    try:
        n = input("Enter Name:")
        r = input("Enter RegNo:")
        co = input("Enter Book Code:")
        d = input("Enter Date:")
        a = "insert into submit values(%s, %s, %s, %s)"
        data = (n, r, co, d)
        c = con.cursor()
        c.execute(a, data)
        print("*" * 100)
        print("Book submitted by:", n)
        print("Keep Learning")
        bookup(co, 1)
        main()
    except:
        main()

def bookup(co, u):
    a = "select TOTAL from books where bcode = %s"
    data = (co,)
    c = con.cursor()
    c.execute(a, data)
    myresult = c.fetchone()
    t = myresult[0] + u
    sql = "update books set total = %s where bcode = %s"
    d = (t, co)
    c.execute(sql, d)
    con.commit()
    main()

def dbook():
    try:
        ac = input("Enter Book Code:")
        a = "delete from books where bcode = %s"
        data = (ac,)
        c = con.cursor()
        c.execute(a, data)
        con.commit()
        main()
        print("Book removed from Library")
    except:
        main()

def dispbook():
    try:
        a = "select * from books"
        c = con.cursor()
        c.execute(a)
        myresult = c.fetchall()
        for i in myresult:
            print("Book Name:", i[0])
            print("Book Code:", i[1])
            print("Total:", i[2])
            print("Category:", i[3])
            print("*" * 100)
        main()
    except:
        main()

def displayissue():
    a = "select * from issue"
    c = con.cursor()
    c.execute(a)
    dsp = c.fetchall()
    for i in dsp:
        print("Name:", i[0])
        print("RegNo:", i[1])
        print("Book code:", i[2])
        print("Date of issue:", i[3])
        print("*" * 50)
    print("*" * 100)
    menu()

def main():
    print('''
           * * * * * * * * * * * * * * * * * * * * * *
           *           WELCOME TO SCHOOL LIBRARY      *
           * 1.ADD BOOK                               *
           * 2.ISSUE BOOK                             *
           * 3.RETURN BOOK                            *
           * 4.REMOVE BOOK                            *
           * 5.DISPLAY ALL BOOKS                      *
           * 6.DISPLAY MEMBERS WHO HAVE ISSUED BOOKS  *
           * 7.EXIT                                   *
           * * * * * * * * * * * * * * * * * * * * * *
           ''')
    ch = int(input("Enter your choice: "))
    try:
        if ch == 1:
            addbook()
        elif ch == 2:
            issueb()
        elif ch == 3:
            submitb()
        elif ch == 4:
            dbook()
        elif ch == 5:
            dispbook()
        elif ch == 6:
            displayissue()
        elif ch == 7:
            print("Thank you")
        else:
            print("Wrong choice, please choose a number between 1-7")
        main()
    except:
        main()

def pswd():
    pswd = input("Enter password: ")
    if pswd == "123123":
        main()
    else:
        print("Wrong password")
        pswd()

pswd()
