"""
Budget Buddy - Personal Budget PWA
Serves the app locally so you can install it on your phone.
"""

import os
import sys
import webbrowser
from flask import Flask, send_from_directory

if getattr(sys, 'frozen', False):
    BASE_DIR = os.path.dirname(sys.executable)
else:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__, static_folder=BASE_DIR)


@app.route('/')
def index():
    return send_from_directory(BASE_DIR, 'index.html')


@app.route('/manifest.json')
def manifest():
    return send_from_directory(BASE_DIR, 'manifest.json')


@app.route('/sw.js')
def service_worker():
    return send_from_directory(BASE_DIR, 'sw.js')


@app.route('/icons/<path:filename>')
def icons(filename):
    return send_from_directory(os.path.join(BASE_DIR, 'icons'), filename)


if __name__ == '__main__':
    import socket
    # Get local IP so your phone can connect
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)

    print("=" * 50)
    print("  Budget Buddy is running!")
    print("=" * 50)
    print(f"\n  On this computer: http://localhost:5000")
    print(f"  On your phone:    http://{local_ip}:5000")
    print(f"\n  To install on iPhone:")
    print(f"  1. Open Safari on your phone")
    print(f"  2. Go to http://{local_ip}:5000")
    print(f"  3. Tap the Share button (box with arrow)")
    print(f"  4. Tap 'Add to Home Screen'")
    print(f"\n  Both devices must be on the same WiFi!")
    print("=" * 50)
    print("\n  Press Ctrl+C to stop.\n")

    webbrowser.open('http://localhost:5000')
    app.run(host='0.0.0.0', port=5000, debug=False)
