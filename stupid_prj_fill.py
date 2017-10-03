import requests
import string
import re
import urllib
import sys
import datetime
import re
import random
#datetime.datetime.now().month


def print_data_in_db():
	payload2={}
	payload2['unit_cd1'] = plan
	payload2['sy'] = year
	payload2['sm'] = year
	payload2['ey'] = month
	payload2['em'] = month
	payload2['sd'] = '01'
	payload2['ed'] = '28'
	payload2['go'] = "%E4%BE%9D%E6%A2%9D%E4%BB%B6%E9%81%B8%E5%87%BA%E8%B3%87%E6%96%99"
	result = s.post("http://miswww1.cc.ccu.edu.tw/pt_proj/print_row.php",data=payload2)
	print result.content[300:]
	print "************************************"

def generate_SN(s,plan,year): #if succeed, it'll generate SN and remove data in db
	unit_cd1=plan
	payload = {}
	payload['go'] =  "%E4%BE%9D%E6%A2%9D%E4%BB%B6%E9%81%B8%E5%87%BA%E8%B3%87%E6%96%99"
	payload['sm'] = "01"
	payload['sd'] = "01"
	payload['sy'] = year
	payload['ey'] = year
	payload['em'] = '12'
	payload['ed'] = '28'
	payload['unit_cd1'] = plan
	result = s.post("http://miswww1.cc.ccu.edu.tw/pt_proj/print_row.php",data=payload)
	#print result.content
	del payload
	rec_num = result.content.count('<td rowspan="2"')
	print "%d Record loaded..." % rec_num
	payload = {}
	payload['chka'] = 'on'
	for i in range(0,rec_num):
		payload['cb_'+str(i)]='1'
	payload['go_check']='%E7%A2%BA%E5%AE%9A%E9%80%81%E5%87%BA%E4%B8%A6%E5%88%97%E5%8D%B0'
	result = s.post("http://miswww1.cc.ccu.edu.tw/pt_proj/print_check.php",data=payload)
	#print result.content
	p = re.compile("<u>\d+</u>")
	print p.findall(result.content)	#testing~

if __name__ == '__main__':
	year=str(datetime.datetime.now().year-1911)
	month=str(datetime.datetime.now().month)
	plan_opt = {0:"104-00134",1:"103-01789"}
	plan_select = int(raw_input('''Which project?
0 => internal science council
1 => Creative XXXX -- Pao-An Shiung
Select your project: '''
	))
	plan = plan_opt[plan_select]
	if plan_select == 0:
		total_hour = 25

	elif plan_select == 1:
		total_hour = 60

	#"103-01452" #internal science council
	#"103-01789"  #CREATIVE -- Pao-An Shiung

	msg = 'Total hour: %d, Date:%s, Proceed? (0/1)' % (total_hour,year+'_'+month)
	if int(raw_input(msg)) == 0:
		year = raw_input("Which year?(10x)").replace('\n','')
		month = raw_input("Which month?(1~12)").replace('\n','')
		if int(month) < 1 or int(month) > 12:
			print "abort"
			sys.exit()
		print 'Continue with month %s' % month
	s = requests.Session()

	s.post('http://miswww1.cc.ccu.edu.tw/pt_proj/control.php', data={'staff_cd':'Q123989302','passwd':'xczwfj','proj_type':'3'}) #fill your account, passwd and assistance type
	s.get("http://miswww1.cc.ccu.edu.tw/pt_proj/control2.php")	#session registering...fuck it
	#print_data_in_db()


	task=['%E9%96%8B%E6%9C%83%E8%A8%8E%E8%AB%96',
	'%E6%92%B0%E5%AF%AB%E7%A8%8B%E5%BC%8F',
	'%E6%B8%AC%E8%A9%A6%E7%A8%8B%E5%BC%8F',
	'%E7%A0%94%E8%AE%80%E8%AB%96%E6%96%87'
	]
	rand_hour = [3,4,5,6]
	url = 'http://miswww1.cc.ccu.edu.tw/pt_proj/next.php'

	payload = {}
	payload['type']= plan
	payload['yy']= year
	payload['mm']= month

	payload['workin']=urllib.unquote('%E8%87%BA%E7%B6%9C%E5%A4%A7%E6%A0%A1%E5%9C%92%E4%B8%BB%E6%A9%9F%E8%B3%87%E5%AE%89%E6%8E%A7%E7%AE%A1%E7%B3%BB%E7%B5%B1')

	day_walker = 1

	while total_hour > 0 and day_walker < 29:
		if not 0 <= datetime.date(int(payload['yy'])+1911,int(payload['mm']),day_walker).weekday() < 5: #check week of day
			day_walker += 2
		payload['dd']=str(day_walker)
		if total_hour < 5:
			payload['workin'] = urllib.unquote("%E5%BE%AE%E8%AA%BF%E8%88%87%E9%A9%97%E6%94%B6%E6%88%90%E6%9E%9C")
		else :
			payload['workin'] = urllib.unquote(random.choice(task))
		work_hour = random.choice(rand_hour)
		payload['hrs'] = str(work_hour)
		result = s.post(url,data=payload)
		total_hour -= work_hour
		day_walker += 1

	result = s.get("http://miswww1.cc.ccu.edu.tw/pt_proj/todb.php")	#write to db
	#print result.content
	#sys.exit()
	if 'logout' in result:
		print "DB SYNC ERROR :p"
		sys.exit()
	#FILLING DONE~!
	generate_SN(s,plan,year) 	#testing 
