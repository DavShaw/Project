import tkinter as tk
from tkinter import messagebox

def mostrar_mensaje():
    resultado = messagebox.askyesno("Mensaje", "¿Deseas volver a jugar?")
    if resultado:

        print("Volver a jugar")
        root.destroy()
    else:
        print("Salir")
        root.destroy()

root = tk.Tk()
root.withdraw()

ventana_mensaje = tk.Toplevel(root)

ventana_mensaje.geometry("300x100")

x = (root.winfo_screenwidth() - ventana_mensaje.winfo_reqwidth()) / 2
y = (root.winfo_screenheight() - ventana_mensaje.winfo_reqheight()) / 2
ventana_mensaje.geometry("+%d+%d" % (x, y))

ventana_mensaje.resizable(False, False)

boton_volver_a_jugar = tk.Button(ventana_mensaje, text="Volver a jugar", command=mostrar_mensaje)
boton_volver_a_jugar.pack(padx=10, pady=20, side="left")

boton_salir = tk.Button(ventana_mensaje, text="Salir", command=mostrar_mensaje)
boton_salir.pack(padx=10, pady=20, side="right")

root.mainloop()
