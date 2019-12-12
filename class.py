
class Student:
	def __init__(self, StudentID, Student_Name, Email):
		#initialise variables
		self.StudentID = StudentID
		self.Student_Name = Student_Name
		self.Email = Email
	#methods
	def Email():
		return Email;

	def Student_Name():
		return Student_Name

	def Student_ID():
		return Student_ID


class Course:
	def __init__(self, CourseID, Course_name):
		#initialise variables
		self.CourseID = CourseID
		self.Course_name = Course_name
		super().__init__(StudentID, Student_Name, Email)
	def Course():
		return Course_ID


class Module:
	def __init__(self, ModuleID, Module_name, Marks, Exam_date, Assessments_due):
		#initialise variables
		self.ModuleID = ModuleID
		self.Module_name = Module_name
		self.Marks = Marks
		self.Exam_date = Exam_date
		self.Assessments_due = Assessments_due
		super().__init__(CourseID, Course_name)
	#methods
	def Module_ID():
		return ModuleID

	def Module_name():
		return Module_name

	def Assessments_due():
		return Assessments_due

	def Exam_date():
		return Exam_date

	# def Modules_taken(): 
	# 	#Would iterate over the objects in the class //Still implementing
	
class Lecturer:
	def __init__(self, LecturerID, Name, Office_location, Lecturer_email):
		#initialise variables
		self.LecturerID = LecturerID
		self.Name = Name
		self.Office_location = Office_location
		self.Lecturer_email = Lecturer_email
		super().__init__(ModuleID, Module_name, Marks, Exam_date, Assessments_due)
	#methods
	def Lecturer_office():
		return Office_location

	def Lecturer_email():
		return Lecturer_email
	
	# def Leading_lecturer_of():
	# 	#would return the lecturer + the module that he/she is leader of  //Still implementing
	
	# def Personal_tutor_info():
	# 	#would return the email, office location and name of the personal tutor by checking where the (personal tutor) student.lecturer_id  = lecturer_id  in the database //Still implementing

class Timetable:
	def __init__(self, Class_ID, Class_title, Starting_time, Duration, Date, Location_class):
		#initialise variables
		self.Class_ID = Class_ID
		self.Class_title = Class_title
		self.Starting_time = Starting_time
		self.Duration = Duration
		self.Date = Date
		self.Location_class = Location_class
		super().__init__(ModuleID, Module_name, Marks, Exam_date, Assessments_due)
	#methods
	def Class_title():
		return Class_title

	def Location_class():
		return Location_class

	# def Timetable():
	# 	#It would return all classes(lectures)/objects in the class by obtaining them from the database //Still implementing

	def Duration_of_class():
		return Duration

	def Starting_time_class():
		return Starting_time

class Building:
	def __init__(self, BuildingID, Building_name, Building_location):
		#initialise variables
		self.BuildingID = BuildingID
		self.Building_name = Building_name
		self.Building_location = Building_location
		super().__init__(StudentID, Student_Name, Email)
	#methods here
	def Building_location():
		return Building_location

	def Building_name():
		return Building_name

class Room:
	def __init__(self, RoomID, Booking_avail):
		#initialise variables
		self.RoomID = RoomID
		self.Booking_avail = Booking_avail
		super().__init__(BuildID, Building_name, Building_location)
	#methods
	def Is_booked():
		booking_avil1 = True #after filling the classess with objects the method would be changed
		if not booking_avil1:
			return RoomID
	# def Booking():
	# 	#would give the student the oppurtinity of booking a room by adding new record in the database //Still implementing
	# def Room_location():
	# 	#would return the building that the room is in, by checking with the database // Still implementing
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
		super().__init__(RoomID, booking_avail)
	#methods
	def Event_name():
		return Event_name

	def Duration():
		return Duration
	def Date_of_event():
		return Date

	def Starting_time():
		return Starting_time

	def Ticket_Price():
		return Ticket_price
