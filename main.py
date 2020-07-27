import contact_app as C
import sqlite3

db=sqlite3.connect('Contact.db')

choice=C.display_Menu()
cur = db.cursor()
cur.execute('create table if not exists'\
            +'  contacts(First_Name text, Last_Name text, Mobile_No text)')

while choice!=5:
    if choice == 1:
        print("Enter Contact details: ")
        f_name=input("Enter First Name: ")
        l_name=input("Enter last Name: ")
        mob=input("Enter Mobile Number: ")
        C.Add_Contact(db,f_name,l_name,mob)

    elif choice == 2:
        C.View_Contact(db)

    elif choice == 3:
        f_name=input(" Enter First Name of the Record to be Updated: ")
        mob=input(" Enter Updated Phone Number: ")
        C.Update_Contact(db,f_name,mob)

    elif choice == 4:
        f_name=input(" Enter First Name of the record to be deleted: ")
        C.Delete_Contact(db,f_name)

    else:
        print("Invalid Menu Option....Please Try Again")
    choice=C.display_Menu()
db.close()