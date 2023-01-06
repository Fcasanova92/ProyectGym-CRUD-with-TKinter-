
from model import MODEL

from vista import INTERFAZ

from tkinter import ttk

import tkinter as tk

from tkinter import messagebox as ms

from datetime import datetime, timedelta

import re


# es esta clase se controlan las excepciones y los errores

# IMPORTAR EL CONTROLADOR A LA VISTA


class controller:

     def __init__(self):

          self.root = tk.Tk()

          self.vista = INTERFAZ(self.root, self)

          self.model = MODEL()

          self.root.mainloop()

          
     def agregar_alumno(self):

          try:

               dato_alumno = [self.vista.gestion.DNI.get(), self.vista.gestion.nombre.get(), self.vista.gestion.apellido.get(), self.vista.gestion.email.get(), 
               
               self.vista.gestion.telefono.get(), self.vista.gestion.pago.get(), self.vista.gestion.rutina.get()]

               self.model.AGREGAR(dato_alumno)

               ms.showwarning("Alerta", "Alumno Agregado")

               self.set_field()

          except:

               ms.showwarning("Alerta", " El alumno ya se encuentra inscripto")



     def buscar_alumno(self):

          try:
               id = self.vista.gestion.DNI.get()

               dato_alumno = self.model.BUSCAR(id)

               for dato in dato_alumno:

                    self.vista.gestion.nombre.set(dato[0])
                    
                    self.vista.gestion.apellido.set(dato[1])
                    
                    self.vista.gestion.email.set(dato[2]) 
          
                    self.vista.gestion.telefono.set(dato[3]) 
                    
                    self.vista.gestion.pago.set(dato[4]) 
                    
                    self.vista.gestion.rutina.set(dato[5])

          except:

               ms.showwarning(" Alerta ", " Numero de DNI inexistente ")


     def actualizar_alumno(self):

          try:

               dato_alumno = [self.vista.gestion.nombre.get(), self.vista.gestion.apellido.get(), self.vista.gestion.email.get(), 
               
               self.vista.gestion.telefono.get(), self.vista.gestion.pago.get(), self.vista.gestion.rutina.get()] 

               id = self.vista.gestion.DNI.get()

               self.model.ACTUALIZAR(id, dato_alumno)

               ms.showwarning(" Alerta ", " Alumno Actualizado ")

               self.set_field()

          except:

               ms.showwarning(" Alerta ", " Numero de Dni inexistente")



     def borrar_alumno(self):

          try:

               id = self.vista.gestion.DNI.get()

               self.model.BORRAR(id)

               ms.showwarning(" Alerta ", "Alumno Eliminado ")

               self.set_field()

          except:

               ms.showwarning(" Alerta ", " Numero de Dni inexistente")


     def view_alumno(self):

          data =  self.model.VIEW_ALUMNO()

          for i in data:
                         
               self.vista.nombre_bienvenida.set(i[0] + " " + i[1])

               fecha_pago = i[2]

               self.vista.rutina_bienvenida.set(i[3])

          fecha_pago = datetime.strptime(fecha_pago, "%d/%m/%Y") + timedelta(days=30)

          self.vista.vencimiento.set(fecha_pago)



     def set_field(self):

          self.vista.gestion.DNI.set(" ")

          self.vista.gestion.nombre.set(" ")
                    
          self.vista.gestion.apellido.set(" ")
                    
          self.vista.gestion.email.set(" ") 
          
          self.vista.gestion.telefono.set(" ") 
                    
          self.vista.gestion.pago.set(" ") 
                    
          self.vista.gestion.rutina.set(" ")


     def validate_dni(self, text, new_text):

         if len(new_text) > 8 :

          return False

         return text.isdecimal()

     
     def validate_telefono(self, text, new_text):

         if len(new_text) > 9 :

          return False

         return text.isdecimal()


     def validate_text(self, text):

          return text.isalpha()
          

# Ver el tema de validacion del email, no esta devolviendol, probar con bind

     def validate_email(self, event):

          if event:

               email = self.vista.gestion.email.get()

               if  re.search("^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$", email) is not None:

                    return email

               else:

                    ms.showwarning("Alerta", "mail invalido")

                    self.vista.gestion.email.set()
               


     def validate_date(self, text):

          if len(text) > 10:
               return False

          checks = []

          for i, char in enumerate(text):

               if i in (2, 5):

                    checks.append(char == "/")

               else:
                    checks.append(char.isdecimal())

          return all(checks)
          

     def view_alumno(self):

          try:
               id = self.vista.dni_entry.get()

               data = self.model.VIEW_ALUMNO(id)

               for i in data:

                    self.vista.nombre_bienvenida.set(i[0] + " " + i[1])

                    fecha_pago = i[2]

                    self.vista.rutina_bienvenida.set(i[3])

               self.fecha_vencimiento = datetime.strptime(fecha_pago, "%d/%m/%Y") + timedelta(days=30)

               self.dias_suscrip = round((self.fecha_vencimiento - datetime.today()).total_seconds()/86400)

               self.vista.dias_vencimiento.set(self.dias_suscrip)

               self.vista.vencimiento.set(self.fecha_vencimiento)

               ms.showinfo("Tugym", "Bienvenido")

          except:

               ms.showerror("Alerta", " No es alumno inscripto en el establecimiento")


