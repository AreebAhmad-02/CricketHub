import mysql.connector
from pathlib import Path


my_connection = mysql.connector.connect(
    host='localhost', user='root', password='SQLKAPASSWORD', database='cricinfosystem2')

mycursor = my_connection.cursor()

mycursor.execute("SELECT * FROM cricinfosystem2.player;")
players=mycursor.fetchall()
n=0
playersData=[]
for i in players:
    #covert i to list
    i=list(i)
    #append player id to list
    mycursor.execute("select sum(runs)/(sum(deliveries) /6) as Economy_Rate from bowlerstatsininning where fk_bowler_id in ( select player_id from player where player_id=%s ) and fk_match_id in ( select Match_id from matchfixture where match_type = 'T20' ) group by fk_bowler_id;",(i[0],))
    economy_rate=mycursor.fetchall()
    if len(economy_rate)==0:
        economy_rate=[(None,)]
        #append in i array
        i.append(economy_rate[0][0])
    else:
        i.append(economy_rate[0][0])
    mycursor.execute("select sum(runs)/(sum(deliveries) /6) as Economy_Rate from bowlerstatsininning where fk_bowler_id in ( select player_id from player where player_id=%s ) and fk_match_id in ( select Match_id from matchfixture where match_type = 'ODI' ) group by fk_bowler_id;",(i[0],))
    economy_rate=mycursor.fetchall()
    if len(economy_rate)==0:
        economy_rate=[(None,)]
        #append in i array
        i.append(economy_rate[0][0])
    else:
        i.append(economy_rate[0][0])
    mycursor.execute("select sum(runs)/(sum(deliveries) /6) as Economy_Rate from bowlerstatsininning where fk_bowler_id in ( select player_id from player where player_id=%s ) and fk_match_id in ( select Match_id from matchfixture where match_type = 'Test' ) group by fk_bowler_id;",(i[0],))
    economy_rate=mycursor.fetchall()
    if len(economy_rate)==0:
        economy_rate=[(None,)]
        #append in i array
        i.append(economy_rate[0][0])
    else:
        i.append(economy_rate[0][0])
    
    mycursor.execute("select sum(runs_scored)/count(fk_Match_Id) as Avg from batterstatsininning where fk_batter_id in ( select player_id from player where player_id=%s ) and fk_match_id in ( select Match_id from matchfixture where match_type = 'T20' ) group by fk_batter_id",(i[0],))
    avg=mycursor.fetchall()
    if len(avg)==0:
        avg=[(None,)]
        i.append(avg[0][0])
    else:
        i.append(avg[0][0])

    mycursor.execute("select sum(runs_scored)/count(fk_Match_Id) as Avg from batterstatsininning where fk_batter_id in ( select player_id from player where player_id=%s ) and fk_match_id in ( select Match_id from matchfixture where match_type = 'ODI' ) group by fk_batter_id",(i[0],))
    avg=mycursor.fetchall()
    if len(avg)==0:
        avg=[(None,)]
        i.append(avg[0][0])
    else:
        i.append(avg[0][0])
    
    mycursor.execute("select sum(runs_scored)/count(fk_Match_Id) as Avg from batterstatsininning where fk_batter_id in ( select player_id from player where player_id=%s ) and fk_match_id in ( select Match_id from matchfixture where match_type = 'Test' ) group by fk_batter_id",(i[0],))
    avg=mycursor.fetchall()
    if len(avg)==0:
        avg=[(None,)]
        i.append(avg[0][0])
    else:
        i.append(avg[0][0])
    

    mycursor.execute("select count(fk_Match_Id) as total_Matches from batterstatsininning where fk_batter_id in ( select player_id from player where player_id=%s) and fk_match_id in ( select Match_id from matchfixture where match_type = 'T20' ) group by fk_batter_id",(i[0],))
    total_matches=mycursor.fetchall()
    if len(total_matches)==0:
        total_matches=[(None,)]
        i.append(total_matches[0][0])
    else:
        i.append(total_matches[0][0])

    mycursor.execute("select count(fk_Match_Id) as total_Matches from batterstatsininning where fk_batter_id in ( select player_id from player where player_id=%s) and fk_match_id in ( select Match_id from matchfixture where match_type = 'ODI' ) group by fk_batter_id",(i[0],))
    total_matches=mycursor.fetchall()
    if len(total_matches)==0:
        total_matches=[(None,)]
        i.append(total_matches[0][0])
    else:
        i.append(total_matches[0][0])

    mycursor.execute("select count(fk_Match_Id) as total_Matches from batterstatsininning where fk_batter_id in ( select player_id from player where player_id=%s) and fk_match_id in ( select Match_id from matchfixture where match_type = 'Test' ) group by fk_batter_id",(i[0],))
    total_matches=mycursor.fetchall()
    if len(total_matches)==0:
        total_matches=[(None,)]
        i.append(total_matches[0][0])
    else:
        i.append(total_matches[0][0])

    
    mycursor.execute("select sum(runs_scored)/sum(ballfaced) * 100 as strike_rate from batterstatsininning where fk_batter_id in ( select player_id from player where player_id=%s) and fk_match_id in ( select Match_id from matchfixture where match_type = 'T20' ) group by fk_batter_id",(i[0],))
    strike_rate=mycursor.fetchall()
    if len(strike_rate)==0:
        strike_rate=[(None,)]
        i.append(strike_rate[0][0])
    else:
        i.append(strike_rate[0][0])

    mycursor.execute("select sum(runs_scored)/sum(ballfaced) * 100 as strike_rate from batterstatsininning where fk_batter_id in ( select player_id from player where player_id=%s) and fk_match_id in ( select Match_id from matchfixture where match_type = 'ODI' ) group by fk_batter_id",(i[0],))
    strike_rate=mycursor.fetchall()
    if len(strike_rate)==0:
        strike_rate=[(None,)]
        i.append(strike_rate[0][0])
    else:
        i.append(strike_rate[0][0])

    mycursor.execute("select sum(runs_scored)/sum(ballfaced) * 100 as strike_rate from batterstatsininning where fk_batter_id in ( select player_id from player where player_id=%s) and fk_match_id in ( select Match_id from matchfixture where match_type = 'Test' ) group by fk_batter_id",(i[0],))
    strike_rate=mycursor.fetchall()
    if len(strike_rate)==0:
        strike_rate=[(None,)]
        i.append(strike_rate[0][0])
    else:
        i.append(strike_rate[0][0])

    mycursor.execute("select count(*) as '3w' from (select count(*) as '3w' from wicketstatsinnings where BowlerId in ( select player_id from player where player_id=%s ) and fk_match_id in ( select Match_id from matchfixture where match_type = 'T20' ) group by BowlerId , fk_match_id having count(*) >= 3) as anothertable",(i[0],))
    wickets=mycursor.fetchall()
    if len(wickets)==0:
        wickets=[(None,)]
        i.append(wickets[0][0])
    else:
        i.append(wickets[0][0])

    mycursor.execute("select count(*) as '3w' from (select count(*) as '3w' from wicketstatsinnings where BowlerId in ( select player_id from player where player_id=%s ) and fk_match_id in ( select Match_id from matchfixture where match_type = 'ODI' ) group by BowlerId , fk_match_id having count(*) >= 3) as anothertable",(i[0],))
    wickets=mycursor.fetchall()
    if len(wickets)==0:
        wickets=[(None,)]
        i.append(wickets[0][0])
    else:
        i.append(wickets[0][0])

    mycursor.execute("select count(*) as '3w' from (select count(*) as '3w' from wicketstatsinnings where BowlerId in ( select player_id from player where player_id=%s ) and fk_match_id in ( select Match_id from matchfixture where match_type = 'Test' ) group by BowlerId , fk_match_id having count(*) >= 3) as anothertable",(i[0],))
    wickets=mycursor.fetchall()
    if len(wickets)==0:
        wickets=[(None,)]
        i.append(wickets[0][0])
    else:
        i.append(wickets[0][0])

    mycursor.execute("select count(fk_Match_Id) as '50s' from batterstatsininning where fk_batter_id in ( select player_id from player where player_id=%s ) and fk_match_id in ( select Match_id from matchfixture where match_type = 'T20' ) and runs_scored > 50 group by fk_batter_id",(i[0],))
    fifties=mycursor.fetchall()
    if len(fifties)==0:
        fifties=[(None,)]
        i.append(fifties[0][0])
    else:
        i.append(fifties[0][0])
    
    mycursor.execute("select count(fk_Match_Id) as '50s' from batterstatsininning where fk_batter_id in ( select player_id from player where player_id=%s ) and fk_match_id in ( select Match_id from matchfixture where match_type = 'ODI' ) and runs_scored > 50 group by fk_batter_id",(i[0],))  
    fifties=mycursor.fetchall()
    if len(fifties)==0:
        fifties=[(None,)]
        i.append(fifties[0][0])
    else:
        i.append(fifties[0][0])

    mycursor.execute("select count(fk_Match_Id) as '50s' from batterstatsininning where fk_batter_id in ( select player_id from player where player_id=%s ) and fk_match_id in ( select Match_id from matchfixture where match_type = 'Test' ) and runs_scored > 50 group by fk_batter_id",(i[0],))
    fifties=mycursor.fetchall()
    if len(fifties)==0:
        fifties=[(None,)]
        i.append(fifties[0][0])
    else:
        i.append(fifties[0][0])

    mycursor.execute("select max(runs_scored) from batterstatsininning where fk_batter_id in ( select player_id from player where player_id=%s ) and fk_match_id in ( select Match_id from matchfixture where match_type = 'T20' ) group by fk_batter_id",(i[0],))
    highest_score=mycursor.fetchall()
    if len(highest_score)==0:
        highest_score=[(None,)]
        i.append(highest_score[0][0])
    else:
        i.append(highest_score[0][0])

    mycursor.execute("select max(runs_scored) from batterstatsininning where fk_batter_id in ( select player_id from player where player_id=%s ) and fk_match_id in ( select Match_id from matchfixture where match_type = 'ODI' ) group by fk_batter_id",(i[0],))
    highest_score=mycursor.fetchall()
    if len(highest_score)==0:
        highest_score=[(None,)]
        i.append(highest_score[0][0])
    else:
        i.append(highest_score[0][0])

    mycursor.execute("select max(runs_scored) from batterstatsininning where fk_batter_id in ( select player_id from player where player_id=%s ) and fk_match_id in ( select Match_id from matchfixture where match_type = 'Test' ) group by fk_batter_id",(i[0],))
    highest_score=mycursor.fetchall()
    if len(highest_score)==0:
        highest_score=[(None,)]
        i.append(highest_score[0][0])
    else:
        i.append(highest_score[0][0])

    mycursor.execute("select sum(runs)/sum(deliveries) * 100 as strike_rate from bowlerstatsininning where fk_bowler_id in ( select player_id from player where player_id=%s ) and fk_match_id in ( select Match_id from matchfixture where match_type = 'T20' ) group by fk_bowler_id",(i[0],))
    strike_rate=mycursor.fetchall()
    if len(strike_rate)==0:
        strike_rate=[(None,)]
        i.append(strike_rate[0][0])
    else:
        i.append(strike_rate[0][0])

    mycursor.execute("select sum(runs)/sum(deliveries) * 100 as strike_rate from bowlerstatsininning where fk_bowler_id in ( select player_id from player where player_id=%s ) and fk_match_id in ( select Match_id from matchfixture where match_type = 'ODI' ) group by fk_bowler_id",(i[0],))
    strike_rate=mycursor.fetchall()
    if len(strike_rate)==0:
        strike_rate=[(None,)]
        i.append(strike_rate[0][0])
    else:
        i.append(strike_rate[0][0])

    mycursor.execute("select sum(runs)/sum(deliveries) * 100 as strike_rate from bowlerstatsininning where fk_bowler_id in ( select player_id from player where player_id=%s ) and fk_match_id in ( select Match_id from matchfixture where match_type = 'Test' ) group by fk_bowler_id",(i[0],))
    strike_rate=mycursor.fetchall()
    if len(strike_rate)==0:
        strike_rate=[(None,)]
        i.append(strike_rate[0][0])
    else:
        i.append(strike_rate[0][0])


    
    playersData.append(i)


for i in playersData:
    print(i)





