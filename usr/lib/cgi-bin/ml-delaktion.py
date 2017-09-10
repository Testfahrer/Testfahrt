#!/usr/bin/python3
#----------------------------------------------------------------
#
#----------------------------------------------------------------

import cgi, cgitb, sqlite3
cgitb.enable()

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
  <h2> Danke </h2>
   Folgender ID Satz wurde entfernt.<br/>
   id: &nbsp; %s<br/><br/>
   <a href="http://192.168.178.25/cgi-bin/ml-gesamt.py">Zurueck zur Uebersicht</a>
  </body>
</html>'''

#ida=''

form = cgi.FieldStorage()
ida = form.getvalue('ida')


#Zeilen anhand id löschen 
connection = sqlite3.connect('/var/www/home/data/todolist.db')
cursor = connection.cursor()
params1 = (ida)
cursor.execute("DELETE FROM todolist WHERE id = (?)", [params1])
connection.commit()
connection.close()

print (RESPONSE % (ida))
