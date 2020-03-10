import cx_Oracle
import datetime
#The following line below would work only if you have connected through the VPN - OpenVPN program
dsn_tns = cx_Oracle.makedsn('csoracle.cs.cf.ac.uk', '1521', service_name='csora12edu.cs.cf.ac.uk')
#this is the connectivity line that works with my server.
conn = cx_Oracle.connect(user='', password='', dsn=dsn_tns) #Oracle username and password
curs = conn.cursor()
curs.arraysize=50
dates = []
list1 = []
k = 0
curs.execute('SELECT Module_name,next_class_start,next_class_end, next_class_date FROM Modules,NextClass WHERE Modules.Module_ID = NextClass.Module_ID')
print('TIMETABLE')
print('Module name \  Next Class starting at: \ Next Class ending at: \ Date of class: ')
for i in curs.fetchall():
        list1.append(i)
        print(i)
curs.close()
conn.close()
