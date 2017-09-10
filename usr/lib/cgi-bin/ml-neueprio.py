#!/usr/bin/python3
#----------------------------------------------------------------
#
#----------------------------------------------------------------

import cgi, cgitb, sqlite3
cgitb.enable()
import time

HTML = {ord('ä'): '&auml;', ord('ö'): '&ouml;',
        ord('ü'): '&uuml;', ord('Ä'): '&Auml;',
        ord('Ö'): '&Ouml;', ord('Ü'): '&Uuml;',
        ord('ß'): '&szlig'}

RESPONSE='''Content-Type: text/html

<html>
<meta http-equiv="Content-Type" content="charset=utf-8" />
  <head>
        <title>Daten eingegeben</title>
        <link rel="stylesheet" href="http://192.168.178.25/home/default.css">
 </head>
<body>
  <h3> Danke </h3>
   Die Daten wurden gespeichert.<br/>
   id: &nbsp; %s<br/>
   prio: &nbsp; %s<br/>
   Datum: &nbsp; %s<br/><br/>
   <a href="http://192.168.178.25/cgi-bin/ml-gesamt.py">Uebersicht</a>
  </body>
</html>'''

form = cgi.FieldStorage()
#ida = form.getvalue('id').translate(HTML)
#stat = form.getvalue('status')

ida = form.getvalue('id')
pri = form.getvalue('prio').translate(HTML)

datum = time.localtime()
datziel = str(datum[2])+'.'+str(datum[1])+'.'+str(datum[0])+' '+str(datum[3])+':'+str(datum[4])

#DB initial vorbereiten
connection = sqlite3.connect('/var/www/home/data/todolist.db')
cursor = connection.cursor()

params2 = (pri, ida)
cursor.execute("UPDATE todolist SET prio = (?) WHERE id=(?)", params2)
connection.commit()
params3 = (datziel, ida)
cursor.execute("UPDATE todolist SET anpass = (?) WHERE id=(?)", params3)
connection.commit()
connection.close()

print (RESPONSE % (ida, pri, datziel))
