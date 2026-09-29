import mysql.connector
class blood_donor:

    def  __init__(self):
        self.con=mysql.connector.connect(
            user='root',
            password='john',
            host='localhost',
            database='blooddb'
        )
        self.cursor=self.con.cursor()

    def list(self):
        query='SELECT * FROM donor'
        self.cursor.execute(query)
        data=self.cursor.fetchall()
        if data:
            for record in data:
                print(record)
        else:
            print('No records found')
    def create(self,id,name,bloodgroup,phone,city,last_donation):
        query=''' INSERT INTO donor(name,bloodgroup,phone,city,last_donation)
                values(%s,%s,%s,%s,%s,%s)'''
        data=(id,name,bloodgroup,phone,city,last_donation)
        self.cursor.execute(query,data)
        self.con.commit()
        print("Inserted data successfully")
