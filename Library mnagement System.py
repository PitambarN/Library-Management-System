import psycopg2


#create connection
con = None
conn= psycopg2.connect(database= "library",user= "postgres",password= "1122",host= "localhost",port= "5432")
print("connected to database")



def addbook():
    bn=input("Enter book Name:\n")
    c = input("Enter book Code:\n")
    t = input("Enter Total Book:\n")
    s = input("Enter Subject:\n")
    query="insert into books values(%s,%s,%s,%s)"
    data=(bn,c,t,s)
    #create cursor
    curs=conn.cursor()
    curs.execute(query,data)
    conn.commit()
    print(">-------------------------------------<")
    print("Data Entered successfully")
    main()

#code of issue book
def issueb():

    n=input("Enter your Name:\n")
    r=input("Enter Reg no:\n")
    co=input("Enter book code:\n")
    da=input("Enter Issue Date:\n")
    data=(n,r,co,da)
    query="insert into issue values(%s,%s,%s,%s)"
    #create cursor
    cur=conn.cursor()
    cur.execute(query,data)
    conn.commit()
    print(">------------------------------------------<")
    print("Book issued To the name of:",n)
    bookup(co,-1)

#code for submitBook
def submitb():
    n = input("Enter your Name:\n")
    r = input("Enter Reg no:\n")
    co = input("Enter book code:\n")
    d = input("Enter Issue Date:\n")
    data=(n,r,co,d)
    query="insert into submit values(%s,%s,%s,%s)"
    #create cursor
    cur=conn.cursor()
    cur.execute(query,data)
    conn.commit()
    print(">-------------------------------------------<")
    print("Book submitted from :",n)
    bookup(co,+1)

#code for update book
def bookup(co,u):
    co=input("Enter book code:\n")
    query="select total from books where bcode = %s"
    data=(co,)
    #create cursor
    cur=conn.cursor()
    cur.execute(query,data)
    myresult=cur.fetchone()
    q=myresult[0]+u
    query1="update books set total=%s where bcode=%s"
    d=(q,co)
    cur=conn.cursor()
    cur.execute(query1,d)
    conn.commit()


#code for delete book
def delbook():
    ac=input("Enter book code:\n")
    query="delete from books where bcode=%s"
    data=(ac,)
    cur=conn.cursor()
    cur.execute(query,data)
    conn.commit()
    main()

#code for display book
def disbook():
    query="select * from books"
    cur=conn.cursor()
    cur.execute(query)
    result=cur.fetchall()
    print(result)
    for i in result:
        print("Book Name:",i[0])
        print("Book Code:",i[1])
        print("Total:",i[2])
        print(">-------------------------<")










def main():
    print("""
    ----------------------------------LIBRARY MANAGER--------------------------------
    1.ADD BOOK
    2.ISSUE BOOK
    3.SUBMIT BOOK
    4.DELETE BOOK
    5.DISPLAY BOOK
    6.UPDATE BOOK
    """)
    choice=int(input("Enter your Choice(1-5):\n"))
    if choice==1:
        addbook()
    elif choice==2:
        issueb()
    elif choice==3:
        submitb()
    elif choice==4:
        delbook()
    elif choice==5:
        disbook()
    elif choice==6:
         bookup()


    else:
        print("Invalid Choice")
main()





