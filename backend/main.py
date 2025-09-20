from stt import listen_to_speech
from nlu import get_intent
from executor import execute_intent

def main():
    print("Aurea listening. Say something...")
    while True:
        text = listen_to_speech()
        if text.lower() in ["exit", "quit", "stop"]:
            print("Shutting down...")
            break

        intent_data = get_intent(text)
        if intent_data:
            execute_intent(intent_data)
        else:
            print("Sorry, I didn't understand that.")

if __name__ == "__main__":
    main()
