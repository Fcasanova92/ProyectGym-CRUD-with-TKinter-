
from tkinter import ttk

import tkinter as tk

from datetime import *



# Clase que desarrolla unicamente la interfaz


class INTERFAZ:

    # Constructor de la clase interfaz (contruye la interfaz)

    def __init__(self, root, controller):

        # estos atributos del constructor desarrollan la raiz o fram principal de la interfaz

        self.root = root

        self.controller = controller

        self.root.geometry("1200x720")     

        self.root.resizable(0,0) 

        self.root.title("TuGYM")

        self.gestion = gestion_alumnos(self.root, self.controller)

        self.bar_menu = tk.Menu(self.root)

        self.root.config(relief = "sunken", borderwidth = 10, menu=self.bar_menu, bg="ivory2")

        icono = tk.PhotoImage(file="png-transparent-dumbbells-gym-sport-weight-sports-icon.png")

        icono2= tk.PhotoImage(file="png-transparent-logo-event-planning-fitness-centre-protocol-gym-text-logo-monochrome (1).png")

        self.root.iconphoto(True, icono)

        title = tk.Label(self.root, text = "BIENVENIDO A TUGYM", bg= "ivory2", font=("CASTELLAR",40) )

        title.place(x=240 , y=50 ,  width="700", height="50")

        image = tk.Label(self.root, width="150", height="100", image = icono2 )

        image.place(x=967, y=30)

        self.day_now = tk.Label(self.root, text="  ", font=("Rockwell", 15), bg="ivory2")
                
        self.day_now.place(x=450, y=100, width="90" , height="50")

        self.date_now = tk.Label(self.root, text="  ", font=("Rockwell", 15), bg="ivory2")
                
        self.date_now.place(x=550, y=100, width="90" , height="50")

        self.text_time = tk.Label(self.root, text="  ", font=("Rockwell", 15), bg="ivory2")
                
        self.text_time.place(x=650, y=100, width="90" , height="50")

        # Estos metodos llamados en el constructor desarrollan otras partes secundarias de la interfaz

        self.frame_inf()

        self.menu()

        self.frame_sup()

        self.update_time()



    def frame_sup(self):

        # Estos metodos desarrolla el frame superior, el cual tiene los datos que se muestran cuando se ingresa el dni

        frame1 = tk.Frame(self.root,width="1000", height="400", bg = "ivory3", relief = "solid", borderwidth = 5)

        frame1.place(x=120, y=140)


        bienvenido_alumno = tk.Label(frame1, text="ALUMNO ", font=("Rockwell", 20), bg="ivory3")
        
        bienvenido_alumno.place(x=2, y=20, width="500", height="50")

        self.nombre_bienvenida = tk.StringVar()

        nombre_bienvenida = tk.Entry(frame1, font=("Rockwell", 20), bg = "ivory3", state="readonly", textvariable = self.nombre_bienvenida)

        nombre_bienvenida.place(x=380, y=20 , width="500", height="50")


        bienvenido_rutina = tk.Label(frame1, text="RUTINA ", font=("Rockwell", 20), bg="ivory3")
        
        bienvenido_rutina.place(x=40, y=90, width="400", height="50")

        self.rutina_bienvenida = tk.StringVar()

        rutina = tk.Entry(frame1, font=("Rockwell", 15), bg = "ivory3", state="readonly", textvariable = self.rutina_bienvenida)

        rutina.place(x=380, y=90 , width="500", height="220")



        dias_vencimiento = tk.Label(frame1, text="VENCIMIENTO ", font=("Rockwell", 20), bg="ivory3")

        dias_vencimiento.place(x=127, y=330, width="300", height="50")

        self.vencimiento = tk.StringVar()


        suscr_bienvenida = tk.Entry(frame1, font=("Rockwell", 20), bg = "ivory3", state="disable", textvariable = self.vencimiento)

        suscr_bienvenida.place(x=380, y=330 , width="150", height="50")


        
    def update_time(self):

        # Estos metodo configura el aspecto de la fecha y hora de la interfaz ( el reloj que se ve)

        self.time = datetime.now()
            
        self.hora= self.time.strftime("%H:%M:%S")

        self.text_time.configure(text=self.hora)

            
        self.date = self.time.strftime("%d/%m/%y")

        self.date_now.configure(text=self.date)


        self.day = self.time.strftime("%A")

        if self.day == "Monday":

                self.day = "Lunes"

                self.day_now.configure(text = self.day)


        elif self.day == "Tuesday":

                self.day = "Martes"

                self.day_now.configure(text = self.day)

        elif self.day == "Wednesday":

            self.day = "Miercoles"

            self.day_now.configure(text = self.day)


        elif self.day == "Thursday":

            self.day = "Jueves"

            self.day_now.configure(text = self.day)


        elif self.day == "Friday":

             self.day = "Viernes"

             self.day_now.configure(text = self.day)


        elif self.day == "Saturday":

             self.day = "Sabado"

             self.day_now.configure(text = self.day)


        self.root.after(1000, self.update_time )


        
    def frame_inf(self):

        # Estos metodo configura el frame inferior, donde se busca el dni y se observa los dias que le quedan de suscripcion


        Frame2 = tk.Frame(self.root, width="1000", height="150", bg = "ivory3", relief = "solid", borderwidth = "5")

        Frame2.place(x=120, y=550)


        text_dni2 = tk.Label(Frame2, text="DNI : ", font=("Rockwell", 30), bg="ivory3")
                
        text_dni2.place(x=10, y=35, width="100" , height="50")

        self.dni_entry = tk.StringVar()


        entrada_dni = tk.Entry(Frame2 ,font=("Rockwell", 30),bg="ivory3", textvariable = self.dni_entry)

        entrada_dni.place(x=110, y=45, width = "250", height="40")


        botton_entry_dni = tk.Button(Frame2, text= "OK", font=("Rockwell", 15), relief="sunken", borderwidth="10", bg="ivory3", foreground="black")

        botton_entry_dni.place(x=380, y=45, width=50, height=40)



        text_vencimiento = tk.Label(Frame2, text="Días restantes de suscripcion en el gimnasio :  ", font=("Rockwell", 15), bg="ivory3")
                
        text_vencimiento.place(x=430, y=35, width="500" , height="50")

        self.dias_vencimiento = tk.StringVar()


        self.vencimiento = tk.Entry(Frame2 ,font=("Rockwell", 15),bg="ivory3", state="readonly", textvariable = self.dias_vencimiento)

        self.vencimiento .place(x=900, y=40, width = "30", height="40")



    def menu(self):

        # Estos metodo configura la barra del menu

        gestionfile = tk.Menu(self.bar_menu, tearoff=0)

        helpmenu= tk.Menu(self.bar_menu,tearoff=0)

        self.bar_menu.add_cascade(label="Inicio", menu=gestionfile)

        self.bar_menu.add_cascade(label="Ayuda", menu = helpmenu)

        gestionfile.add_separator()

        gestionfile.add_command(label="Gestion Alumno", command = self.gestion.gestion_alumnos)  

        gestionfile.add_command(label="Gestion Gimnasio")

        gestionfile.add_command(label = "Salir", command= self.root.quit)



class gestion_alumnos:


    def __init__(self, root, controller):

        self.root = root

        self.controller = controller


    def gestion_alumnos(self):

        self.window = tk.Toplevel(self.root,width="600", height="900", bg = "ivory3", relief = "solid", borderwidth = 5)

        self.window.resizable(0,0) 

        self.window.title("GESTION DE ALUMNOS")

        
        self.DNI = tk.StringVar()

        self.nombre = tk.StringVar()

        self.apellido = tk.StringVar()

        self.telefono = tk.StringVar()

        self.email = tk.StringVar()

        self.pago = tk.StringVar()

        self.rutina = tk.StringVar()


        text_dni = tk.Label(self.window, text="DNI  ", font=("Rockwell", 15),bg = "ivory3")
                    
        text_dni .place(x=50,y=50)

        entry_DNI = tk.Entry(self.window, textvariable = self.DNI, validate="key", validatecommand=(self.root.register(self.controller.validate_dni), "%S", "%P"))

        entry_DNI.place(x=250,y=55,width=200, height=20)



        text_nombre = tk.Label(self.window, text="Nombre ", font=("Rockwell", 15),bg = "ivory3")
                        
        text_nombre.place(x=50,y=100)

        entry_nombre = ttk.Entry(self.window, textvariable = self.nombre, validate="key", validatecommand=( self.root.register(self.controller.validate_text), "%S"))

        entry_nombre.place(x=250,y=105, width=200, height=20)


                    
        text_apellido = tk.Label(self.window, text="Apellido  ", font=("Rockwell", 15), bg = "ivory3")

        text_apellido.place(x=50,y=150)

        entry_apellido = tk.Entry(self.window , textvariable = self.apellido, validate = "key", validatecommand=( self.root.register(self.controller.validate_text), "%S"))

        entry_apellido.place(x=250,y=150, width=200, height=20)



        text_telefono = tk.Label(self.window, text="Telefono  ", font=("Rockwell", 15),bg = "ivory3")
                        
        text_telefono.place(x=50,y=200)

        entry_telefono = tk.Entry(self.window, textvariable = self.telefono, validate="key", validatecommand=( self.root.register(self.controller.validate_telefono), "%S", "%P"))

        entry_telefono.place(x=250,y=205,width=200, height=20)



        text_email = tk.Label(self.window, text="Email  ", font=("Rockwell", 15),bg = "ivory3")
                        
        text_email.place(x=50,y=250)
        
        entry_email = tk.Entry(self.window, textvariable = self.email)

        entry_email.bind("<Return>", self.controller.validate_email)

        entry_email.place(x=250,y=255, width=200, height=20)



        text_pago = tk.Label(self.window, text="Fecha de Inscripción  ", font=("Rockwell", 15), bg = "ivory3")
                        
        text_pago.place(x=50,y=300)
     
        entry_pago = tk.Entry(self.window, textvariable = self.pago, validate="key", validatecommand=(self.root.register(self.controller.validate_date), "%P"))

        entry_pago.place(x=250,y=305, width=200, height=20)


        text_rutina = tk.Label(self.window, text = "Rutina ", font=("Rockwell", 15), bg="ivory3")

        text_rutina.place(x=50, y=350)

        self.entry_rutina = tk.Entry(self.window, font=("Rockwell", 15), textvariable = self.rutina )

        self.entry_rutina.place(x=250, y=355, width=300, height=400)
        

                # BOTONES DE GESTIÓN

        self.boton_agregar = tk.Button(self.window, text= "AGREGAR", font=("Rockwell", 10), relief="sunken", borderwidth="10", bg="ivory4", foreground="black", command = self.controller.agregar_alumno)

        self.boton_agregar.place(x=27, y=800, width=100, height=70)


        self.boton_actualizar = tk.Button(self.window, text= "ACTUALIZAR", font=("Rockwell", 10), relief="sunken",borderwidth="10", bg="ivory4", foreground="black", command = self.controller.actualizar_alumno)

        self.boton_actualizar.place(x=167, y=800, width=100, height=70)


        self.boton_borrar = tk.Button(self.window, text= "BORRAR", font=("Rockwell", 10),relief="sunken", borderwidth="10", bg="ivory4", foreground="black", command = self.controller.borrar_alumno)

        self.boton_borrar.place(x=312, y=800, width=100, height=70)


        self.boton_buscar = tk.Button(self.window, text= "BUSCAR", font=("Rockwell", 10),relief="sunken", borderwidth="10", bg="ivory4", foreground="black", command = self.controller.buscar_alumno)

        self.boton_buscar.place(x=457, y=800, width=100, height=70)

            
        self.window.mainloop()
