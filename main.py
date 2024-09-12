import tkinter as tk
import mouse
import threading
import time
import json
import pyautogui
import random
from tkinter import simpledialog, messagebox
from PIL import Image, ImageGrab
import pytesseract
import cv2
import numpy as np
import os
import math

# Variables globales para grabar la macro
macro_recording = False
macro_steps = []
macro_storage = {}

def load_macros():
    global macro_storage
    try:
        with open("macros.json", "r") as file:
            macro_storage = json.load(file)
    except FileNotFoundError:
        macro_storage = {}
    except json.JSONDecodeError:
        macro_storage = {}

def save_macros():
    with open("macros.json", "w") as file:
        json.dump(macro_storage, file)

def on_button_click():
    if not button.clicked:
        button.config(bg="yellow")
        button.clicked = True
        print("Botón presionado. Esperando el clic...")
        threading.Thread(target=wait_for_click).start()
    else:
        print("Por favor, espera al siguiente clic.")

def wait_for_click():
    button_type = None
    
    while button_type is None:
        if mouse.is_pressed(button="left"):
            x, y = mouse.get_position()
            update_gui(x, y)
            print(f"Coordenadas del clic izquierdo: ({x}, {y})")
            button_type = 'left'
        elif mouse.is_pressed(button="right"):
            x, y = mouse.get_position()
            update_gui(x, y)
            print(f"Coordenadas del clic derecho: ({x}, {y})")
            button_type = 'right'
        time.sleep(0.1)
    
    button.config(bg="SystemButtonFace")
    button.clicked = False
    record_step('click', button_type, x, y)

def on_key_button_click():
    key_button.config(bg="yellow")
    key_button.clicked = True
    print("Botón de teclado presionado. Esperando la tecla...")
    root.bind('<KeyPress>', record_key)

def record_key(event):
    key = event.keysym
    update_key(key)
    print(f"Tecla presionada: {key}")
    key_button.config(bg="SystemButtonFace")
    key_button.clicked = False
    root.unbind('<KeyPress>')
    record_step('key', key)

def on_delay_button_click():
    delay_button.config(bg="yellow")
    delay_button.clicked = True
    delay_entry.config(state=tk.NORMAL)
    delay_entry.focus_set()

def apply_delay():
    try:
        delay = float(delay_entry.get())
        print(f"Aplicando un retraso de {delay} segundos...")
        update_delay_display(delay)
        record_step('delay', delay)  # Guarda solo el valor base sin variación
    except ValueError:
        print("Por favor, ingresa un número válido.")
    delay_entry.delete(0, tk.END)
    delay_button.config(bg="SystemButtonFace")
    delay_button.clicked = False
    delay_entry.config(state=tk.DISABLED)

def update_gui(x, y):
    coords_label.config(text=f"Coordenadas: ({x}, {y})")

def update_key(key):
    key_label.config(text=f"Tecla: {key}")

def update_delay_display(delay):
    delay_label.config(text=f"Último Retraso Aplicado: {delay} segundos")

def record_step(action_type, *args):
    if macro_recording:
        macro_steps.append((action_type, *args))
        display_step(action_type, *args)

def display_step(action_type, *args):
    if action_type == 'click':
        button_type, x, y = args
        step_text = f"Clic {button_type} en ({x}, {y})"
    elif action_type == 'key':
        key = args[0]
        step_text = f"Tecla presionada: {key}"
    elif action_type == 'delay':
        delay = args[0]
        step_text = f"Retraso de {delay} segundos"
    elif action_type == 'search_text':
        text_to_find, steps = args
        step_text = f"Buscar texto '{text_to_find}' en {steps} pasos"
    else:
        step_text = "Acción desconocida"

    macro_text.config(state=tk.NORMAL)
    macro_text.insert(tk.END, step_text + "\n", "blue")
    macro_text.see(tk.END)
    macro_text.config(state=tk.DISABLED)


def start_stop_macro():
    global macro_recording
    if not macro_recording:
        macro_steps.clear()
        macro_button.config(bg="yellow")
        macro_button.config(text="Detener Macro")
        macro_recording = True
        print("Inicio de grabación de macro.")
        macro_text.config(state=tk.NORMAL)
        macro_text.delete(1.0, tk.END)
        macro_text.insert(tk.END, "Inicio de grabación de macro\n", "blue")
        macro_text.config(state=tk.DISABLED)
    else:
        macro_button.config(bg="SystemButtonFace")
        macro_button.config(text="Grabar Macro")
        macro_recording = False
        print("Detención de grabación de macro.")
        macro_text.config(state=tk.NORMAL)
        macro_text.insert(tk.END, "Fin de grabación de macro\n", "blue")
        macro_text.config(state=tk.DISABLED)
        save_macro()

def save_macro():
    name = simpledialog.askstring("Guardar Macro", "Ingresa un nombre para la macro (deja en blanco para no guardar):")
    if name:
        macro_storage[name] = list(macro_steps)
        save_macros()
        print(f"Macro guardada como '{name}'.")
        messagebox.showinfo("Guardar Macro", f"Macro guardada como '{name}'.")
    else:
        print("No se ha guardado la macro.")
        messagebox.showinfo("Guardar Macro", "No se ha guardado la macro.")

def get_repeat_count():
    while True:
        try:
            repeat_count = simpledialog.askinteger("Repeticiones", "¿Cuántas veces quieres repetir la macro?", minvalue=1)
            if repeat_count is not None:
                return repeat_count
        except ValueError:
            print("Por favor, ingresa un número válido.")

def play_macro(name):
    if name in macro_storage:
        macro_steps = macro_storage[name]
        repeat_count = get_repeat_count()
        if repeat_count is None:
            return
        print(f"Reproduciendo macro '{name}' {repeat_count} veces...")
        macro_text.config(state=tk.NORMAL)
        macro_text.insert(tk.END, f"Reproduciendo macro '{name}' {repeat_count} veces:\n", "blue")
        macro_text.config(state=tk.DISABLED)
        for _ in range(repeat_count):
            for step in macro_steps:
                action_type = step[0]
                if action_type == 'click':
                    button_type, x, y = step[1], step[2], step[3]
                    print(f"Reproduciendo clic {button_type} en ({x}, {y})")
                    display_step('click', button_type, x, y)
                    update_gui(x, y)
                    if button_type == 'left':
                        pyautogui.click(x, y)
                    elif button_type == 'right':
                        pyautogui.click(x, y, button='right')
                elif action_type == 'key':
                    key = step[1]
                    print(f"Reproduciendo tecla: {key}")
                    display_step('key', key)
                    update_key(key)
                    pyautogui.press(key)
                elif action_type == 'delay':
                    delay = step[1]
                    variation = random.uniform(-0.3, 0.6)
                    adjusted_delay = delay + variation
                    print(f"Reproduciendo retraso de {adjusted_delay} segundos (original: {delay} segundos, variación: {variation} segundos)")
                    display_step('delay', delay)
                    update_delay_display(delay)
                    time.sleep(adjusted_delay)
                elif action_type == 'search_text':
                    text_to_find, steps = step[1], step[2]
                    print(f"Buscando el texto '{text_to_find}' con {steps} pasos en espiral.")
                    spiral_search(text_to_find, steps)
                root.update()
        macro_text.config(state=tk.NORMAL)
        macro_text.insert(tk.END, "Reproducción de macro finalizada\n", "blue")
        macro_text.see(tk.END)
        macro_text.config(state=tk.DISABLED)
    else:
        messagebox.showerror("Error", f"No se encontró la macro '{name}'.")


def show_macros():
    def play_selected_macro():
        selected_macro = macro_listbox.get(tk.ACTIVE)
        if selected_macro:
            play_macro(selected_macro)

    def delete_selected_macro():
        selected_macro = macro_listbox.get(tk.ACTIVE)
        if selected_macro:
            del macro_storage[selected_macro]
            save_macros()
            update_macro_list()
            print(f"Macro '{selected_macro}' eliminada.")
            messagebox.showinfo("Eliminar Macro", f"Macro '{selected_macro}' eliminada.")
    
    def update_macro_list():
        macro_listbox.delete(0, tk.END)
        for name in macro_storage.keys():
            macro_listbox.insert(tk.END, name)

    macro_window = tk.Toplevel(root)
    macro_window.title("Macros Guardadas")
    macro_window.geometry("300x400")

    tk.Label(macro_window, text="Macros guardadas:").pack(pady=10)

    macro_listbox = tk.Listbox(macro_window)
    macro_listbox.pack(pady=10, fill=tk.BOTH, expand=True)

    update_macro_list()

    tk.Button(macro_window, text="Reproducir", command=play_selected_macro).pack(pady=5)
    tk.Button(macro_window, text="Eliminar", command=delete_selected_macro).pack(pady=5)
    tk.Button(macro_window, text="Cerrar", command=macro_window.destroy).pack(pady=5)

def spiral_search(text_to_find, steps):
    save_path = r"C:\python"
    os.makedirs(save_path, exist_ok=True)
    
    screen_width, screen_height = pyautogui.size()
    center_x, center_y = screen_width // 2, screen_height // 2
    
    def spiral_move(steps, step_size, pause_time):
        for i in range(steps):
            angle = i * 0.5 * math.pi
            dx = int(math.cos(angle) * step_size * (i + 1))
            dy = int(math.sin(angle) * step_size * (i + 1))
            new_x, new_y = center_x + dx, center_y + dy
            
            print(f"\nPaso {i+1}:")
            print(f"Moviendo el mouse a ({new_x}, {new_y})")
            pyautogui.moveTo(new_x, new_y)
            time.sleep(pause_time)
            
            screenshot = ImageGrab.grab(bbox=(new_x - 80, new_y + 30, new_x + 80, new_y + 60))
            screenshot_path = os.path.join(save_path, f"captura_{i+1}.png")
            screenshot.save(screenshot_path)
            print(f"Imagen guardada como: {screenshot_path}")
            
            time.sleep(pause_time)
            
            img_np = np.array(screenshot)
            gray = cv2.cvtColor(img_np, cv2.COLOR_BGR2GRAY)
            text = pytesseract.image_to_string(gray)
            
            print(f"Texto reconocido: {text.strip()}")
            
            if text_to_find.lower() in text.lower():
                print(f"'{text_to_find}' encontrado! Haciendo clic...")
                mouse.click()
                return True
            
            time.sleep(pause_time)
        
        return False
    
    print("Iniciando movimiento en espiral...")
    found = spiral_move(steps=steps, step_size=15, pause_time=2)
    if not found:
        print(f"\nNo se encontró '{text_to_find}' en ninguno de los pasos.")
    return found

def on_search_button_click():
    text_to_find = simpledialog.askstring("Buscar Texto", "Ingresa el texto a buscar:")
    if text_to_find:
        steps = simpledialog.askinteger("Número de pasos", "¿Cuántos pasos quieres que tenga la búsqueda en espiral?", minvalue=1)
        if steps:
            # Si la macro está grabando, registra el paso de búsqueda
            if macro_recording:
                record_step('search_text', text_to_find, steps)
                
            # Ejecuta la búsqueda en un hilo separado
            threading.Thread(target=lambda: spiral_search(text_to_find, steps)).start()



# Configuración de la ventana principal
root = tk.Tk()
root.title("Registro de Clics, Teclas, Retrasos y Macros")
root.geometry("400x600")

# Cargar macros guardadas
load_macros()

# Botón para registrar clics
button = tk.Button(root, text="Presionar Clic", command=on_button_click)
button.pack(pady=10)
button.clicked = False

# Botón para registrar teclas
key_button = tk.Button(root, text="Registrar Tecla", command=on_key_button_click)
key_button.pack(pady=10)
key_button.clicked = False

# Botón para aplicar retraso
delay_button = tk.Button(root, text="Aplicar Retraso", command=on_delay_button_click)
delay_button.pack(pady=10)
delay_button.clicked = False

# Campo de entrada para el retraso
delay_entry = tk.Entry(root)
delay_entry.pack(pady=10)
delay_entry.config(state=tk.DISABLED)

# Botón para aplicar el retraso ingresado
apply_delay_button = tk.Button(root, text="Aplicar Retraso Ingresado", command=apply_delay)
apply_delay_button.pack(pady=10)

# Botón para grabar macro
macro_button = tk.Button(root, text="Grabar Macro", command=start_stop_macro)
macro_button.pack(pady=10)

# Botón para reproducir macro
play_button = tk.Button(root, text="Play", command=lambda: play_macro(simpledialog.askstring("Seleccionar Macro", "Ingresa el nombre de la macro a reproducir:")))
play_button.pack(pady=10)

# Botón para ver macros guardadas
view_macros_button = tk.Button(root, text="Ver Macros", command=show_macros)
view_macros_button.pack(pady=10)

# Botón para buscar texto en pantalla
search_button = tk.Button(root, text="Buscar Texto en Pantalla", command=on_search_button_click)
search_button.pack(pady=10)

# Etiqueta para mostrar las coordenadas
coords_label = tk.Label(root, text="Coordenadas: (--, --)")
coords_label.pack()

# Etiqueta para mostrar la tecla presionada
key_label = tk.Label(root, text="Tecla: --")
key_label.pack()

# Etiqueta para mostrar el último retraso aplicado
delay_label = tk.Label(root, text="Último Retraso Aplicado: -- segundos")
delay_label.pack()

# Área de texto para mostrar los pasos de la macro
macro_text = tk.Text(root, height=10, width=50, wrap=tk.WORD, bg="light gray")
macro_text.tag_configure("blue", foreground="blue")
macro_text.pack(pady=10)
macro_text.config(state=tk.DISABLED)

root.mainloop()
