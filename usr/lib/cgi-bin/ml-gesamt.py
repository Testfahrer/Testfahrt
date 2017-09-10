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
        <title>Gesamtliste</title>
        <link rel="stylesheet" href="http://192.168.178.25/home/default.css">
  </head>
<body>
  <h1> Liste </h1>
    <p></p>
    <table border='1'>
    <tr class="fi">\
    <td align="center">ID</td> \
    <td align="center">Aktion</td> \
    <td>Inhalt</td> \
    <td>Status</td> \
    <td align="center">Prio</td> \
    <td align="center">Startdatum</td> \
    <td align="center">Update</td> \
    <td align="center">Zieldatum</td> \
    <td>Euro</td> \
    </tr>
      %s  
    </table>   
    </p>
    <form method="get"
	action="http://192.168.178.25/cgi-bin/ml-delaktion.py">
     Welche ID soll weg?
       <input type="number" name="ida" size=6>
      <input type="Submit" value="Commit"/>
    </form>

    <form method="get"
	action="http://192.168.178.25/cgi-bin/ml-neuerstatus.py">
     Welche ID welcher Status__?
       <input type="number" name="id" size=6>
       <input type="text" name="status" size=25>   
      <input type="Submit" value="Commit"/>
    </form>

    <form method="get"
	action="http://192.168.178.25/cgi-bin/ml-neueprio.py">
     Welche ID welche Prio__?
       <input type="number" name="id" size=6>
       <input type="number" name="prio" size=25>   
      <input type="Submit" value="Commit"/>
    </form>

    <form method="get"
	action="http://192.168.178.25/cgi-bin/ml-neuerinhalt.py">
     Welche ID welcher Inhalt__?
	<input type="number" name="id" size=3>
	<input type="text" name="inhalt" size=40>
       <input type="Submit" value="Commit"/>
    </form>

    <form method="get"
	action="http://192.168.178.25/cgi-bin/ml-neueaktion.py">
     Neue Aktion eingeben? *=Pflicht
     </P>
	*Aktion___<input type="text" name="akt" size=20></p>
	*Inhalt___<input type="text" name="inh" size=40></p>
	*Status_____<input type="text" name="stat" size=6></p>
	*Prio_____<input type="number" name="prio" size=6></p>
	*Zieldatum_<input type="text" name="datziel" size=12></p>
	*Betrag_<input type="number" name="euro" size=12></p>
       <input type="Submit" value="Commit"/>
    </form>

    <a href="http://192.168.178.25/">Startseite</a></p> 
  </body>
</html>'''

conn=sqlite3.connect('/var/www/home/data/todolist.db')
c = conn.cursor()
query = '''SELECT * FROM todolist ORDER BY prio ASC'''
c.execute(query)

qwert = ''
summe1 = 0
erledig = 0
asdf = ''

#try:
for dsatz in c:
    summe1 += 1
    if dsatz[3]==('erledigt'):
        erledig += 1
        asdf='1'
        qwert += ('<tr>\
        <td align="center">%s</td> \
        <td align="left">%s</td> \
        <td>%s</td> \
        <td bgcolor="green">%s</td> \
        <td align="center">%s</td> \
        <td align="center">%s</td> \
        <td align="center">%s</td> \
        <td align="center">%s</td> \
        <td>%s</td> \
        </tr>' % (dsatz[0], dsatz[1], dsatz[2], dsatz[3], dsatz[4], dsatz[5], dsatz[6], dsatz[7], dsatz[8])) 

    elif dsatz[3]!= ('erledigt') and dsatz[4]==(1):
        #erledig += 1
        #asdf='3'
        qwert += ('<tr>\
        <td align="center">%s</td> \
        <td align="left">%s</td> \
        <td>%s</td> \
        <td>%s</td> \
        <td align="center" bgcolor="red">%s</td> \
        <td align="center">%s</td> \
        <td align="center">%s</td> \
        <td align="center">%s</td> \
        <td>%s</td> \
        </tr>' % (dsatz[0], dsatz[1], dsatz[2], dsatz[3], dsatz[4], dsatz[5], dsatz[6], dsatz[7], dsatz[8])) 

    else:
        asdf='2'
        qwert += ('<tr>\
        <td align="center">%s</td> \
        <td align="left">%s</td> \
        <td>%s</td> \
        <td>%s</td> \
        <td align="center">%s</td> \
        <td align="center">%s</td> \
        <td align="center">%s</td> \
        <td align="center">%s</td> \
        <td>%s</td> \
        </tr>' % (dsatz[0], dsatz[1], dsatz[2], dsatz[3], dsatz[4], dsatz[5], dsatz[6], dsatz[7], dsatz[8])) 

print (RESPONSE % qwert)

print ('Anzahl aller Aktionen ----> ',(summe1))
print ('davon sind aktuell',(summe1-erledig),'offen und',(erledig),'erledigt.')
#print (qwert)
#	ID______<input type="number" name="ida" size=3></p>
#	Startdatum_<input type="number" name="datstart" size=12></p>
#	Updatedat__<input type="number" name="anpass" size=6></p>

#except:
#    print (RESPONSE % ('Leider sind keine Daten vorhanden.'))
    
#      <input type="text" name="datstart" size=12>
