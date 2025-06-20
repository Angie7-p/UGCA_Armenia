import tkinter as tk
from tkinter import messagebox, simpledialog, ttk
import json
import os
from datetime import datetime

# Ruta del archivo para guardar los eventos
FILE = "eventos.json"

# Cargar eventos guardados
def cargar_eventos():
    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            return json.load(f)
    return []

# Guardar eventos en archivo
def guardar_eventos():
    with open(FILE, "w") as f:
        json.dump(eventos, f, indent=4)

# Agregar evento
def agregar_evento():
    fecha = simpledialog.askstring("Fecha", "Ingrese la fecha (YYYY-MM-DD):")
    hora = simpledialog.askstring("Hora", "Ingrese la hora (HH:MM):")
    desc = simpledialog.askstring("Descripción", "Descripción del evento:")

    if fecha and hora and desc:
        eventos.append({"fecha": fecha, "hora": hora, "descripcion": desc})
        eventos.sort(key=lambda e: (e["fecha"], e["hora"]))
        actualizar_tabla()
        guardar_eventos()
    else:
        messagebox.showwarning("Datos incompletos", "Todos los campos son obligatorios.")

# Eliminar evento seleccionado
def eliminar_evento():
    selected = tabla.selection()
    if selected:
        index = int(selected[0])
        eventos.pop(index)
        actualizar_tabla()
        guardar_eventos()
    else:
        messagebox.showinfo("Sin selección", "Seleccione un evento para eliminar.")

# Actualizar tabla visual
def actualizar_tabla():
    for row in tabla.get_children():
        tabla.delete(row)
    for i, evento in enumerate(eventos):
        tabla.insert("", "end", iid=i, values=(evento["fecha"], evento["hora"], evento["descripcion"]))

# Ventana principal
root = tk.Tk()
root.title("Agenda de Eventos - Universidad La Gran Colombia")
root.geometry("600x400")

# Logo (puedo ayudarte a añadirlo si me das la imagen)
# logo = tk.PhotoImage(file="logo_ucg.png")
# logo_label = tk.Label(root, image=logo)
# logo_label.pack(pady=5)

# Tabla de eventos
tabla = ttk.Treeview(root, columns=("Fecha", "Hora", "Descripción"), show="headings")
tabla.heading("Fecha", text="Fecha")
tabla.heading("Hora", text="Hora")
tabla.heading("Descripción", text="Descripción")
tabla.pack(fill="both", expand=True)

# Botones
frame_botones = tk.Frame(root)
frame_botones.pack(pady=10)

tk.Button(frame_botones, text="Agregar evento", command=agregar_evento).pack(side="left", padx=5)
tk.Button(frame_botones, text="Eliminar evento", command=eliminar_evento).pack(side="left", padx=5)

# Cargar datos
eventos = cargar_eventos()
actualizar_tabla()

# Ejecutar app
root.mainloop()
