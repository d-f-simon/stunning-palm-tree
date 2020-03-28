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
  - utter_find_room

## who
* who
  - utter_who

