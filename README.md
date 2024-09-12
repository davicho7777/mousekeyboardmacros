# Macro Recorder & Player GUI

This project is a Python-based graphical user interface (GUI) tool designed to automate repetitive tasks. It allows users to record mouse clicks, keystrokes, delays, and text searches on the screen. These sequences (macros) can be saved, loaded, and replayed multiple times. The application is built using Tkinter for the GUI and various third-party libraries to handle mouse and keyboard inputs, screen captures, and text recognition.

## Features

- **Record Mouse Clicks**: Capture both left and right mouse clicks, along with their screen coordinates.
- **Record Keystrokes**: Record keyboard inputs for automated playback.
- **Apply Delays**: Add delays between actions for more accurate automation.
- **Save & Load Macros**: Save recorded macros to a JSON file and reload them for later use.
- **Replay Macros**: Repeat macros multiple times with optional random delay variations.
- **Text Search on Screen**: Search for specified text in a spiral pattern on the screen, using Optical Character Recognition (OCR) via Tesseract.
- **Manage Macros**: View, play, or delete saved macros through an intuitive interface.

## Requirements

This project requires **Python 3.6** or later.

### Python Libraries

Install the required libraries by running the following pip commands:
```bash
pip install pyautogui
pip install mouse
pip install Pillow
pip install pytesseract
pip install opencv-python
pip install numpy
