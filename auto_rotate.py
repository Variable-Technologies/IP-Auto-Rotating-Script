import time
import requests
import stem
from stem import Signal
from stem.control import Controller
import re

# Configuration
TOR_PROXY = {
    'http': 'socks5h://127.0.0.1:9050',
    'https': 'socks5h://127.0.0.1:9050'
}
IP_CHECK_URL = 'http://icanhazip.com'  # Plain-text, no HTML
ROTATION_DELAY = 10  # seconds to wait after NEWNYM
DISPLAY_INTERVAL = 3  # seconds between IP checks

def get_tor_ip():
    try:
        response = requests.get(IP_CHECK_URL, proxies=TOR_PROXY, timeout=10)
        ip = re.search(r'\d+\.\d+\.\d+\.\d+', response.text)
        return ip.group() if ip else "IP not found"
    except Exception as e:
        return f"Error: {str(e)}"

def rotate_tor_ip():
    try:
      with Controller.from_port(port=9051) as controller:
            controller.authenticate()
            controller.signal(Signal.NEWNYM)
    except stem.SocketError:
        print("❌ Could not connect to Tor control port.")
    except stem.connection.AuthenticationFailure:
        print("❌ Authentication failed. Check your Tor config.")

def countdown(seconds):
    for i in range(seconds, 0, -1):
        print(i, end=' ', flush=True)
        time.sleep(1)
    print()

def main():
    print("🔄 Starting Tor IP rotation...\n")
    while True:
        rotate_tor_ip()
        time.sleep(ROTATION_DELAY)
        ip = get_tor_ip()
        print(f"🛡️ Tor IP: {ip}")
        countdown(DISPLAY_INTERVAL)

if __name__ == "__main__":
    main()
