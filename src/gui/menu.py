import sys
sys.path.append("src")

import tkinter as tk
import tkinter.font as tkFont
import juego as game




class App:
    def __init__(self, root):

        bg_color = "#F59682"

        #setting title
        root.title("Menú principal")

        root.config(bg = bg_color)

        #setting window size
        width=255
        height=372
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GButton_697=tk.Button(root)
        GButton_697["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_697["font"] = ft
        GButton_697["fg"] = "#000000"
        GButton_697["justify"] = "center"
        GButton_697["text"] = "Jugar"
        GButton_697.place(x=70,y=60,width=124,height=33)
        GButton_697["command"] = self.GButton_697_command
        GButton_697.configure(bg="#FFE1CD")

        GButton_480=tk.Button(root)
        GButton_480["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_480["font"] = ft
        GButton_480["fg"] = "#000000"
        GButton_480["justify"] = "center"
        GButton_480["text"] = "Opciones"
        GButton_480.place(x=70,y=130,width=125,height=30)
        GButton_480["command"] = self.GButton_480_command
        GButton_480.configure(bg="#FFE1CD")

        GButton_120=tk.Button(root)
        GButton_120["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_120["font"] = ft
        GButton_120["fg"] = "#000000"
        GButton_120["justify"] = "center"
        GButton_120["text"] = "Salir"
        GButton_120.place(x=70,y=200,width=123,height=30)
        GButton_120["command"] = self.GButton_120_command
        GButton_120.configure(bg="#FFE1CD")

        GLabel_194=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_194["font"] = ft
        GLabel_194["fg"] = "#333333"
        GLabel_194["justify"] = "center"
        GLabel_194["text"] = "By: David Carrillo Torres"
        GLabel_194.place(x=0,y=340,width=153,height=30)
        GLabel_194.config(bg = bg_color)

    def GButton_697_command(self):
        print("Boton: Jugar")
        root.destroy()
        game.jugar()


    def GButton_480_command(self):
        from opciones import run as optionrunner
        root.destroy()
        optionrunner()

    def GButton_120_command(self):
        print("Boton: Salir")
        root.destroy()

def run():
    global root
    root = tk.Tk()
    App(root)
    root.mainloop()

if __name__ == "__main__":
    run()