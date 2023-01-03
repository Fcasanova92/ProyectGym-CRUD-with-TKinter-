import sqlite3

from datetime import datetime, timedelta

# esta clase maneja los metodos que se activan en los botones de gestion de alumnos, interactuando con la base de datos

class MODEL:

    def AGREGAR (self, data):

        self.conexion = sqlite3.connect("Base de datos Alumnos Gym")

        self.cursor = self.conexion.cursor()

        self.cursor.execute("INSERT INTO ALUMNOS VALUES (?,?,?,?,?,?,?)", (data))

        self.conexion.commit()

        self.conexion.close()


    def BUSCAR(self, id):

        self.conexion = sqlite3.connect("Base de datos Alumnos Gym")
        
        self.cursor = self.conexion.cursor()

        self.cursor.execute("SELECT NOMBRE, APELLIDO, TELEFONO, EMAIL, FECHA, RUTINA FROM ALUMNOS WHERE DNI =" + id)

        self.datos_alumno = self.cursor.fetchall()

        return  self.datos_alumno

      

    def ACTUALIZAR(self, id, data):

        self.cursor.execute("UPDATE ALUMNOS SET NOMBRE=?, APELLIDO=?, TELEFONO=?, EMAIL= ?, FECHA=? , RUTINA = ? WHERE DNI =" + id,(data))

        self.conexion.commit()

        self.conexion.close()


    
    def BORRAR(self, id):

        # el self.dni.get se tiene que obtener por un getter proveniende del objeto interfaz

        self.cursor.execute("DELETE FROM ALUMNOS WHERE DNI =" + id)

        self.conexion.commit()

        self.conexion.close()


# este metodo muestra los datos cuando el alumno indica el dni para saber si puede ingresar o no al gimnasio

    def VIEW_ALUMNO(self, id2):

        self.cursor.execute("SELECT NOMBRE, APELLIDO, FECHA, RUTINA FROM ALUMNOS WHERE DNI =" + id2)

        self.data_view_datos=self.cursor.fetchall()

        self.conexion.close()

        return  self.data_view_datos



# estas lineas de codigo van en el controlador, donde se visualizara
#la informacion en la ventana principal


 #  for i in view_datos:
            
#  #          self.nombre_bienvenida.set(i[0] + " " + i[1])

  #          fecha_pago = i[2]

 #           self.rutina_bienvenida.set(i[3])

#
    #    fecha_pago = datetime.strptime(fecha_pago, "%Y-%m-%d")
#
    #   self.fecha_vencimiento = fecha_pago + timedelta(days=30)
#
     #   self.vencimiento.set(self.fecha_vencimiento)
#
