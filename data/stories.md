<!-- this is where it is decided which action is completed after the bot has determined the intent 
      put custom actions in here so that they are executed -->

## greet path
* greet
  - utter_greet

## happy path
* mood_great
  - utter_happy

## sad path 1
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* affirm
  - utter_happy

## sad path 2
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* deny
  - utter_goodbye

## say goodbye
* goodbye
  - utter_goodbye

## find_lecturer
* find_lecturer
    - action_show_lecturers
    - utter_lecturer

## time table time
* timetable_time
  - utter_empty_time

## time table date
* timetable_date
  - action_show_timetable
  - utter_timetable
  <!-- - action_reset_slot -->

## find room
* find_room
  - action_FindRoom
  - utter_find_room

## who
* who
  - utter_who

## events
* events
    - action_SU
    - utter_events

## modules
* modules
    - action_modules
    - utter_modules

## schools
* schools
    - action_schools
    - utter_schools

## rooms
* rooms
    - action_rooms
    - utter_rooms

## address
* address
    - action_where
    - utter_where

## LecturerOffice
* LecturerOffice
    - action_office
    - utter_office

## LecturerEmail
* LecturerEmail
    - аction_lecturer_email
    - utter_email