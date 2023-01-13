 # mycursor.execute("select count(*)  as wickets , BowlerId from wicketstatsinnings where BowlerId in ( select player_id  from player where Country = %s )and fk_Match_Id in (select Match_id from matchfixture where match_type = 'T20') group by BowlerId",(x[0],))
    # myresult = mycursor.fetchall()
    # max_wickets = myresult[0][0]
    # id = myresult[0][1]
    # for k in myresult:
    #     if k[0] > max_wickets:
    #         max_wickets = k[0]
    #         id = k[1]
    # mycursor.execute("select First_name,Last_Name from player where player_id = %s and Country=%s",(id,x[0],))
    # name = mycursor.fetchall()
    # name = name[0][0] + " " + name[0][1]
    # x.append(name)
    # x.append(max_wickets)