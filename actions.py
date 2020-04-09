from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
import cx_Oracle
import datetime

dsn_tns = cx_Oracle.makedsn('csoracle.cs.cf.ac.uk', '1521', service_name='csora12edu.cs.cf.ac.uk')
connection = cx_Oracle.connect(user='c1824840', password='12345678Bg', dsn=dsn_tns)


class ResetSlot(Action):

    def name(self):
        return "action_reset_slot"

    def run(self, dispatcher, tracker, domain):
        return [SlotSet("TimeTable", [])]



class showTimetable(Action):

 def name(self) -> Text:
  return "action_show_timetable"

 def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
    #day = tracker.get_slot('date') testing this dw about it
    cursor = connection.cursor()
    cursor.execute("SELECT Module_name,next_class_start,next_class_end, next_class_date FROM Modules,NextClass WHERE Modules.Module_ID = NextClass.Module_ID")
    timetable_list = []
    for i in cursor.fetchall():
        timetable_list.append(i)
    return [SlotSet("TimeTable", timetable_list if timetable_list is not None else [])]

class showLecturer(Action):
 def name(self) -> Text:
  return "action_show_lecturers"

 def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
    cursor = connection.cursor()
    cursor.execute("SELECT Lecturer_name, Job_desc, Lecturer_email,School_name, Room_Id FROM Lecturer,Schools WHERE Lecturer.School_ID = Schools.School_ID")
    lecturer = []
    for k in cursor.fetchall():
        # lecturer[k[0]] = [k[1],k[2],k[3],k[4]]
        lecturer.append(k)
    return [SlotSet("Lecturers", lecturer if lecturer is not None else [])]

class actionSU(Action):
 def name(self) -> Text:
  return "action_SU"

 def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
    cursor = connection.cursor()
    cursor.execute("SELECT Event_name,starting_time,ending_time,date_event,Building_name,Location_building FROM Bookings,Rooms,Buildings WHERE Bookings.Room_ID = Rooms.Room_ID AND Buildings.Building_ID = Rooms.Building_ID")
    SU = []
    for k in cursor.fetchall():
        SU.append(k)
    return [SlotSet("Events", SU if SU is not None else [])]
class actionModules(Action):
 def name(self) -> Text:
  return "action_modules"

 def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
    cursor = connection.cursor()
    cursor.execute("SELECT Module_ID, Module_name,Semester,Lecturer_name FROM Modules,Lecturer WHERE Modules.Lecturer_ID = Lecturer.Lecturer_ID")
    Modules = []
    for k in cursor.fetchall():
        Modules.append(k)
    return [SlotSet("Modules", Modules if Modules is not None else [])]

class actionSchools(Action):
 def name(self) -> Text:
  return "action_schools"

 def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
    cursor = connection.cursor()
    cursor.execute("SELECT School_name, Building_name, Location_building FROM Buildings,Schools WHERE Buildings.Building_ID = Schools.Building_ID")
    Schools = []
    for k in cursor.fetchall():
        Schools.append(k)
    return [SlotSet("Schools", Schools if Schools is not None else [])]

class actionRooms(Action):
 def name(self) -> Text:
  return "action_rooms"

 def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
    cursor = connection.cursor()
    cursor.execute("SELECT Room_ID, Building_name FROM Rooms,Buildings WHERE Rooms.Building_ID = Buildings.Building_ID")
    Rooms = []
    for k in cursor.fetchall():
         Rooms.append(k)
    return [SlotSet("Rooms",  Rooms if  Rooms is not None else [])]

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

