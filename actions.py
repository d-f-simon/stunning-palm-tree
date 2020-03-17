from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import cx_Oracle
import datetime

dsn_tns = cx_Oracle.makedsn('csoracle.cs.cf.ac.uk', '1521', service_name='csora12edu.cs.cf.ac.uk')
timetable_list = []
class showTimetable(Action):
 def name(self) -> Text:
  return "action_show_timetable"
 def run(self, dispatcher, tracker, domain):
  connection = cx_Oracle.connect(user='c1824840', password='12345678Bg', dsn=dsn_tns)
  with cx_Oracle.connect("c1824840", "12345678Bg", "CSORA12EDU.CS.CF.AC.UK",
            encoding="UTF-8") as connection:
    cursor = connection.cursor()
    cursor.execute("SELECT Module_name,next_class_start,next_class_end, next_class_date FROM Modules,NextClass WHERE Modules.Module_ID = NextClass.Module_ID",
            (1, "Some string"))
    for i in curs.fetchall():
        timetable_list.append(i)
    connection.commit()















class viewTimetableTime(Action):
 def name(self) -> Text:
  return "action_view_timetable_time"
 def run(self, dispatcher, tracker, domain):
  userpwd = "oracle"
  connection = cx_Oracle.connect("hr", userpwd, "CSORA12EDU.CS.CF.AC.UK", encoding="UTF-8")
  with cx_Oracle.connect("hr", userpwd, "CSORA12EDU.CS.CF.AC.UK",
            encoding="UTF-8") as connection:
    cursor = connection.cursor()
    cursor.execute("insert into SomeTable values (:1, :2)",
            (1, "Some string"))
    connection.commit()

class suEventsDate(Action):
 def name(self) -> Text:
  return "action_view_su_events_date"
 def run(self, dispatcher, tracker, domain):
  userpwd = "oracle"
  connection = cx_Oracle.connect("hr", userpwd, "CSORA12EDU.CS.CF.AC.UK", encoding="UTF-8")
  with cx_Oracle.connect("hr", userpwd, "CSORA12EDU.CS.CF.AC.UK",
            encoding="UTF-8") as connection:
    cursor = connection.cursor()
    cursor.execute("insert into SomeTable values (:1, :2)",
            (1, "Some string"))
    connection.commit()

class suEventsTime(Action):
 def name(self) -> Text:
  return "action_view_su_events_time"
 def run(self, dispatcher, tracker, domain):
  userpwd = "oracle"
  connection = cx_Oracle.connect("hr", userpwd, "CSORA12EDU.CS.CF.AC.UK", encoding="UTF-8")
  with cx_Oracle.connect("hr", userpwd, "CSORA12EDU.CS.CF.AC.UK",
            encoding="UTF-8") as connection:
    cursor = connection.cursor()
    cursor.execute("insert into SomeTable values (:1, :2)",
            (1, "Some string"))
    connection.commit()

class locateLocation(Action):
 def name(self) -> Text:
  return "action_locate_location"
 def run(self, dispatcher, tracker, domain):
  userpwd = "oracle"
  connection = cx_Oracle.connect("hr", userpwd, "CSORA12EDU.CS.CF.AC.UK", encoding="UTF-8")
  with cx_Oracle.connect("hr", userpwd, "CSORA12EDU.CS.CF.AC.UK",
            encoding="UTF-8") as connection:
    cursor = connection.cursor()
    cursor.execute("insert into SomeTable values (:1, :2)",
            (1, "Some string"))
    connection.commit()