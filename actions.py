# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import requests
import json


class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_hello_world"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        msg = {"type": "video", "payload": {
            "src": "https://youtube.com/embed/9C1Km6xfdMA"}}
        dispatcher.utter_message(text="Hello World!", attachment=msg)

        return []


class ActionFacilitySearch(Action):


    """example of custom action"""


    def name(self):

        """name of the custom action"""

        return "action_facility_search"


    def run(self, dispatcher, tracker, domain):


        """action for display all tickets in freshdesk"""

        number = tracker.get_slot("number")  # number=INC0010002

        ticket_url = 'https://dev95710.service-now.com/api/now/table/incident?sysparm_query=number%3D'+number + \
            '&sysparm_fields=opened_by%2Cinc_short_description%2Cdescription%2Cinc_closed_by%2Cinc_sys_created_by%2Cincident_state%2Csys_updated_by&sysparm_limit=1'

        user = 'admin'

        pwd = '6RqQFofl8NGe'

        headers = {"Accept": "application/json"}

        response = requests.get(ticket_url, auth=(user, pwd), headers=headers)

        message = response.json()


        '''if response.status_code != 200:

        print('Status:', response.status_code, 'Headers:', response.headers, 'Error Response:', response.content)'''

        dispatcher.utter_message(message)

        return []
