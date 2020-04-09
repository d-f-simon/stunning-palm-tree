from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
import cx_Oracle
from datetime import date

dsn_tns = cx_Oracle.makedsn('csoracle.cs.cf.ac.uk', '1521', service_name='csora12edu.cs.cf.ac.uk')
connection = cx_Oracle.connect(user='c1824840', password='12345678Bg', dsn=dsn_tns)



class getDate():
    def date_choice(day):


        #dateTimeObj = date.today()
        #timeStampStrToday = dateTimeObj.strftime("%d/%m/%Y")
        #dateTimeObj = date.tomorrow()
        #timeStampStrTomorrow = dateTimeObj.strftime("%d/%m/%Y")
        timeStampStrToday = '19/04/2020'
        timeStampStrTomorrow = '20/04/2020'

        if day  == 'today':
            date_choice = timeStampStrToday
        elif day == 'tomorrow':
            date_choice = timeStampStrTomorrow

        return str(date_choice)

class ResetSlot(Action):

    def name(self):
        return "action_reset_slot"

    def run(self, dispatcher, tracker, domain):
        return [SlotSet("TimeTable", [])]



class showTimetable(Action):
 def name(self) -> Text:
  return "action_show_timetable"

 def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
    
    cursor = connection.cursor()
    cursor.execute("SELECT Module_name,next_class_start,next_class_end, next_class_date FROM Modules,NextClass WHERE Modules.Module_ID = NextClass.Module_ID")
    timetable_list = []
    timetable_string = ""
    timetable_string_temp = ""

    day = tracker.get_slot('date')
    message = tracker.latest_message.get('text')
    
    for i in cursor.fetchall():
        timetable_list.append(i)

    if 'today' in message or 'tomorrow' in message:
        for k in timetable_list:
            if k[3] == getDate.date_choice(day):
                timetable_string_temp = "Module name: " + k[0] + ", Starting at: " + k[1] + ", Ending at: " + k[2] + ", Date " + k[3] + "<br /> "
                timetable_string += timetable_string_temp

        if timetable_string == '':
            timetable_string = "currently empty."
    else:
        for k in timetable_list:
            timetable_string_temp = "Module name: " + k[0] + ", Starting at: " + k[1] + ", Ending at: " + k[2] + ", Date " + k[3] + "<br /> "
            timetable_string += timetable_string_temp

        
    return [SlotSet("TimeTable", timetable_string)]

class showLecturer(Action):
 def name(self) -> Text:
  return "action_show_lecturers"

 def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
    cursor = connection.cursor()
    cursor.execute("SELECT Lecturer_name, Job_desc, Lecturer_email,School_name, Room_Id FROM Lecturer,Schools WHERE Lecturer.School_ID = Schools.School_ID")
    lecturer = []
    lecturer_string_temp = ""
    lecturer_string = ""
    for k in cursor.fetchall():
        lecturer.append(k)
    for i in lecturer:
        lecturer_string_temp = "Lecturer name: " + i[0] + ", Job Description: " + i[1] + ", Lecturer email: " + i[2] + ", School of " + i[3] + ", Office: " + i[4] + "<br /> "
        lecturer_string += lecturer_string_temp
    return [SlotSet("Lecturers", lecturer_string)]

class actionSU(Action):
 def name(self) -> Text:
  return "action_SU"

 def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
    cursor = connection.cursor()
    cursor.execute("SELECT Event_name,starting_time,ending_time,date_event,Building_name,Location_building FROM Bookings,Rooms,Buildings WHERE Bookings.Room_ID = Rooms.Room_ID AND Buildings.Building_ID = Rooms.Building_ID")
    SU = []
    SU_string_temp = ""
    SU_string = ""
    day = tracker.get_slot('date')
    message = tracker.latest_message.get('text')

    for k in cursor.fetchall():
        SU.append(k)

    if 'today' in message or 'tomorrow' in message:
        for i in SU:
            print(i[3])
            if i[3] == getDate.date_choice(day):
                SU_string_temp = "Event name: " + i[0] + ", Starting time: " + i[1] + ", Ending time: " + i[2] + ", Date of the event: " + i[3] + ", At: " + i[4] + "<br /> "
                SU_string += SU_string_temp

        if SU_string == '':
            SU_string = "no upcoming events"
    else:
        for i in SU:
            SU_string_temp = "Event name: " + i[0] + ", Starting time: " + i[1] + ", Ending time: " + i[2] + ", Date of the event: " + i[3] + ", At: " + i[4] + "<br /> "
            SU_string += SU_string_temp

    return [SlotSet("Events", SU_string)]

class actionModules(Action):
 def name(self) -> Text:
  return "action_modules"

 def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
    cursor = connection.cursor()
    cursor.execute("SELECT Module_ID, Module_name,Semester,Lecturer_name FROM Modules,Lecturer WHERE Modules.Lecturer_ID = Lecturer.Lecturer_ID")
    Modules = []
    Modules_string_temp = ""
    Modules_string = ""
    for k in cursor.fetchall():
        Modules.append(k)
    for i in Modules:
        Modules_string_temp = "Module code: " + i[0] + ", Module name: " + i[1] + ", Semester: " + i[2] + ", Leading lecturer: " + i[3] + "<br /> "
        Modules_string += Modules_string_temp
    return [SlotSet("Modules", Modules_string)]

class actionSchools(Action):
 def name(self) -> Text:
  return "action_schools"

 def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
    cursor = connection.cursor()
    cursor.execute("SELECT School_name, Building_name, Location_building FROM Buildings,Schools WHERE Buildings.Building_ID = Schools.Building_ID")
    Schools = []
    School_string = ""
    Schools_string_temp = ""
    for k in cursor.fetchall():
        Schools.append(k)
    for i in Schools:
        Schools_string_temp = "School of " + i[0] + ", Building of the school: " + i[1] + "<br /> "
        Schools_string += Schools_string_temp
    return [SlotSet("Schools", Schools_string)]

class actionRooms(Action):
 def name(self) -> Text:
  return "action_rooms"

 def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
    cursor = connection.cursor()
    cursor.execute("SELECT Room_ID, Building_name FROM Rooms,Buildings WHERE Rooms.Building_ID = Buildings.Building_ID")
    Rooms = []
    Rooms_string = ""
    Rooms_string_temp = ""
    for k in cursor.fetchall():
         Rooms.append(k)
    for i in Rooms:
        Rooms_string_temp = "Room : " + i[0] + " Located in: " + i[1] + "<br /> "
        Rooms_string += Rooms_string_temp
    return [SlotSet("Rooms",  Rooms_string)]

class actionWhere(Action):
 def name(self) -> Text:
  return "action_where"

 def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
    cursor = connection.cursor()
    cursor.execute("SELECT School_name, Building_name, Location_building FROM Buildings,Schools WHERE Buildings.Building_ID = Schools.Building_ID")
    Buildings = []
    message = tracker.latest_message.get('text')
    for k in cursor.fetchall():
         Buildings.append(k)
    for j in Buildings:
        if j[0] in message:
            return [SlotSet("Address", j[2])]
        elif j[1] in message:
            return [SlotSet("Address", j[2])]

class actionFindRoom(Action):
 def name(self) -> Text:
  return "action_FindRoom"

 def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
    cursor = connection.cursor()
    cursor.execute("SELECT Room_ID, Building_name FROM Rooms,Buildings WHERE Rooms.Building_ID = Buildings.Building_ID")
    Rooms = []
    message = tracker.latest_message.get('text')
    for k in cursor.fetchall():
         Rooms.append(k)
    for j in Rooms:
        if j[0] in message:
            return [SlotSet("Room Location", j[1])]

class actionOffice(Action):
 def name(self) -> Text:
  return "action_office"

 def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
    cursor = connection.cursor()
    cursor.execute("SELECT Lecturer_name,Room_ID FROM Lecturer")
    Office = []
    message = tracker.latest_message.get('text')
    for k in cursor.fetchall():
         Office.append(k)
    for j in Office:
        if j[0] in message:
            return [SlotSet("Office", j[1])]

class actionEmail(Action):
 def name(self) -> Text:
  return "аction_lecturer_email"

 def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
    cursor = connection.cursor()
    cursor.execute("SELECT Lecturer_name,Lecturer_email FROM Lecturer")
    Email = []
    message = tracker.latest_message.get('text')
    for k in cursor.fetchall():
         Email.append(k)
    for j in Email:
        if j[0] in message:
            return [SlotSet("Email", j[1])]

connection.commit()

