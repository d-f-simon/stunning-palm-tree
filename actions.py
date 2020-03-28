from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import cx_Oracle
import datetime

dsn_tns = cx_Oracle.makedsn('csoracle.cs.cf.ac.uk', '1521', service_name='csora12edu.cs.cf.ac.uk')
connection = cx_Oracle.connect(user='c1824840', password='12345678Bg', dsn=dsn_tns)
timetable_list = []
class showTimetable(Action):
 def name(self) -> Text:
  return "action_show_timetable"
 def run(self, dispatcher, tracker, domain):
    cursor = connection.cursor()
    cursor.execute("SELECT Module_name,next_class_start,next_class_end, next_class_date FROM Modules,NextClass WHERE Modules.Module_ID = NextClass.Module_ID")
    for i in cursor.fetchall():
        timetable_list.append(i)
    connection.commit()
    return timetable_list