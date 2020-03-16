import cx_Oracle
import datetime
#The following line below would work only if you have connected through the VPN - OpenVPN program
dsn_tns = cx_Oracle.makedsn('csoracle.cs.cf.ac.uk', '1521', service_name='csora12edu.cs.cf.ac.uk')
#this is the connectivity line that works with my server.
conn = cx_Oracle.connect(user='', password='', dsn=dsn_tns) #Oracle username and password
curs = conn.cursor()
curs.arraysize=50
timetable_list = []
lecturer_list = []
schools_buildings_list = []
modules_info_list = []
events_SU = []
curs.execute('SELECT Module_name,next_class_start,next_class_end, next_class_date FROM Modules,NextClass WHERE Modules.Module_ID = NextClass.Module_ID')
for i in curs.fetchall():
        timetable_list.append(i)
curs.execute('SELECT Lecturer_name, Job_desc, Lecturer_email,School_name, Room_Id FROM Lecturer,Schools WHERE Lecturer.School_ID = Schools.School_ID')
for k in curs.fetchall():
	lecturer_list.append(k)
curs.execute('SELECT School_name, Building_name, Location_building FROM Buildings,Schools WHERE Buildings.Building_ID = Schools.Building_ID')
for j in curs.fetchall():
	schools_buildings_list.append(j)
curs.execute('SELECT Module_ID, Module_name,Semester,Lecturer_name FROM Modules,Lecturer WHERE Modules.Lecturer_ID = Lecturer.Lecturer_ID')
for a in curs.fetchall():
	modules_info_list.append(a)
curs.execute('SELECT Event_name,starting_time,ending_time,date_event,Building_name,Location_building FROM Bookings,Rooms,Buildings WHERE Bookings.Room_ID = Rooms.Room_ID AND Buildings.Building_ID = Rooms.Building_ID')
for b in curs.fetchall():
	events_SU.append(b)
print("1 - Will print out your timetable:")
print("2 - Will print out information about lecturers:")
print("3 - Will print out information about buildings and schools:")
print("4 - Will print out information about modules:")
print("5 - Will print out information about the upcoming SU events:")
x = input("Which option would you like to choose: ")
print(x)
if x == "1":
        for u in timetable_list:
                print("Module : " + u[0] + ", Starting time: " + u[1] + ", Ending time: " + u[2] + ", Date: " + u[3])
elif x == "2":
        for y in lecturer_list:
                print("Lecturer : " + y[0] + ", Working as " + y[1] + ", Email: " + y[2] + ", In the school of: " + y[3] + ", With Office: " + y[4])
elif x == "3":
        for c in schools_buildings_list:
                print("School of: " + c[0] + ", Building name: " + c[1] + ", Address: " + c[2])
elif x == "4":
        for z in modules_info_list:
                print("Module code: " + z[0] + ", Module name: " + z[1] + ", Semester: " + z[2] + ", Leading lecturer: " + z[3])
elif x == "5":
        for m in events_SU:
                print("Event: " + m[0] + ", Starting time: " + m[1] + ", Ending time: " + m[2] + ", Date: " + m[3] + ", Building: " + m[4] + ", Address: " + m[5])        
else:
	print("Wrong input, start the program again")
curs.close()
conn.close()
