import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import sqlite3
from PIL import Image, ImageTk
from datetime import datetime

# Conexión a SQLite
conn = sqlite3.connect("eventos.db")
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS eventos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    fecha TEXT,
    hora TEXT,
    descripcion TEXT
)
""")
conn.commit()

# Función para insertar evento
def agregar_evento():
    fecha = simpledialog.askstring("Fecha", "Ingrese la fecha (YYYY-MM-DD):")
    hora = simpledialog.askstring("Hora", "Ingrese la hora (HH:MM):")
    desc = simpledialog.askstring("Descripción", "Descripción del evento:")

    if fecha and hora and desc:
        try:
            datetime.strptime(fecha, "%Y-%m-%d")
            datetime.strptime(hora, "%H:%M")
            cursor.execute("INSERT INTO eventos (fecha, hora, descripcion) VALUES (?, ?, ?)",
                           (fecha, hora, desc))
            conn.commit()
            actualizar_tabla()
        except ValueError:
            messagebox.showerror("Formato inválido", "Formato de fecha u hora incorrecto.")
    else:
        messagebox.showwarning("Datos faltantes", "Todos los campos son requeridos.")

# Eliminar evento seleccionado
def eliminar_evento():
    seleccionado = tabla.focus()
    if seleccionado:
        evento_id = tabla.item(seleccionado)["values"][0]
        cursor.execute("DELETE FROM eventos WHERE id=?", (evento_id,))
        conn.commit()
        actualizar_tabla()
    else:
        messagebox.showinfo("Selecciona", "Debes seleccionar un evento para eliminar.")

# Cargar eventos a la tabla
def actualizar_tabla():
    for row in tabla.get_children():
        tabla.delete(row)
    cursor.execute("SELECT * FROM eventos ORDER BY fecha, hora")
    for fila in cursor.fetchall():
        tabla.insert("", "end", values=fila)

# GUI principal
root = tk.Tk()
root.title("Agenda UGC con Base de Datos")
root.geometry("700x500")

# Logo
try:
    img = Image.open("logo.png")
    img = img.resize((300, 100), Image.ANTIALIAS)
    logo_img = ImageTk.PhotoImage(img)
    logo_label = tk.Label(root, image=logo_img)
    logo_label.pack(pady=5)
except:
    logo_label = tk.Label(root, text="Universidad La Gran Colombia", font=("Arial", 16))
    logo_label.pack(pady=5)

# Tabla de eventos
tabla = ttk.Treeview(root, columns=("ID", "Fecha", "Hora", "Descripción"), show="headings")
tabla.heading("ID", text="ID")
tabla.heading("Fecha", text="Fecha")
tabla.heading("Hora", text="Hora")
tabla.heading("Descripción", text="Descripción")
tabla.pack(fill="both", expand=True)

# Botones
frame = tk.Frame(root)
frame.pack(pady=10)
tk.Button(frame, text="Agregar Evento", command=agregar_evento).pack(side="left", padx=10)
tk.Button(frame, text="Eliminar Evento", command=eliminar_evento).pack(side="left", padx=10)

actualizar_tabla()
root.mainloop()
