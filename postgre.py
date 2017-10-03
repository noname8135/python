import psycopg2

con = psycopg2.connect(database='iii_prj', user='iii_prj',password='ilovesgc',port='1234',host='140.123.103.160') 
cur = con.cursor()			#holder of returned result
query = "INSERT INTO blacklist(id,ip,rec_date) VALUES (DEFAULT,%s,%s)"
value = i,"%s" % (today)
try:
	cur.execute(query,value)
	con.commit()
	print "%s INSERTED" % i
except:
	query = "UPDATE blacklist SET rec_date = %s WHERE ip=%s" % (today,i)
	print "%s UPDATED" % i
	
	
query = "SELECT * FROM account"
cur.execute(query)
for i in cur:
	print i
#or curfetchone()

