from stt import listen_to_speech
from nlu import get_intent
from executor import execute_intent
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

WAKE_WORD = "hey"
STOP_WORDS = ["stop", "exit", "quit"]

def main():
    print("Aurea is idle. Say 'Hey Aurea' to wake me up...")
    listening = False  

    while True:
        text = listen_to_speech()
        if not text:
            continue

        text_lower = text.lower().strip()

        if not listening:
            if text_lower.startswith(WAKE_WORD):
                print("Yes? I'm listening to you now...")
                listening = True
            continue

        if listening:
            if text_lower in STOP_WORDS:
                print("Stopping active listening. Say 'Hey Aurea' to wake me again.")
                listening = False
                continue

            intent_data = get_intent(text_lower)
            if intent_data:
                execute_intent(intent_data)
            else:
                print("Sorry, I didn't understand that.")

if __name__ == "__main__":
    main()
