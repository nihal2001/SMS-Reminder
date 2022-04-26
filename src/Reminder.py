import sqlite3
from tokenize import String

conn = sqlite3.connect("reminderSMS.db")

#Gets all info from db
def getInfo() -> String:
    cursor = conn.execute("SELECT name, due_date, class FROM Events;")
    str_Info = ""
    for row in cursor:
        str_Info += row[0] + " is due on " + row[1] + "\n"
        
    conn.commit()
    return str_Info;

#Adds event to db
def addEvent(name, due, type):
    conn.execute("INSERT INTO Events VALUES ('"+name+"', '"+due+"', '"+type+"')")
    conn.commit()
    