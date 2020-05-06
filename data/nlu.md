<!-- this is where the bot decides intent based on how similar the user input is to "training data" under each heading, if you want a certain input to give a certain intent put it in here -->

## intent:greet
- hey
- hello
- hi
- good morning
- good evening
- hey there

## intent:goodbye
- bye
- goodbye
- see you around
- see you later

## intent:affirm
- yes
- indeed
- of course
- that sounds good
- correct

## intent:deny
- no
- never
- I don't think so
- don't like that
- no way
- not really

## intent:mood_great
- perfect
- very good
- great
- amazing
- wonderful
- I am feeling very good
- I am great
- I'm good

## intent:mood_unhappy
- sad
- very sad
- unhappy
- bad
- very bad
- awful
- terrible
- not very good
- extremely sad
- so sad

## intent:weather
- what is the weather [today](date)
- what's the weather [today](date)
- what is the weather outside

## intent:who
- who are you?
- what are you?
- are you a bot?
- are you a human?
- who am I talking to?
- am I talking to a bot?
- am I talking to a human?

## intent:feeling
- how are you?
- how are you feeling
- tell me how you're feeling

## intent:timetable_date
- what is my timetable [today](date)
- what is my timetable for [today](date)
- what is my timetable [tomorrow](date)
- what is my timetable for [tomorrow](date)
- what is my timetable on [monday](date)
- what is my timetable on [tuesday](date)
- what is my timetable on [wednesday](date)
- what is my timetable on [thursday](date)
- what is my timetable on [friday](date)
- what lectures do I have [today](date)
- what lectures do I have [tomorrow](date)
- what are my lectures for [tomorrow](date)
- what are my lectures for [today](date)
- show my timetable for [tomorrow](date)
- timetable
- show me my timetable

## intent:timetable_time
- timetable time
- time lecture

## intent:find_room
- where can i find room
- where is room 

## intent:find_lecturer
- what lecturers do you have in db
- show me lecturer information

## intent:events
- what are the upcoming events in SU
- what events are on [today](date)
- what events are on [tomorrow](date)
- what events are on in the SU[tomorrow](date)
- what events are on [monday](date)
- what events are on [tuesday](date)
- what events are on [wednesday](date)
- what events are on [thursday](date)
- what events are on [friday](date)
- show me upcoming events
- upcoming events

## intent:modules
- what are my modules
- modules

## intent:schools
- schools
- what schools are there
- what are the schools in the university
- show me the schools of the university

## intent:rooms
- rooms
- list all the rooms
- what are the rooms in the university

## intent:address
- tell me more about location
- where is the location
- what is the address
- where is 
- where are the law buildings
- what is the address for the law buildings?

##intent:directions
- give me directions to
- where can i find 
- how can i get to
- how can I get to the school of engineering
- show me the way to 
- I can't find 
- How do I get to the school of engineering
- how do i get to law buildings
- how do I get to the queens buildings
- how do I get to the school of medicine

## intent:LecturerOffice
- what is the office of lecturer
- what is randy adams office
- can you tell me the office of mike bowker
- I need the office of steve talbot
- lecturer office
- John Smiths office
- show me the office of Mike Bowker

## intent:LecturerEmail
- what is the email of lecturer
- what is randy adams email
- can you tell me the email of mike bowker
- I need the email of steve talbot
- lecturer email
- John Smiths email
- show me the email of Mike Bowker

## intent:PersonalTutor
- who is my personal tutor
- personal tutor
- Can you tell me who my personal tutor is?

## intent:NotUnderstood
- 
- .
- fdsafdasfda

## intent:Exam
- exam date
- when is the exam of
- exam

## intent:Assessment
- assessment date
- when is the assessment of
- assessment
- what is the date of assessment

## intent:SendingEmail
- Can I send email
- I need to send an email
- send an email
- send an email to [example@hotmail.com](receiver)
- Can i send an email to [events@cardiff.ac.uk](receiver)
- Can I send an email to [John@gmail.com](receiver)
- Can I send an email to [Grig@gmail.com](receiver)
- Can I send an email to [Andon@outlook.com](receiver)
- Can I send an email to [Grig@outlook.com](receiver)
- Can I send an email to [GribachevA@cardiff.ac.uk](receiver)
- Can I send an email to [Grig@cardiff.ac.uk](receiver)

## intent: receiver_entry
-[John@gmail.com](receiver)
-[Andon@gmail.com](receiver)
-[Andon@outlook.com](receiver)
-[Grig@outlook.com](receiver)
-[GribachevA@cardiff.ac.uk](receiver)
-[collierj5@cardiff.ac.uk](receiver)
-[Grig@cardiff.ac.uk](receiver)
-[example@hotmail.com](receiver)
-[moreexamples@hotmail.com](receiver)
-[example@hotmail.co.uk](receiver)

## intent: subject_entry
-[Inquiry](subject)
-the subject is [Inquiry](subject)
-[event booking](subject)
-[Personal](subject)
-[Distribution](subject)
-[Offer](subject)
-[Story](subject)
-[Urgency](subject)
-[Urgent Inquiry](subject)
-[Urgent inquiry](subject)
-[inquiry](subject)
-[inquiries](subject)
-[Greetings](subject)
-[important](subject)
-[meeting](subject)


## intent: body_entry
-[qweasd](body)
-[asdzxc](body)
-[TestText](body)
-[Test](body)
-[Hello](body)
-[Dear](body)
-[Hello Mr](body)
-[Hello Ms](body)
-[Dear Mr](body)
-[Dear Ms](body)
-[I would like to book one ticket for healthcare Give it a go, many thanks](body)

## intent:confirm
- yes
- that's all
- yes that helps
- thank you
- yes thank you