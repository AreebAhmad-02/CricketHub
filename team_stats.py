import mysql.connector
from pathlib import Path


my_connection = mysql.connector.connect(
    host='localhost', user='root', password='SQLKAPASSWORD', database='cricinfosystem2')

mycursor = my_connection.cursor()

mycursor.execute("SELECT team_name FROM cricinfosystem2.team;")
myresult = mycursor.fetchall()
teamStats=[]
for x in myresult:
    x=list(x)
    mycursor.execute("select count(*) as losses from matchfixture where (fk_team_1_id in ( select team_id from team  where  team_name = %s) or fk_team_2_id in (select team_id from team where team_name = %s)) and Matchwinner not  in ( select team_id from team where team_name = %s) and Matchwinner != 0 and match_type = 'T20'",(x[0],x[0],x[0]))
    losses=mycursor.fetchall()
    x.append(losses[0][0])
    mycursor.execute("select count(*) as draws from matchfixture where (fk_team_1_id in ( select team_id from team  where  team_name = %s) or fk_team_2_id in (select team_id from team where team_name = %s)) and Matchwinner = 0 and match_type = 'T20'",(x[0],x[0],))
    draws=mycursor.fetchall()
    x.append(draws[0][0])
    mycursor.execute("select count(*) as wins from matchfixture where (fk_team_1_id in ( select team_id from team  where  team_name = %s) or fk_team_2_id in (select team_id from team where team_name = %s)) and Matchwinner in ( select team_id from team where team_name = %s) and match_type = 'T20'",(x[0],x[0],x[0]))
    wins=mycursor.fetchall()
    x.append(wins[0][0])
    mycursor.execute("select count(*)  as wickets , BowlerId from wicketstatsinnings where BowlerId in ( select player_id  from player where Country = %s )and fk_Match_Id in (select Match_id from matchfixture where match_type = 'T20') group by BowlerId",(x[0],))
    myresult = mycursor.fetchall()
    max_wickets = myresult[0][0]
    id = myresult[0][1]
    for k in myresult:
        if k[0] > max_wickets:
            max_wickets = k[0]
            id = k[1]
    mycursor.execute("select First_name,Last_Name from player where player_id = %s and Country=%s",(id,x[0],))
    name = mycursor.fetchall()
    name = name[0][0] + " " + name[0][1]
    x.append(name)
    x.append(max_wickets)
    
    mycursor.execute(" select max(total_runs) , fk_batter_id from (select (sum(runs_scored)) as total_runs , fk_batter_id from batterstatsininning where fk_batter_id in ( select player_id  from player where Country =%s) and fk_Match_Id in (select Match_id from matchfixture where match_type = 'T20') group by fk_batter_id) as sub ",(x[0],))
    myresult = mycursor.fetchall()
    max_runs = myresult[0][0]
    id = myresult[0][1]
    mycursor.execute("select First_name,Last_Name from player where player_id = %s and Country=%s",(id,x[0],))
    name = mycursor.fetchall()
    name = name[0][0] + " " + name[0][1]
    x.append(name)
    x.append(max_runs)


    #do the same task for ODI and Test
    mycursor.execute("select count(*) as losses from matchfixture where (fk_team_1_id in ( select team_id from team  where  team_name = %s) or fk_team_2_id in (select team_id from team where team_name = %s)) and Matchwinner not  in ( select team_id from team where team_name = %s) and Matchwinner != 0 and match_type = 'ODI'",(x[0],x[0],x[0]))
    losses=mycursor.fetchall()
    x.append(losses[0][0])
    mycursor.execute("select count(*) as draws from matchfixture where (fk_team_1_id in ( select team_id from team  where  team_name = %s) or fk_team_2_id in (select team_id from team where team_name = %s)) and Matchwinner = 0 and match_type = 'ODI'",(x[0],x[0],))
    draws=mycursor.fetchall()
    x.append(draws[0][0])
    mycursor.execute("select count(*) as wins from matchfixture where (fk_team_1_id in ( select team_id from team  where  team_name = %s) or fk_team_2_id in (select team_id from team where team_name = %s)) and Matchwinner in ( select team_id from team where team_name = %s) and match_type = 'ODI'",(x[0],x[0],x[0]))
    wins=mycursor.fetchall()
    x.append(wins[0][0])
    mycursor.execute("select count(*)  as wickets , BowlerId from wicketstatsinnings where BowlerId in ( select player_id  from player where Country = %s )and fk_Match_Id in (select Match_id from matchfixture where match_type = 'ODI') group by BowlerId",(x[0],))
    myresult = mycursor.fetchall()
    if myresult:
        max_wickets = myresult[0][0]
        id = myresult[0][1]
        for k in myresult:
            if k[0] > max_wickets:
                max_wickets = k[0]
                id = k[1]
        mycursor.execute("select First_name,Last_Name from player where player_id = %s and Country=%s",(id,x[0],))
        name = mycursor.fetchall()
        name = name[0][0] + " " + name[0][1]
        x.append(name)
        x.append(max_wickets)
    else:
        x.append("No data")
        x.append("No data")

    mycursor.execute(" select max(total_runs) , fk_batter_id from (select (sum(runs_scored)) as total_runs , fk_batter_id from batterstatsininning where fk_batter_id in ( select player_id  from player where Country =%s) and fk_Match_Id in (select Match_id from matchfixture where match_type = 'ODI') group by fk_batter_id) as sub ",(x[0],))
    
    myresult = mycursor.fetchall()
    if myresult[0][0]:
        max_runs = myresult[0][0]
        id = myresult[0][1]
        mycursor.execute("select First_name,Last_Name from player where player_id = %s and Country=%s",(id,x[0],))
        name = mycursor.fetchall()
        name = name[0][0] + " " + name[0][1]
        
        x.append(name)
        x.append(max_runs)
    else:
        x.append("No data")
        x.append("No data")


    mycursor.execute("select count(*) as losses from matchfixture where (fk_team_1_id in ( select team_id from team  where  team_name = %s) or fk_team_2_id in (select team_id from team where team_name = %s)) and Matchwinner not  in ( select team_id from team where team_name = %s) and Matchwinner != 0 and match_type = 'Test'",(x[0],x[0],x[0]))
    losses=mycursor.fetchall()
    x.append(losses[0][0])
    mycursor.execute("select count(*) as draws from matchfixture where (fk_team_1_id in ( select team_id from team  where  team_name = %s) or fk_team_2_id in (select team_id from team where team_name = %s)) and Matchwinner = 0 and match_type = 'Test'",(x[0],x[0],))
    draws=mycursor.fetchall()
    x.append(draws[0][0])
    mycursor.execute("select count(*) as wins from matchfixture where (fk_team_1_id in ( select team_id from team  where  team_name = %s) or fk_team_2_id in (select team_id from team where team_name = %s)) and Matchwinner in ( select team_id from team where team_name = %s) and match_type = 'Test'",(x[0],x[0],x[0]))
    wins=mycursor.fetchall()
    x.append(wins[0][0])
    mycursor.execute("select count(*)  as wickets , BowlerId from wicketstatsinnings where BowlerId in ( select player_id  from player where Country = %s )and fk_Match_Id in (select Match_id from matchfixture where match_type = 'Test') group by BowlerId",(x[0],))
    myresult = mycursor.fetchall()

    if myresult:
        max_wickets = myresult[0][0]
        id = myresult[0][1]
        for k in myresult:
            if k[0] > max_wickets:
                max_wickets = k[0]
                id = k[1]
        mycursor.execute("select First_name,Last_Name from player where player_id = %s and Country=%s",(id,x[0],))
        name = mycursor.fetchall()
        name = name[0][0] + " " + name[0][1]
        x.append(name)
        x.append(max_wickets)
    else:
        x.append("No data")
        x.append("No data")

    mycursor.execute(" select max(total_runs) , fk_batter_id from (select (sum(runs_scored)) as total_runs , fk_batter_id from batterstatsininning where fk_batter_id in ( select player_id  from player where Country =%s) and fk_Match_Id in (select Match_id from matchfixture where match_type = 'Test') group by fk_batter_id) as sub ",(x[0],))

    myresult = mycursor.fetchall()
    if myresult[0][0]:
        max_runs = myresult[0][0]
        id = myresult[0][1]
        mycursor.execute("select First_name,Last_Name from player where player_id = %s and Country=%s",(id,x[0],))
        name = mycursor.fetchall()
        name = name[0][0] + " " + name[0][1]
        
        x.append(name)
        x.append(max_runs)
    else:
        x.append("No data")
        x.append("No data")

    teamStats.append(x)
    

for i in teamStats:
    print(i)