import tkinter as tk 
ventana =tk.Tk()
ventana.title("Menu de una tienda(Inventario)")
ventana.geometry("700x400")

mi_menu = tk.Menu(ventana)
mi_menu.add_command(label='Inicio')
mi_menu.add_command(label='Inventario')
mi_menu.add_command(label='Ventas')
mi_menu.add_command(label='Facturas')


ventana.config(menu=mi_menu)

ventana.mainloop()
