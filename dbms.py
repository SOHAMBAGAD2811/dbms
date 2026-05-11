import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="soham",
    password="2811",
    database="school_db",
    ssl_disabled=True,
)
cursor = conn.cursor()

cursor.execute("create table if not exists employee (empid INT, name VARCHAR(50), salary INT)")

while True:
    print("\n1.Add  \n2.Update  \n3.Delete  \n4.Show All  \n5.Salary>50k  \n6.Search  \n7.Exit")
    choice = input("Choice: ")

    if choice == '1':
        e_id = input("ID: ")
        name = input("Name: ")
        sal = input("Salary: ")
        cursor.execute("insert into employee values (%s, %s, %s)", (e_id, name, sal))
        conn.commit()
        print("Employee added.")

    elif choice == '2':
        e_id = input("ID to update: ")
        sal = input("New Salary: ")
        cursor.execute("update employee set salary=%s where empid=%s", (sal, e_id))
        conn.commit()
        print("Salary updated.")

    elif choice == '3':
        e_id = input("ID to delete: ")
        cursor.execute("delete from employee where empid=%s", (e_id,))
        conn.commit()
        print("Employee deleted.")

    elif choice == '4':
        cursor.execute("select * from employee")
        rows = cursor.fetchall()
        if rows:
            for row in rows:
                print(row)
        else:
            print("No records found.")

    elif choice == '5':
        cursor.execute("select * from employee where salary > 50000")
        rows = cursor.fetchall()
        if rows:
            for row in rows:
                print(row)
        else:
            print("No employees with salary > 50k.")

    elif choice == '6':
        e_id = input("ID to search: ")
        cursor.execute("SELECT * FROM employee WHERE empid=%s", (e_id,))
        row = cursor.fetchone()
        print(row if row else "Employee not found.")

    elif choice == '7':
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Try again.")

cursor.close()
conn.close()
