import webbrowser

def open_url(url="https://google.com"):
    """Open a URL in the default browser."""
    try:
        webbrowser.open(url)
        print(f"🌐 Opening URL: {url}")
    except Exception as e:
        print(f"Error opening URL {url}: {e}")
