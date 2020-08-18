
from sqlite3 import *
class saveData:
    def createDatabse(self,customer_name,customer_bill):
        con=connect("Superstore1")
        cur=con.cursor()
        # sql="""CREATE TABLE utility1 ("customer_name" text,"customer_contact" integer)"""
        sql="INSERT INTO utility1 VALUES('"+str(customer_name) + "'," + str(customer_bill)+")"
        cur.execute(sql)
        con.commit()
        con.close()

####################FOR SEARCHING#######################
    def searchData(self,search_no):
        con=connect("Superstore1")
        cur=con.cursor()
        sql = "SELECT * FROM utility1 WHERE customer_contact="+str(search_no)
        cur.execute(sql)
        x=(cur.fetchall())
        con.commit()
        con.close()
        return (x)
####################FOR CREATED STRINGSEARCH################################
    def createdStringofSearch(self,val):
        allreceived = database.searchData(val)
        value = ""
        for eachrecord in allreceived:
            for eachvalue in eachrecord:
                value = value + str(eachvalue) + "\n==============================\n"
        return value
######################FOR DELDATA######################################
    def Deldata(self,delete):
        con=connect("Superstore1")
        cur=con.cursor()

        sql = "DELETE FROM utility1 WHERE customer_contact= " + str(delete)
        cur.execute(sql)
        x=(cur.fetchall())
        con.commit()
        con.close()
        return (x)
###############FOR CREATING STRINGDEL##############################
    def createdStringofDelete(self,val):
        allreceived = database.Deldata(val)
        value = ""
        for eachrecord in allreceived:
            for eachvalue in eachrecord:
                value = value + str(eachvalue) + "\n==============================\n"
        return value
####################FOR SHOW ALL DATA#################################
    def showDataall(self):
        con=connect("Superstore1")
        cur=con.cursor()

        sql = "SELECT * FROM utility1"
        cur.execute(sql)
        x=(cur.fetchall())
        con.commit()
        con.close()
        return (x)
###############FOR CREATINGSTRING OF SHOWALLDATA#####################################
    def createdStringofShowDataAll(self):
        alldata=self.showDataall()
        value=""
        for eachrecord in alldata:

            for eachvalue in (eachrecord):
                value=value+str(eachvalue)+"\n=======================================\n"
        return value
database=saveData()




