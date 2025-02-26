import cv2
import numpy as np
import os
from colorama import init, Style

init()

ASCII_CHARS = "@%#*+=-:. "

def frame_to_ascii(frame):
    height, width, _ = frame.shape
    scale = 0.1

    small_frame = cv2.resize(frame, (int(width * scale), int(height * scale)))
    ascii_image = ""

    for row in small_frame:
        for pixel in row:
            r, g, b = pixel
            brightness = int(0.2989 * r + 0.5870 * g + 0.1140 * b)
            char = ASCII_CHARS[int(brightness / 256 * len(ASCII_CHARS))]
            color_code = f"\033[38;2;{r};{g};{b}m"
            ascii_image += f"{color_code}{char}{Style.RESET_ALL}"
        ascii_image += "\n"

    return ascii_image

cap = cv2.VideoCapture(1)

try:
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        ascii_frame = frame_to_ascii(frame)

        os.system("clear" if os.name == "posix" else "cls")
        print(ascii_frame, end="")
except KeyboardInterrupt:
    pass
finally:
    cap.release()
    cv2.destroyAllWindows()

