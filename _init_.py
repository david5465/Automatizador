import tkinter as tk
from tkinter import messagebox
import subprocess
import time
import signal
import sys
import pyautogui

script_en_ejecucion = False
proceso_script = None
d1=time.sleep(0.1)
d10=time.sleep(1)

def ejecutar_script(script):
    global script_en_ejecucion, proceso_script
    if not script_en_ejecucion:
        script_en_ejecucion = True
        proceso_script = subprocess.Popen(["python", script])
        actualizar_estado("Ejecutando script: " + script)
        proceso_script.wait()  
        script_en_ejecucion = False
        proceso_script = None
        actualizar_estado("Listo para ejecutar")
    else:
        messagebox.showinfo("Advertencia", "Ya hay un script en ejecución.")

def detener_script():
    global script_en_ejecucion, proceso_script
    if script_en_ejecucion:
        proceso_script.terminate()  
        script_en_ejecucion = False
        proceso_script = None
        actualizar_estado("Script detenido")
    else:
        messagebox.showinfo("Advertencia", "No hay ningún script en ejecución.")

def actualizar_estado(texto):
    estado_label.config(text="Estado: " + texto)

# Crear la ventana principal
root = tk.Tk()
root.title("Ejecutar Scripts")
root.geometry("200x300")
font = ('Arial', 10, 'bold')

# Etiqueta para mostrar el estado de ejecución del script
estado_label = tk.Label(root, text="Estado: Listo para ejecutar")
estado_label.pack()

# Funciones de ejecución de los scripts
def ejecutar_script_1():
    pyautogui.click(1000,50)
    pyautogui.hotkey('ctrl', 'alt', 'z')
    pyautogui.hotkey('ctrl', 'alt', 'r')

def ejecutar_script_2():
    pyautogui.click(pyautogui.locateOnScreen('botonmas.png', confidence=0.8))
    pyautogui.sleep(2)
    pyautogui.write('consult')
    pyautogui.sleep(0.5)
    pyautogui.press('enter')
    pyautogui.sleep(0.5)
    pyautogui.press('tab')
    pyautogui.sleep(0.5)
    pyautogui.write('canales')
    pyautogui.sleep(0.5)
    pyautogui.press('enter')
    pyautogui.sleep(0.5)
    pyautogui.press('tab')
    pyautogui.sleep(0.5)
    pyautogui.write('vicio')
    pyautogui.sleep(0.5)
    pyautogui.press('tab')
    pyautogui.sleep(1)
    pyautogui.press('tab')
    pyautogui.sleep(0.5)
    pyautogui.hotkey('ctrl','v')
    pyautogui.sleep(0.5)
    pyautogui.press('tab')
    pyautogui.sleep(0.5)
    pyautogui.press('tab')
    pyautogui.sleep(0.5)
    pyautogui.press('tab')
    pyautogui.sleep(0.5)
    pyautogui.write('llamada vicio')
    pyautogui.hotkey('ctrl','s')
    pyautogui.sleep(2)
    pyautogui.click(pyautogui.locateOnScreen('133.png', confidence=0.8))
    

def ejecutar_script_3():
    pyautogui.click(pyautogui.locateOnScreen('botonmas.png', confidence=0.8))
    pyautogui.sleep(2)
    pyautogui.write('problem')
    pyautogui.sleep(0.5)
    pyautogui.press('enter')
    pyautogui.sleep(0.5)
    pyautogui.press('tab')
    pyautogui.sleep(0.5)
    pyautogui.write('factur')
    pyautogui.sleep(0.5)
    pyautogui.press('enter')
    pyautogui.sleep(0.5)
    pyautogui.press('tab')
    pyautogui.sleep(0.5)
    pyautogui.write('no re')
    pyautogui.sleep(0.5)
    pyautogui.press('tab')
    pyautogui.sleep(1)
    pyautogui.press('tab')
    pyautogui.sleep(0.5)
    pyautogui.hotkey('ctrl','v')
    pyautogui.sleep(0.5)
    pyautogui.press('tab')
    pyautogui.sleep(0.5)
    pyautogui.press('tab')
    pyautogui.sleep(0.5)
    pyautogui.press('tab')
    pyautogui.sleep(0.5)
    pyautogui.write('cc')
    pyautogui.hotkey('ctrl','s')
    pyautogui.sleep(2)
    pyautogui.click(pyautogui.locateOnScreen('133.png', confidence=0.8))

def ejecutar_script_4():
    pyautogui.click(pyautogui.locateOnScreen('botonmas.png', confidence=0.8))
    pyautogui.sleep(2)
    pyautogui.write('consult')
    pyautogui.sleep(0.5)
    pyautogui.press('enter')
    pyautogui.sleep(0.5)
    pyautogui.press('tab')
    pyautogui.sleep(0.5)
    pyautogui.write('canales')
    pyautogui.sleep(0.5)
    pyautogui.press('enter')
    pyautogui.sleep(0.5)
    pyautogui.press('tab')
    pyautogui.sleep(0.5)
    pyautogui.write('corta')
    pyautogui.sleep(0.5)
    pyautogui.press('tab')
    pyautogui.sleep(1)
    pyautogui.press('tab')
    pyautogui.sleep(0.5)
    pyautogui.hotkey('ctrl','v')
    pyautogui.sleep(0.5)
    pyautogui.press('tab')
    pyautogui.sleep(0.5)
    pyautogui.press('tab')
    pyautogui.sleep(0.5)
    pyautogui.press('tab')
    pyautogui.sleep(0.5)
    pyautogui.write('cl corta llamada')
    pyautogui.hotkey('ctrl','s')
    pyautogui.sleep(2)
    pyautogui.click(pyautogui.locateOnScreen('133.png', confidence=0.8))

def ejecutar_script_5():

    pyautogui.click(pyautogui.locateOnScreen('botonmas.png', confidence=0.8))
    pyautogui.sleep(1.5)
    pyautogui.write('consult')
    pyautogui.sleep(0.5)
    pyautogui.press('enter')
    pyautogui.sleep(0.5)
    pyautogui.press('tab')
    pyautogui.sleep(0.5)
    pyautogui.write('consum')
    pyautogui.sleep(0.5)
    pyautogui.press('enter')
    pyautogui.sleep(1)
    pyautogui.press('tab')
    pyautogui.sleep(0.5)
    pyautogui.write('plan')
    pyautogui.sleep(0.5)
    pyautogui.press('tab')
    pyautogui.sleep(1)
    pyautogui.press('tab')
    pyautogui.sleep(0.5)
    pyautogui.hotkey('ctrl','v')
    pyautogui.sleep(0.5)
    pyautogui.press('tab')
    pyautogui.sleep(0.5)
    pyautogui.press('tab')
    pyautogui.sleep(0.5)
    pyautogui.press('tab')
    pyautogui.sleep(0.5)
    pyautogui.write('vv')
    pyautogui.hotkey('ctrl','s')
    pyautogui.sleep(2)
    pyautogui.click(pyautogui.locateOnScreen('133.png', confidence=0.8))

def ejecutar_script_6():
    pyautogui.click(pyautogui.locateOnScreen('botonmas.png', confidence=0.8))
    pyautogui.sleep(2)
    pyautogui.write('consult')
    pyautogui.sleep(0.5)
    pyautogui.press('enter')
    pyautogui.sleep(0.5)
    pyautogui.press('tab')
    pyautogui.sleep(0.5)
    pyautogui.write('canales')
    pyautogui.sleep(0.5)
    pyautogui.press('enter')
    pyautogui.sleep(0.5)
    pyautogui.press('tab')
    pyautogui.sleep(0.5)
    pyautogui.write('deriva')
    pyautogui.sleep(0.5)
    pyautogui.press('tab')
    pyautogui.sleep(1)
    pyautogui.press('tab')
    pyautogui.sleep(0.5)
    pyautogui.hotkey('ctrl','v')
    pyautogui.sleep(0.5)
    pyautogui.press('tab')
    pyautogui.sleep(0.5)
    pyautogui.press('tab')
    pyautogui.sleep(0.5)
    pyautogui.press('tab')
    pyautogui.sleep(0.5)
    pyautogui.write('se deriva')
    pyautogui.hotkey('ctrl','s')
    pyautogui.sleep(2)
    pyautogui.click(pyautogui.locateOnScreen('133.png', confidence=0.8))

def ejecutar_script_7():    
    
    pyautogui.click(pyautogui.locateOnScreen('ea.png', confidence=0.8))
    pyautogui.sleep(2)
    pyautogui.press('up')
    pyautogui.press('enter')
    pyautogui.click(pyautogui.locateOnScreen('er.png', confidence=0.8))
    pyautogui.sleep(2)
    pyautogui.press('down')
    pyautogui.press('enter')
    pyautogui.hotkey('ctrl','s')
    
def ejecutar_script_8(): 
    pyautogui.hotkey('alt','tab')
    pyautogui.sleep(0.5)
    pyautogui.hotkey('ctrl','v')

def ejecutar_script_9(): 
    pyautogui.hotkey('alt','tab')
    pyautogui.sleep(0.5)
    pyautogui.hotkey('ctrl','c')

# Crear botones para ejecutar los scripts
button_script_1 = tk.Button(root, text="Reset", width=5, height=1, command=ejecutar_script_1)
button_script_1.pack()

button_script_2 = tk.Button(root, text="Vicio", width=5, height=1, command=ejecutar_script_2)
button_script_2.pack()

button_script_3 = tk.Button(root, text="Factu", width=5, height=1, command=ejecutar_script_3)
button_script_3.pack()

button_script_4 = tk.Button(root, text="Corta", width=5, height=1, command=ejecutar_script_4)
button_script_4.pack()

button_script_5 = tk.Button(root, text="Info", width=5, height=1, command=ejecutar_script_5)
button_script_5.pack()

button_script_6 = tk.Button(root, text="Deriv", width=5, height=1, command=ejecutar_script_6)
button_script_6.pack()

button_script_7 = tk.Button(root, text="cerrarss", width=5, height=1, command=ejecutar_script_7)
button_script_7.pack()

button_script_8 = tk.Button(root, text="ctrl V", width=5, height=1, command=ejecutar_script_8)
button_script_8.pack()

button_script_9 = tk.Button(root, text="ctrl C", width=5, height=1, command=ejecutar_script_9)
button_script_9.pack()

# Botón para detener el script
button_detener = tk.Button(root, text='Stop', font=font, fg="white", bg="red", width=4, height=1, command=detener_script)
button_detener.pack()

# Ejecutar el bucle principal de la ventana
root.mainloop()