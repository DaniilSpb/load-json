import cgi, sys,os
import json
from tokenize import String

form = cgi.FieldStorage()         
print("Content­type: text/html")  

html ="""
<html>
<link type="text/css" rel="stylesheet" href="../style_table.css"/>
<body>
<H1>Json table</H1>
<table border =2> <tr>  <td>Ключ</td><td>Значение</td>  </tr>
"""
print (html)
obj = json.loads(form["myFile"].value)
for key in obj:
     print ('<tr><td> %s </td> <td> %s </td></tr>'% (key, obj[key]))
print ('</table>')

