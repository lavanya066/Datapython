import mysql.connector
from mysql.connector import Error
def insertVals():
    name=input("enter name")
    roll=input("enter roll no")
    classy=input("enter the class")
    val=(name,roll,classy)
    q="INSERT INTO stu_data VALUES (%s,%s,%s)"
    cursor.execute(q,val)
    print('inserted')
def showAll():
    q="SELECT * FROM stu_data"
    cursor.execute(q)
    records = cursor.fetchall()
    print('name\troll no\tclass')
    for rec in records:
        print(rec[0],"\t",rec[1],"\t",rec[2])
        
def appendVals():
    roll=input("enter the roll no to be appended")
    name=input("enter name")
    classy=input("enter the class")
    q="UPDATE stu_data SET name= %s, class=%s WHERE roll=%s"
    val=(name,classy,roll)
    cursor.execute(q,val)
    print('Updated')
try:
    a=0
    connection = mysql.connector.connect(host='localhost',database='students',user='root',password='')
    
    if connection.is_connected():
        cursor = connection.cursor()
        c='y'
        while(c=='y'):
            print("1.insert \n 2.show \n 3.append")
            a=int(input("enter the number of your choice"))
            if(a==1):
                insertVals()
            
            elif(a==2):
                showAll()
            
            elif(a==3):
                appendVals()
                
            else:
                print("Invalid choice")
            connection.commit()
            c=input('Do you want to continue(y/n)')
except Error as e:
    print("Error while connecting to MySQL", e)
finally:
    if (connection.is_connected()):
        cursor.close()
        connection.close()
        print("MySQL connection is closed")
