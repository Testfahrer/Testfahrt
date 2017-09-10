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
        <title>Neue Aktion</title>
        <link rel="stylesheet" href="http://192.168.178.25/home/default.css">
  </head>
<body>
  <h2> Danke </h2>
   Die Daten wurden gespeichert.<br/>
   id: &nbsp; %s<br/>
   Aktion: &nbsp; %s<br/>
   Inhalt: &nbsp; %s<br/>
   Status: &nbsp; %s<br/>
   Prio: &nbsp; %s<br/>
   Startdat: &nbsp; %s<br/>
   Anpassung: &nbsp; %s<br/>
   Zieldat: &nbsp; %s<br/>
   Euro: &nbsp; %s<br/> 
   <a href="http://192.168.178.25/cgi-bin/ml-gesamt.py">Zurueck zur Uebersicht</a>
  </body>
</html>'''

ida = ''
akt = ''
inh = ''
stat = ''
prio = ''
datstart=''
anpass = ''
datziel = ''
euro = ''

datum = time.localtime()
datstart = str(datum[2])+'.'+str(datum[1])+'.'+str(datum[0])+' '+str(datum[3])+':'+str(datum[4])
anpass = str(datum[2])+'.'+str(datum[1])+'.'+str(datum[0])+' '+str(datum[3])+':'+str(datum[4])

form = cgi.FieldStorage()

ida = form.getvalue('ida')
akt = form.getvalue('akt').translate(HTML)
inh = form.getvalue('inh').translate(HTML)
stat = form.getvalue('stat').translate(HTML)
prio = form.getvalue('prio')
datziel = form.getvalue('datziel').translate(HTML)
euro = form.getvalue('euro')

#DB initial vorbereiten
connection = sqlite3.connect('/var/www/home/data/todolist.db')
cursor = connection.cursor()
#-----------------------------------------------
#sql = "CREATE TABLE aktiv(" \
#      "id INTEGER PRIMARY KEY, " \
#      "aktion TEXT, " \
#      "inhalt TEXT, " \
#      "status TEXT, " \
#      "prio INTEGER, " \
#      "datstart INTEGER)"
#      "anpass INTEGER)"
#      "datziel TEXT, " \
#      "euro INTEGER)"
#---------------------------------------------------

params = (ida, akt, inh, stat, prio, datstart, anpass, datziel, euro)

cursor.execute("INSERT INTO todolist VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", params)
 
connection.commit()
connection.close()

print (RESPONSE % (ida, akt, inh, stat, prio, datstart, anpass, datziel, euro))
