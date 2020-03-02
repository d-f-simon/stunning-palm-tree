from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import cx_Oracle



class viewTimetableDate(Action):
 def name(self) -> Text:
  return "action_view_timetable_date"
 def run(self, dispatcher, tracker, domain):
  userpwd = "oracle"
  connection = cx_Oracle.connect("hr", userpwd, "CSORA12EDU.CS.CF.AC.UK", encoding="UTF-8")
  with cx_Oracle.connect("hr", userpwd, "CSORA12EDU.CS.CF.AC.UK",
            encoding="UTF-8") as connection:
    cursor = connection.cursor()
    cursor.execute("insert into SomeTable values (:1, :2)",
            (1, "Some string"))
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