## happy path
* greet
  - utter_greet
  - action_hello_world
* mood_great
  - utter_happy

## search incident happy path
* greet
  - utter_greet
  - action_hello_world
* search_provider{"facility_type":"incident","number":"INC0010002"}
  - action_facility_search
  
* thanks
  - utter_goodbye

## search incident+number
* greet
  - utter_greet
  - action_hello_world
* search_provider{"facility_type":"incident"}
  - utter_ask_location
* inform{"number":"INC0010002"}
  - action_facility_search
* thanks
  - utter_goodbye

## search incident
* search_provider{"facility_type":"incident","number":"INC0010002"}
  - action_facility_search
  
  
* thanks
  - utter_goodbye

## sad path 1
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* affirm
  - utter_happy

## sad path 2
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* deny
  - utter_goodbye

## say goodbye
* goodbye
  - utter_goodbye

## bot challenge
* bot_challenge
  - utter_iamabot
