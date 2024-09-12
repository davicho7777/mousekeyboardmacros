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
