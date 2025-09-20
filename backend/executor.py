import importlib

def execute_intent(intent_data):
    intent_name = intent_data["intent"]

    try:
        if intent_name == "open_url":
            module = importlib.import_module("actions.browser")
            module.open_url(intent_data["slots"].get("url", "https://google.com"))

        elif intent_name == "scroll_down":
            module = importlib.import_module("actions.navigation")
            module.scroll_down()

        elif intent_name == "open_app":
            module = importlib.import_module("actions.system")
            module.open_app(intent_data["slots"].get("app_name"))

        else:
            print(f"No executor found for intent: {intent_name}")
    except Exception as e:
        print(f"Error executing intent: {e}")
