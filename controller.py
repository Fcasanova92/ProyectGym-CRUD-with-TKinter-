
from model import MODEL

from vista import INTERFAZ

from tkinter import ttk

import tkinter as tk

from tkinter import messagebox as ms

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

          dato_alumno = [self.vista.gestion.DNI.get(), self.vista.gestion.nombre.get(), self.vista.gestion.apellido.get(), self.vista.gestion.email.get(), 
          
          self.vista.gestion.telefono.get(), self.vista.gestion.pago.get(), self.vista.gestion.rutina.get()]

          if len(dato_alumno) == 7:

               self.model.AGREGAR(dato_alumno)

               ms.showwarning(" Alerta ", " Alumno Agregado ")

               self.set_field()

          else:
               ms.showwarning(" Alerta ", " Algunos campos estan vacios ")



     def buscar_alumno(self):

          try:
               dato_alumno = self.model.BUSCAR(self.vista.gestion.DNI.get())

               for dato in dato_alumno:

                    self.vista.gestion.nombre.set(dato[0])
                    
                    self.vista.gestion.apellido.set(dato[1])
                    
                    self.vista.gestion.email.set(dato[2]) 
          
                    self.vista.gestion.telefono.set(dato[3]) 
                    
                    self.vista.gestion.pago.set(dato[4]) 
                    
                    self.vista.gestion.rutina.set(dato[5])

               self.set_field()


          except:

               ms.showwarning(" Alerta ", " Numero de DNI inexistente ")


     def actualizar_alumno(self):

          try:

               dato_alumno = [self.vista.gestion.nombre.get(), self.vista.gestion.apellido.get(), self.vista.gestion.email.get(), 
               
               self.vista.gestion.telefono.get(), self.vista.gestion.entry_pago.entry.get(), self.vista.gestion.rutina.get()] 

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


     
     def set_field(self):

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
          
         
c = controller()











