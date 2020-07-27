import sqlite3

def display_Menu():
    print("-----------> Welcome to the Contacts App <---------------")
    print(" MENU:- ")
    print(" 1. Add a Contact")
    print(" 2. View a Contact")
    print(" 3. Update a Contact")
    print(" 4. Delete a Contact")
    print(" 5. EXIT")
    choice=int(input(" Enter Your Choice Number: "))
    return choice


def Add_Contact(db,f_name,l_name,mob):
    cur = db.cursor()
    cur.execute('select * from contacts where First_Name=? or Mobile_No=?', (f_name, mob))
    cont = cur.fetchall()
    if not cont:
        cur.execute('insert into contacts values(?,?,?)', (f_name, l_name, mob))
        print("-----* Record Successfully Added *-----")
        db.commit()
    else:
        print("---------* Record Already Exists *----------")



def Update_Contact(db,f_name,mob):
    ct = (mob, f_name)
    cur = db.cursor()
    cur.execute('select * from contacts where First_Name=?', (f_name,))
    cont = cur.fetchall()
    if cont:
        cnt = cur.execute('update contacts set Mobile_No=? where First_Name=?', ct)
        db.commit()
        print("-----* Record Successfully Updated *-----")
    else:
        print("----------* Failed to Update Data as Record Does Not Exist *----------")


def Delete_Contact(db,f_name):
    ct = (f_name,)
    cur = db.cursor()
    cur.execute('select * from contacts where First_Name=?', (f_name,))
    cont = cur.fetchall()
    if cont:
        cur.execute('delete from contacts where First_Name=?', ct)
        db.commit()
        print("-----* Record Successfully Deleted *-----")
    else:
        print("-------------* Failed To Delete Data as Record Does Not Exist *----------------")


def View_Contact(db):
    print("Contact List is: ")
    cur=db.cursor()
    cur.execute('select * from contacts')
    while True:
        cont = cur.fetchone()
        if cont:
            f_name, l_name, mob = cont
            print(f_name, " ", l_name, " : ", mob)
        else:
           break



