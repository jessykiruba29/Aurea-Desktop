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

        elif intent_name == "add_task":
            module = importlib.import_module("actions.tasks")
            task_name = intent_data["slots"].get("task_name")
            time = intent_data["slots"].get("time")
            module.add_task(task_name, time)

        elif intent_name == "list_tasks":
            module = importlib.import_module("actions.tasks")
            module.list_tasks()

        elif intent_name == "remove_task":
            module = importlib.import_module("actions.tasks")
            task_name = intent_data["slots"].get("task_name")
            module.remove_task(task_name)

        else:
            print(f"No executor found for intent: {intent_name}")

    except Exception as e:
        print(f"Error executing intent: {e}")
