import pymysql.cursors

connection = pymysql.connect(host='34.211.148.131',
                             user='mbdsuser',
                             password='mbds2017',
                             db='mbdsdb',
                             port=3306,
                             cursorclass=pymysql.cursors.DictCursor)

try:
    with connection.cursor() as cursor:
        sql = "SHOW tables"
        cursor.execute(sql)
        result = cursor.fetchall()
        print result
                
#        sql = "SHOW COLUMNS FROM bigdatasurvey"
#        cursor.execute(sql)
#        result = cursor.fetchall()        
#        print type(result)
        
#        for item in result:
#            print item
        
#        sql = "INSERT INTO bigdatasurvey VALUES ('Joey Bingham', 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1)"
#        cursor.execute(sql)

#	sql = "SELECT * from bigdatasurvey WHERE name != 'Eric Rozier' "
#	cursor.execute(sql)
#	result = cursor.fetchall()
#	for item in result:
#		print item	
       
        connection.commit()

finally:
    connection.close()
