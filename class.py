class Event:
	def __init__(self, EventID, Event_name, Booker_name, Duration, Starting_time, Date, Ticket_Price):
		#initialise variables
		self.EventID = EventID
		self.Event_name = Event_name
		self.Booker_name = Booker_name
		self.Duration = Duration
		self.Starting_time = Starting_time
		self.Date = Date
		self.Ticket_Price
	#functions
	def Event_name():
		#do something

	def Duration():
		#do something

	def Date():
		#do something

class Building:
	def __init__(self, BuildingID, Building_name, Building_location):
		#initialise variables
		self.BuildingID = BuildingID
		self.Building_name = Building_name
		self.Building_location = Building_location
	#functions here
	def Building_location():
		#do something

	def Building_name():
		#do something

class Room:
	def __init__(self, RoomID, Booking_avail):
		#initialise variables
		self.RoomID = RoomID
		self.Booking_avail = Booking_avail
	#functions
	def Is_booked():
		#do something
	def Booking():
		#do something
	def Room_location():
		#do something

class Student:
	def __init__(self, StudentID, Name, Password, Email, Personal_tutor_name, Personal_tutor_email):
		#initialise variables
		self.StudentID = StudentID
		self.Name = Name
		self.Password = Password
		self.Email = Email
		self.Personal_tutor_name = Personal_tutor_name
		self.Personal_tutor_email = Personal_tutor_email
	#functions
	def Login():
		#do something

	def Personal_tutor():
		#do something


class Lecturer:
	def __init__(self, LecturerID, Name, Office_location, Lecturer_email):
		#initialise variables
		self.LecturerID = LecturerID
		self.Name = Name
		self.Office_location = Office_location
		self.Lecturer_email = Lecturer_email
	#functions
	def Lecturer_name():
		#do something

	def Lecturer_office():
		#do something

	def Lecturer_email():
		#do something


class Course:
	def __init__(self, CourseID, Course_name):
		#initialise variables
		self.CourseID = CourseID
		self.Course_name = Course_name
	#functions
	def Course():
		#do something

	def Modules_taken():
		#do something


class Timetable:
	def __init__(self, TimetableID, Lecture_Lab, Starting_time, Duration):
		#initialise variables
		self.TimetableID = TimetableID
		self.Lecture_Lab = Lecture_Lab
		self.Starting_time = Starting_time
		self.Duration = Duration
	#functions
	def Class_room():
		#do something

	def Lab_or_Lecture():
		#do something

	def Timetable():
		#do something

	def Duration_of_class():
		#do something

class Module:
	def __init__(self, ModuleID, Module_name, Marks, Exam_date, Assessments_due):
		#initialise variables
		self.ModuleID = ModuleID
		self.Module_name = Module_name
		self.Marks = Marks
		self.Exam_date = Exam_date
		self.Assessments_due = Assessments_due
	#functions
	def Module_name():
		#do something

	def Assessments_due():
		#do something

	def Exam_date():
		#do something

	def Marks():
		#do something

	def Leading_lecturer():
		#do something
