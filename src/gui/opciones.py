import json
import os
import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, root):
        # Datos para mostrar en el Entry
        self.datos = self.cargar_json("database")
        self.root = root

        #setting title
        self.root.title("undefined")
        #setting window size
        self.width=395
        self.height=736
        self.screenwidth = root.winfo_screenwidth()
        self.screenheight = root.winfo_screenheight()
        self.alignstr = '%dx%d+%d+%d' % (self.width, self.height, (self.screenwidth - self.width) / 2, (self.screenheight - self.height) / 2)
        self.root.geometry(self.alignstr)
        self.root.resizable(width=False, height=False)

        self.GLineEdit_209=tk.Entry(root)
        self.GLineEdit_209["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        self.GLineEdit_209["font"] = ft
        self.GLineEdit_209["fg"] = "#333333"
        self.GLineEdit_209["justify"] = "center"
        self.GLineEdit_209.insert(0, self.datos["pantalla_tamano"][0])
        self.GLineEdit_209.place(x=250,y=30,width=70,height=25)

        self.GLineEdit_889=tk.Entry(root)
        self.GLineEdit_889["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        self.GLineEdit_889["font"] = ft
        self.GLineEdit_889["fg"] = "#333333"
        self.GLineEdit_889["justify"] = "center"
        self.GLineEdit_889.insert(0, self.datos["pantalla_tamano"][1])
        self.GLineEdit_889.place(x=250,y=80,width=70,height=25)

        self.GLineEdit_24=tk.Entry(root)
        self.GLineEdit_24["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        self.GLineEdit_24["font"] = ft
        self.GLineEdit_24["fg"] = "#333333"
        self.GLineEdit_24["justify"] = "center"
        self.GLineEdit_24.insert(0, self.datos["velocidad_enemigo"])
        self.GLineEdit_24.place(x=250,y=120,width=70,height=25)

        self.GLineEdit_97=tk.Entry(root)
        self.GLineEdit_97["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        self.GLineEdit_97["justify"] = "center"
        self.GLineEdit_97["fg"] = "#333333"
        self.GLineEdit_97["font"] = ft
        self.GLineEdit_97.insert(0, self.datos["velocidad_jugador"])
        self.GLineEdit_97.place(x=250,y=170,width=70,height=25)

        self.GLineEdit_665=tk.Entry(root)
        self.GLineEdit_665["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        self.GLineEdit_665["font"] = ft
        self.GLineEdit_665["fg"] = "#333333"
        self.GLineEdit_665["justify"] = "center"
        self.GLineEdit_665.insert(0, self.datos["radio_enemigo"])
        self.GLineEdit_665.place(x=250,y=220,width=70,height=25)

        self.GLabel_681=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        self.GLabel_681["font"] = ft
        self.GLabel_681["fg"] = "#333333"
        self.GLabel_681["justify"] = "center"
        self.GLabel_681["text"] = "Pantalla (Ancho)"
        self.GLabel_681.place(x=70,y=30,width=102,height=30)

        self.GLabel_202=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        self.GLabel_202["font"] = ft
        self.GLabel_202["fg"] = "#333333"
        self.GLabel_202["justify"] = "center"
        self.GLabel_202["text"] = "Pantalla (Alto)"
        self.GLabel_202.place(x=70,y=80,width=84,height=30)

        self.GLabel_666=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        self.GLabel_666["font"] = ft
        self.GLabel_666["fg"] = "#333333"
        self.GLabel_666["justify"] = "center"
        self.GLabel_666["text"] = "Velocidad (Enemigo)"
        self.GLabel_666.place(x=80,y=120,width=114,height=30)

        self.GLabel_297=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        self.GLabel_297["font"] = ft
        self.GLabel_297["fg"] = "#333333"
        self.GLabel_297["justify"] = "center"
        self.GLabel_297["text"] = "Velocidad (Heroe)"
        self.GLabel_297.place(x=70,y=170,width=113,height=30)

        self.GLabel_144=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        self.GLabel_144["font"] = ft
        self.GLabel_144["fg"] = "#333333"
        self.GLabel_144["justify"] = "center"
        self.GLabel_144["text"] = "Radio (Enemigo)"
        self.GLabel_144.place(x=70,y=220,width=100,height=30)

        self.GLineEdit_200=tk.Entry(root)
        self.GLineEdit_200["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        self.GLineEdit_200["font"] = ft
        self.GLineEdit_200["fg"] = "#333333"
        self.GLineEdit_200["justify"] = "center"
        self.GLineEdit_200.insert(0, self.datos["radio_jugador"])
        self.GLineEdit_200.place(x=250,y=270,width=70,height=25)

        self.GLabel_761=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        self.GLabel_761["font"] = ft
        self.GLabel_761["fg"] = "#333333"
        self.GLabel_761["justify"] = "center"
        self.GLabel_761["text"] = "Radio (Heroe)"
        self.GLabel_761.place(x=70,y=270,width=88,height=30)

        self.GLineEdit_385=tk.Entry(root)
        self.GLineEdit_385["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        self.GLineEdit_385["font"] = ft
        self.GLineEdit_385["fg"] = "#333333"
        self.GLineEdit_385["justify"] = "center"
        self.GLineEdit_385.insert(0, self.datos["cantidad_enemigos"])
        self.GLineEdit_385.place(x=250,y=320,width=70,height=25)

        self.GLabel_609=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        self.GLabel_609["font"] = ft
        self.GLabel_609["fg"] = "#333333"
        self.GLabel_609["justify"] = "center"
        self.GLabel_609["text"] = "Cantidad (Enemigos)"
        self.GLabel_609.place(x=70,y=320,width=122,height=30)

        self.GLabel_474=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        self.GLabel_474["font"] = ft
        self.GLabel_474["fg"] = "#333333"
        self.GLabel_474["justify"] = "center"
        self.GLabel_474["text"] = "Multiplicador (Puntos)"
        self.GLabel_474.place(x=70,y=370,width=132,height=30)

        self.GLineEdit_513=tk.Entry(root)
        self.GLineEdit_513["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        self.GLineEdit_513["font"] = ft
        self.GLineEdit_513["fg"] = "#333333"
        self.GLineEdit_513["justify"] = "center"
        self.GLineEdit_513.insert(0, self.datos["multiplicador_puntos"])
        self.GLineEdit_513.place(x=250,y=370,width=70,height=25)

        self.GLabel_994=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        self.GLabel_994["font"] = ft
        self.GLabel_994["fg"] = "#333333"
        self.GLabel_994["justify"] = "center"
        self.GLabel_994["text"] = "Ticks (Puntos)"
        self.GLabel_994.place(x=60,y=420,width=109,height=30)

        self.GLineEdit_953=tk.Entry(root)
        self.GLineEdit_953["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        self.GLineEdit_953["font"] = ft
        self.GLineEdit_953["fg"] = "#333333"
        self.GLineEdit_953["justify"] = "center"
        self.GLineEdit_953.insert(0, self.datos["ticks_puntos"])
        self.GLineEdit_953.place(x=250,y=420,width=70,height=25)

        self.GLabel_369=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        self.GLabel_369["font"] = ft
        self.GLabel_369["fg"] = "#333333"
        self.GLabel_369["justify"] = "center"
        self.GLabel_369["text"] = "Int. aument. Vel. (Enemigo)"
        self.GLabel_369.place(x=80,y=470,width=150,height=30)

        self.GLineEdit_249=tk.Entry(root)
        self.GLineEdit_249["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        self.GLineEdit_249["font"] = ft
        self.GLineEdit_249["fg"] = "#333333"
        self.GLineEdit_249["justify"] = "center"
        self.GLineEdit_249.insert(0, self.datos["velocidad_enemigo_incrementar_en_intervalo"])
        self.GLineEdit_249.place(x=250,y=470,width=70,height=25)

        self.GLabel_305=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        self.GLabel_305["font"] = ft
        self.GLabel_305["fg"] = "#333333"
        self.GLabel_305["justify"] = "center"
        self.GLabel_305["text"] = "Aument. Vel. (Enemigo)"
        self.GLabel_305.place(x=80,y=530,width=132,height=30)

        self.GLineEdit_313=tk.Entry(root)
        self.GLineEdit_313["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        self.GLineEdit_313["font"] = ft
        self.GLineEdit_313["fg"] = "#333333"
        self.GLineEdit_313["justify"] = "center"
        self.GLineEdit_313.insert(0, self.datos["velocidad_enemigo_incremento"])
        self.GLineEdit_313.place(x=250,y=530,width=70,height=25)

        self.GButton_233=tk.Button(root)
        self.GButton_233["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        self.GButton_233["font"] = ft
        self.GButton_233["fg"] = "#000000"
        self.GButton_233["justify"] = "center"
        self.GButton_233["text"] = "Gardar"
        self.GButton_233.place(x=80,y=620,width=70,height=25)
        self.GButton_233["command"] = self.GButton_233_command

        self.GButton_817=tk.Button(root)
        self.GButton_817["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        self.GButton_817["font"] = ft
        self.GButton_817["fg"] = "#000000"
        self.GButton_817["justify"] = "center"
        self.GButton_817["text"] = "Atrás"
        self.GButton_817.place(x=250,y=620,width=70,height=25)
        self.GButton_817["command"] = self.GButton_817_command

    def GButton_233_command(self):
        print("Guardar")
        # Hacer conversión a numeros
        self.datos["pantalla_tamano"][0] =  float(self.GLineEdit_209.get()) 
        self.datos["pantalla_tamano"][1] =  float(self.GLineEdit_889.get()) 
        self.datos["velocidad_enemigo"] =  float(self.GLineEdit_24.get()) 
        self.datos["velocidad_jugador"] =  float(self.GLineEdit_97.get()) 
        self.datos["radio_enemigo"] =  float(self.GLineEdit_665.get()) 
        self.datos["radio_jugador"] =  float(self.GLineEdit_200.get()) 
        self.datos["cantidad_enemigos"] =  float(self.GLineEdit_385.get()) 
        self.datos["multiplicador_puntos"] =  float(self.GLineEdit_513.get()) 
        self.datos["ticks_puntos"] =  float(self.GLineEdit_953.get()) 
        self.datos["velocidad_enemigo_incrementar_en_intervalo"] =  float(self.GLineEdit_249.get()) 
        self.datos["velocidad_enemigo_incremento"] =  float(self.GLineEdit_313.get())

        self.guardar_json("database", self.datos)


    def GButton_817_command(self):
        from menu import run as menu_runner
        self.root.destroy()
        menu_runner()


    def guardar_json(self, nombre_archivo, datos):
        with open(nombre_archivo, 'w') as archivo:
            json.dump(datos, archivo, indent=4)

    def cargar_json(self, nombre_archivo, datos_default = None):
        if not os.path.exists(nombre_archivo):
            if datos_default is not None:
                return datos_default
            else:
                return {}
        else:
            with open(nombre_archivo, 'r') as archivo:
                return json.load(archivo)

def run():
    global root
    root = tk.Tk()
    app = App(root)
    root.mainloop()
