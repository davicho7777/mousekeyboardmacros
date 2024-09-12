# Macro Recorder & Player GUI

This project is a windows Python-based graphical user interface (GUI) tool designed to automate repetitive tasks. It allows users to record mouse clicks, keystrokes, delays, and text searches on the screen. These sequences (macros) can be saved, loaded, and replayed multiple times. The application is built using Tkinter for the GUI and various third-party libraries to handle mouse and keyboard inputs, screen captures, and text recognition.

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

### Path Configuration

Please note that the script saves macros to a local JSON file (macros.json) and may also use specific paths for saving screenshots. Ensure that these paths are correctly configured in your environment:
    The script saves macros to a file named macros.json in the current working directory. Ensure this file is accessible and writable.
    For the text search functionality, screenshots are saved to a directory specified in the script (save_path). You may need to update this path according to your directory structure.

    
### Python Libraries
Install the required libraries by running the following pip commands:
```bash
pip install pyautogui
pip install mouse
pip install Pillow
pip install pytesseract
pip install opencv-python
pip install numpy
```
# Grabadora y Reproductor de Macros GUI

Este proyecto es una herramienta gráfica de interfaz de usuario (GUI) basada en Python, diseñada para automatizar tareas repetitivas. Permite a los usuarios grabar clics del ratón, pulsaciones de teclas, retrasos y búsquedas de texto en la pantalla. Estas secuencias (macros) pueden ser guardadas, cargadas y reproducidas múltiples veces. La aplicación está construida utilizando Tkinter para la GUI y varias bibliotecas de terceros para manejar entradas del ratón y el teclado, capturas de pantalla y reconocimiento de texto.

## Características

- **Grabar Clics del Ratón**: Captura tanto clics del ratón izquierdo como derecho, junto con sus coordenadas en la pantalla.
- **Grabar Pulsaciones de Teclas**: Graba entradas del teclado para su reproducción automática.
- **Aplicar Retrasos**: Añade retrasos entre acciones para una automatización más precisa.
- **Guardar y Cargar Macros**: Guarda macros grabadas en un archivo JSON y cárgalas para usarlas más tarde.
- **Reproducir Macros**: Repite macros múltiples veces con variaciones opcionales de retraso aleatorio.
- **Búsqueda de Texto en la Pantalla**: Busca texto especificado en un patrón en espiral en la pantalla, utilizando Reconocimiento Óptico de Caracteres (OCR) a través de Tesseract.
- **Gestionar Macros**: Ver, reproducir o eliminar macros guardadas a través de una interfaz intuitiva.

## Requisitos

Este proyecto requiere **Python 3.6** o superior.

### Bibliotecas de Python

Instala las bibliotecas requeridas ejecutando los siguientes comandos pip:

```bash
pip install pyautogui
pip install mouse
pip install Pillow
pip install pytesseract
pip install opencv-python
pip install numpy
