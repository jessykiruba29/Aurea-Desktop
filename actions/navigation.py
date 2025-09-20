import pyautogui
import time

def scroll_down(pixels=300):
    """Scroll the current window down by a given number of pixels."""
    try:
        pyautogui.scroll(-pixels)  
        print(f"Scrolled down {pixels} pixels")
    except Exception as e:
        print(f"Error scrolling down: {e}")
