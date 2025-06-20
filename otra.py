import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import csv
import os
from datetime import datetime

# Nombre del archivo CSV
ARCHIVO = "eventos.csv"

# Cargar eventos del archivo CSV
def cargar_eventos():
    eventos = []
    if os.path.exists(ARCHIVO):
        with open(ARCHIVO, newline='', encoding='utf-8') as f:
            reader = csv.reader(f)
            eventos = list(reader)
    return eventos

# Guardar eventos en archivo CSV
def guardar_eventos():
    with open(ARCHIVO, "w", newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        for evento in eventos:
            writer.writerow(evento)

# Agregar nuevo evento
def agregar_evento():
    fecha = simpledialog.askstring("Fecha", "Ingrese la fecha (YYYY-MM-DD):")
    hora = simpledialog.askstring("Hora", "Ingrese la hora (HH:MM):")
    descripcion = simpledialog.askstring("Descripción", "Ingrese la descripción del evento:")

    if fecha and hora and descripcion:
        try:
            datetime.strptime(fecha, "%Y-%m-%d")
            datetime.strptime(hora, "%H:%M")
            eventos.append([fecha, hora, descripcion])
            eventos.sort()
            actualizar_tabla()
            guardar_eventos()
        except ValueError:
            messagebox.showerror("Error", "Formato de fecha u hora inválido.")
    else:
        messagebox.showwarning("Atención", "Debe completar todos los campos.")

# Eliminar evento seleccionado
def eliminar_evento():
    seleccionado = tabla.selection()
    if seleccionado:
        index = int(seleccionado[0])
        eventos.pop(index)
        actualizar_tabla()
        guardar_eventos()
    else:
        messagebox.showinfo("Sin selección", "Seleccione un evento para eliminar.")

# Actualizar tabla visual
def actualizar_tabla():
    for item in tabla.get_children():
        tabla.delete(item)
    for i, (fecha, hora, descripcion) in enumerate(eventos):
        tabla.insert("", "end", iid=i, values=(fecha, hora, descripcion))

# Crear ventana principal
root = tk.Tk()
root.title("Agenda de Eventos - Universidad La Gran Colombia")
root.geometry("650x450")

# Logo (debe estar en formato PNG)
try:
    logo = tk.PhotoImage(file="logo.png")
    tk.Label(root, image=logo).pack(pady=10)
except:
    tk.Label(root, text="[Logo no disponible]", font=("Arial", 14)).pack()

# Tabla
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

# Datos iniciales
eventos = cargar_eventos()
actualizar_tabla()

# Ejecutar app
root.mainloop()
