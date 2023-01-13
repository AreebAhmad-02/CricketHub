import mysql.connector
from pathlib import Path


my_connection = mysql.connector.connect(
    host='localhost', user='root', password='SQLKAPASSWORD', database='cricinfosystem2')

mycursor = my_connection.cursor()

mycursor.execute("select count(*)  as wickets , BowlerId from wicketstatsinnings where BowlerId in ( select player_id  from player where Country = 'Pakistan' )and fk_Match_Id in (select Match_id from matchfixture where match_type = 'T20') group by BowlerId")
myresult = mycursor.fetchall()
max_wickets = myresult[0][0]
id = myresult[0][1]
for x in myresult:
    if x[0] > max_wickets:
        max_wickets = x[0]
        id = x[1]
mycursor.execute("select First_name,Last_Name from player where player_id = %s",(id,))
name = mycursor.fetchall()
name = name[0][0] + " " + name[0][1]

print(id,name,max_wickets)
    