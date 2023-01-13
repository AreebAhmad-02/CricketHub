import mysql.connector
from pathlib import Path


my_connection = mysql.connector.connect(
    host='localhost', user='root', password='SQLKAPASSWORD', database='cricinfosystem2')

mycursor = my_connection.cursor()

team_name_1='Pakistan'
team_name_2='Zimbabwe'
matchData=[]
mycursor.execute("Select event_name,MatchDate,  match_id,fk_team_1_id,fk_team_2_id, Matchwinner_desc from matchfixture join series using(series_id) where fk_team_1_id in (select team_id from team where team_name = %s or team_name like CONCAT('%', %s, '%')) or fk_team_2_id in (select team_id from team where team_name = %s or team_name like CONCAT('%', %s, '%'))",(team_name_1,team_name_2,team_name_1,team_name_2))
available_matches=mycursor.fetchall()
for i in available_matches:
    if i[0]=="England tour of Pakistan":
        continue
    my_match = []
    for j in i:
        my_match.append(j)
        



    mycursor.execute("select sum(extra_runs) + sum(scored_runs) as Totalscore from balls where match_id=%s  group by Match_id,inning;",(my_match[2],))
    total_score=mycursor.fetchall()


    mycursor.execute("select count(*) as wickets from wicketstatsinnings where fk_match_id=%s  group by fk_Match_id,InningNumber", (my_match[2],))
    wickets=mycursor.fetchall()

    for t in zip(total_score,wickets):
            my_match.append(t)
    matchData.append(my_match)
for u in matchData:
    mycursor.execute("select team_name from team where team_id=%s;",(u[3],))
    u[3]=mycursor.fetchall()[0][0]
    mycursor.execute("select team_name from team where team_id=%s;",(u[4],))
    u[4]=mycursor.fetchall()[0][0]

for i in matchData:
    print(i[7][0][0])
    