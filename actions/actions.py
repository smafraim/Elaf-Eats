from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker, FormValidationAction
from rasa_sdk.events import SlotSet, EventType,  ActiveLoop, FollowupAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict
import random
import smtplib
import logging
import json

# logger = logging.getLogger(__name__)

class ValidateFoodForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_food_form"
    
    def validate_email(self, slot_value: Any, dispatcher: CollectingDispatcher, tracker: Tracker, domain: DomainDict) -> Dict[Text, Any]:
        if "@" not in slot_value:
            dispatcher.utter_message(text="Please enter a valid email address")
            return {"email": None}
        else:
            sys_otp = str(random.randint(100000, 999999))
            print(f"Generated OTP: {sys_otp}")
            dispatcher.utter_message(text=f"An OTP has been sent to you. Please enter it to verify your identity.")
            return {"email": slot_value, "sys_otp": sys_otp} # store # Store the generated OTP in the sys_otp slot
    
    def validate_user_otp(self, slot_value: Any, dispatcher: CollectingDispatcher, tracker: Tracker, domain: DomainDict) -> Dict[Text, Any]:
        #entered_otp = slot_value  # Using the slot_value directly as it contains the user's input for the OTP
        stored_otp = tracker.get_slot("sys_otp")

        if slot_value == stored_otp:
            dispatcher.utter_message(text="Authentication successful. Welcome premium user!")
            return {"authenticated": True, "user_otp": slot_value}  # Using entered_otp instead of slot_value for clarity
        else:
            dispatcher.utter_message(text="Wrong OTP. Please try again.")
            return {"authenticated": False, "user_otp": None}
    
    
    
    def validate_phone(self, slot_value: Any, dispatcher: CollectingDispatcher, tracker: Tracker, domain: DomainDict) -> Dict[Text, Any]:
        global order_id
        if len(slot_value) == 11:
            return {"phone": slot_value}
        else:
            dispatcher.utter_message(text="Please enter a valid phone number")
            return {"phone": None}
        
    # ALLOWED_FOOD_ITEMS = ["pizza", "burger", "pasta", "biryani"]  # Defining the allowed food items

    def validate_food(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        ALLOWED_FOOD_ITEMS = ["pizza", "burger", "pasta", "biryani"]  # Defining the allowed food items
        if slot_value.lower() not in ALLOWED_FOOD_ITEMS:
            dispatcher.utter_message(text="Sorry, we don't serve that food.")
            return {"food": None}
        else:
            return {"food": slot_value}

    def validate_food_type(self,slot_value: Any, dispatcher: CollectingDispatcher, tracker: Tracker, domain: DomainDict) -> Dict[Text, Any]:
        global order_id
        ALLOWED_FOOD_TYPES = ["veg", "non-veg", "Veggie","Non-Veggie","Vegan", "Halal"]
        if slot_value.lower() not in ALLOWED_FOOD_TYPES:
            dispatcher.utter_message(text="Please enter a valid food type")
            return {"food_type": None}
        else:
            return {"food_type": slot_value}
        
    def validate_cuisine(self, slot_value: Any, dispatcher: CollectingDispatcher, tracker: Tracker, domain: DomainDict) -> Dict[Text, Any]:
        global order_id
        ALLOWED_CUISINES = ["bangladeshi", "mexican", "jamaican", "japanese", "vietnamese", "indian", "chinese", "italian", "korean", "spanish", "french", "german", "british", "irish", "american", "african"]  # Define your allowed cuisines here
        if slot_value.lower() not in ALLOWED_CUISINES:
            dispatcher.utter_message(text="Sorry, we don't serve that cuisine.")
            return {"cuisine": None}
        else:
            # order_id +=1
            # formatted_order_id = f"{order_id:03}"  # This will format the order_id as a three-digit number with leading zeros
            order_id = random.randint(100, 999)
            return {"cuisine": slot_value, "order_id":order_id}#"order_placed": True}
        
    # def validate_order_id(self, slot_value: Any, dispatcher: CollectingDispatcher, tracker: Tracker, domain: DomainDict) -> Dict[Text, Any]:
    #     global order_id
    #     order_placed = tracker.get_slot("order_placed")
    #     if order_placed:
    #         order_id +=1
    #         formatted_order_id = f"{order_id:03}"  # This will format the order_id as a three-digit number with leading zeros
    #         return {"order_id": formatted_order_id}
    #     else:
    #         return {"order_id": None}
    
        
# order_id = 0
#JSON format e jinishptro save kora
class ActionPlaceOrder(Action):
    def name(self) -> Text:
        return "action_place_order"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: DomainDict) -> List[EventType]:
        global order_id

      # Extract the order details from the slots
        name = tracker.get_slot("name")
        email = tracker.get_slot("email")
        phone = tracker.get_slot("phone")
        food_item = tracker.get_slot("food")
        food_type = tracker.get_slot("food_type")
        order_id = tracker.get_slot("order_id")
        cuisine = tracker.get_slot("cuisine")

      #  a dictionary to store the order details
        order_details = {
            "order_id": order_id,
            "name": name,
            "email": email,
            "phone": phone,
            "food_item": food_item,
            "food_type": food_type,
            "cuisine": cuisine,
            }

      # Write the order details to a JSON file
        with open("orders.json", "w") as f:
            json.dump(order_details, f)

        dispatcher.utter_message(response="utter_submit")
        #return [SlotSet("order_placed", True)]

#cancel

class ActionCancelOrder(Action):
    def name(self) -> Text:
        return "action_cancel_order"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: DomainDict) -> List[EventType]:
        # Extract the order ID from the slots
        order_id = tracker.get_slot("order_id")

       # Check if the order exists
        with open("orders.json", "r") as f:
            orders = json.load(f)

        if order_id in orders:
            # Remove the order from the JSON file
            del orders[order_id]

            with open("orders.json", "w") as f:
                json.dump(orders, f)

            dispatcher.utter_message(text="Your order has been cancelled successfully.")
        else:
            dispatcher.utter_message(text="No order found with the given order ID.")

        return []

#modify

class ValidateModifyOrderForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_modify_food_form"
    
    def validate_mod_order_id(self, slot_value: Any, dispatcher: CollectingDispatcher, tracker: Tracker, domain: DomainDict) -> Dict[Text, Any]:
        global order_id
        if slot_value.isdigit():
            return {"mod_order_id": slot_value}
        else:
            dispatcher.utter_message(text="Invalid order number. Please try again.")
            return {"mod_order_id": None}
    
    def validate_new_food_item(self, slot_value: Any, dispatcher: CollectingDispatcher, tracker: Tracker, domain: DomainDict) -> Dict[Text, Any]:
        ALLOWED_FOOD_ITEMS = ["pizza", "burger", "pasta", "biryani"]
        if slot_value is None:
            return {"new_food_item": None}
        else:
            if slot_value.lower() not in ALLOWED_FOOD_ITEMS:
                dispatcher.utter_message(text="Sorry, we don't serve that food.")
                return {"new_food_item": None}
            else:
                return {"new_food_item": slot_value}
    
    def validate_new_food_type(self, slot_value: Any, dispatcher: CollectingDispatcher, tracker: Tracker, domain: DomainDict) -> Dict[Text, Any]:
        ALLOWED_FOOD_TYPES = ["veg", "non-veg", "Veggies","Non-Veggie","Vegan", "Halal"]
        if slot_value.lower() not in ALLOWED_FOOD_TYPES:
            dispatcher.utter_message(text="Sorry, we don't serve that food type")
            return {"new_food_type": None}
        else:
            return {"new_food_type": slot_value}
    
    def validate_new_cuisine(self, slot_value: Any, dispatcher: CollectingDispatcher, tracker: Tracker, domain: DomainDict) -> Dict[Text, Any]:
        ALLOWED_CUISINES = ["bangladeshi", "mexican", "jamaican", "japanese", "vietnamese", "indian", "chinese", "italian", "korean", "spanish", "french", "german", "british", "irish", "american", "african"]
        if slot_value.lower() not in ALLOWED_CUISINES:
            dispatcher.utter_message(text="Sorry, we don't serve that cuisine.")
            return {"new_cuisine": None}
        else:
            return {"new_cuisine": slot_value}

class ActionModifyOrder(Action):
    def name(self) -> Text:
        return "action_modify_order"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: DomainDict) -> List[EventType]:
        name = tracker.get_slot("name")
        email = tracker.get_slot("email")
        phone = tracker.get_slot("phone")
        new_order_id = str(tracker.get_slot("mod_order_id"))
        new_food_item = tracker.get_slot("new_food_item")
        new_food_type = tracker.get_slot("new_food_type")
        new_cuisine = tracker.get_slot("new_cuisine")

        # Read the existing order
        try:
            with open("orders.json", "r") as f:
                order = json.load(f)
        except Exception as e:
            dispatcher.utter_message(text=f"Failed to read the order: {e}")
            return []

        # Check if the order ID matches and update the order
        if str(order["order_id"]) == new_order_id:
           # Extracting name, email, and phone from the order
            name = order.get("name", "")
            email = order.get("email", "")
            phone = order.get("phone", "")
            # Upodating the order
            order['food_item'] = new_food_item
            order['food_type'] = new_food_type
            order['cuisine'] = new_cuisine

            try:
                with open("orders.json", "w") as f:
                    json.dump(order, f)
                dispatcher.utter_message(text="Your order has been modified successfully.")
            except Exception as e:
                dispatcher.utter_message(text=f"Failed to update the order: {e}")
        else:
            dispatcher.utter_message(text="No order found with the given order ID.")

        return []


#below code is for multiple lists inside a dictionary and the upper one is for only single list
# class ActionModifyOrder(Action):
#     def name(self) -> Text:
#         return "action_modify_order"

#     def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: DomainDict) -> List[EventType]:
#         new_order_id = str(tracker.get_slot("mod_order_id"))
#         new_food_item = tracker.get_slot("new_food_item")
#         new_food_type = tracker.get_slot("new_food_type")
#         new_cuisine = tracker.get_slot("new_cuisine")

#         # Read the existing orders
#         try:
#             with open("orders.json", "r") as f:
#                 orders = json.load(f)
#         except Exception as e:
#             dispatcher.utter_message(text=f"Failed to read orders: {e}")
#             return []

#         # Debugging: Print the order ID and existing order IDs
#         print(f"Attempting to modify order ID: {new_order_id}")
#         print(f"Existing order IDs: {list(orders.keys())}")

#         # Finding and updating the order with the matching order_id
#         #order_found = False
#         # for order in orders:
#         #     if str(order["order_id"]) == new_order_id:
#         #         order['food_item'] = new_food_item
#         #         order['food_type'] = new_food_type
#         #         order['cuisine'] = new_cuisine
#         if str(orders["order_id"]) == new_order_id:
#             orders['food_item'] = new_food_item
#             orders['food_type'] = new_food_type
#             orders['cuisine'] = new_cuisine
#                 # order_found = True
#                 # break

#         # if order_found:
#             try:
#                 with open("orders.json", "w") as f:
#                     json.dump(orders, f)
#                 dispatcher.utter_message(text="Your order has been modified successfully.")
#             except Exception as e:
#                 dispatcher.utter_message(text=f"Failed to update order: {e}")
#         else:
#             dispatcher.utter_message(text="No order found with the given order ID.")

#         return []
    
   
    