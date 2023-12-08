import MySQLdb
conn = MySQLdb.connect('localhost', 'root','root','b44')
curs = conn.cursor()

while True:
    ch = int(input("\n\nEnter Choice:\n1.Add Student\t\t2.Show All Students\n3.Update A Student\t4.Delete a Stuent\n5.Exit"))
    match ch:
        case 1:
            print("Add Student")
            r = int(input("Enter roll_no:"))
            n = input("Enter Name:")
            m = float(input("Enter Marks:"))
            curs.execute(f"insert into student values({r},'{n}',{m})")
            conn.commit()
            print("Student Added")
        case 2:
            print("Show All Students")
            curs.execute("select * from student")
            print("roll_no\tName\tMarks")
            for row in curs:
                print(row[0],'\t',row[1],3'\t',row[2])
        case 3:
            print("Update a Student")
            r = int(input("Enter roll_no to update:"))
            m = float(input("Enter updated Marks:"))
            curs.execute(f"update student set marks={m} where roll_no={r}")
            conn.commit()
            print("student updated")
        case 4:
            print("Delete a Student")
            r = int(input("Enter roll_no to Delete:"))
            curs.execute(f"delete from student where roll_no={r}")
            conn.commit()
            print("student deleted")
        case 5:
            print("Exiting...")
            break
        case _:
            print("Invalid Choice..")

conn.close()

