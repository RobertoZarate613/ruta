import hashlib
import tkinter as tk
from tkinter import messagebox
import openpyxl
import threading
import time  
import watchdog 
    

# Crear una función para encriptar una contraseña
def encriptar(password):
    # Convertir la contraseña a bytes
    password = password.encode()
    # Aplicar el algoritmo SHA256
    password = hashlib.sha256(password).hexdigest()
    # Retornar la contraseña encriptada
    return password

# Crear una función para validar el inicio de sesión
def validar():
    # Obtener el nombre de usuario y la contraseña ingresados
    usuario = entry_usuario.get()
    password = entry_password.get()
    # Encriptar la contraseña
    password = encriptar(password)
    # Abrir el archivo de datos en modo de lectura 
    archivo = open("Base.txt", "r")
    # Recorrer cada línea del archivo
    for linea in archivo:
        # Separar los campos por comas
        campos = linea.split(",")
        # Verificar si el usuario y la contraseña coinciden con algún registro
        if usuario == campos[0] and password == campos[1]:
            # Cerrar el archivo
            archivo.close()
            # Cerrar la ventana de inicio de sesión
            ventana.destroy()
            # Obtener el tipo de usuario
            tipo = campos[2].strip()
            # Abrir la ventana correspondiente al tipo de usuario
            if tipo == "Administrador":
                ventana_admin()
            elif tipo == "Catedratico":
                ventana_catedratico()
            elif tipo == "Estudiante":
                ventana_estudiante()
            # Terminar la función
            return
    # Cerrar el archivo
    archivo.close()
    # Mostrar un mensaje de error si no se encontró el usuario o la contraseña
    messagebox.showerror("Error", "Usuario o contraseña incorrectos")

# Crear una función para registrar un nuevo usuario de tipo estudiante
def registrar():
    # Obtener los datos ingresados por el usuario
    nombre = entry_nombre.get()
    apellido = entry_apellido.get()
    dpi = entry_dpi.get()
    fecha = entry_fecha.get()
    telefono = entry_telefono.get()
    usuario = entry_usuario_reg.get()
    correo = entry_correo.get()
    password = entry_password_reg.get()
    confirmacion = entry_confirmacion.get()
    # Verificar que todos los campos estén llenos
    if nombre and apellido and dpi and fecha and telefono and usuario and correo and password and confirmacion:
        # Verificar que la contraseña y la confirmación coincidan
        if password == confirmacion:
            # Encriptar la contraseña
            password = encriptar(password)
            # Abrir el archivo de datos en modo de abrir
            archivo = open("Base.txt", "a")
            # Escribir los datos del nuevo usuario en el archivo, separados por comas y con un salto de línea al final
            archivo.write(f"{usuario},{password},Estudiante,{nombre},{apellido},{dpi},{fecha},{telefono},{correo}\n")
            # Cerrar el archivo
            archivo.close()
            # Mostrar un mensaje de éxito
            messagebox.showinfo("Éxito", "Usuario registrado correctamente")
            # Cerrar la ventana de registro
            ventana_reg.destroy()
        else:
            # Mostrar un mensaje de error si las contraseñas no coinciden
            messagebox.showerror("Error", "Las contraseñas no coinciden")
    else:
        # Mostrar un mensaje de error si algún campo está vacío
        messagebox.showerror("Error", "Todos los campos son obligatorios")

# Crear una función para registrar un nuevo usuario de tipo estudiante
def ventana_registro():
    global ventana_reg, entry_nombre, entry_apellido, entry_dpi, entry_fecha, entry_telefono, entry_usuario_reg, entry_correo, entry_password_reg, entry_confirmacion 
    # Crear una nueva ventana para el registro
    ventana_reg = tk.Tk()
    ventana_reg.title("Registro_Estudiante")
    ventana_reg.geometry("400x400")
    # Crear las etiquetas y las entradas para los datos del nuevo usuario
    label_nombre = tk.Label(ventana_reg, text="Nombre:")
    label_nombre.place(x=50, y=50)
    entry_nombre = tk.Entry(ventana_reg)
    entry_nombre.place(x=150, y=50)
    label_apellido = tk.Label(ventana_reg, text="Apellido:")
    label_apellido.place(x=50, y=80)
    entry_apellido = tk.Entry(ventana_reg)
    entry_apellido.place(x=150, y=80)
    label_dpi = tk.Label(ventana_reg, text="DPI:")
    label_dpi.place(x=50, y=110)
    entry_dpi = tk.Entry(ventana_reg)
    entry_dpi.place(x=150, y=110)
    label_fecha = tk.Label(ventana_reg, text="Fecha de nacimiento:")
    label_fecha.place(x=50, y=140)
    entry_fecha = tk.Entry(ventana_reg)
    entry_fecha.place(x=150, y=140)
    label_telefono = tk.Label(ventana_reg, text="Teléfono:")
    label_telefono.place(x=50, y=170)
    entry_telefono = tk.Entry(ventana_reg)
    entry_telefono.place(x=150, y=170)
    label_usuario_reg = tk.Label(ventana_reg, text="Nombre de usuario:")
    label_usuario_reg.place(x=50, y=200)
    entry_usuario_reg = tk.Entry(ventana_reg)
    entry_usuario_reg.place(x=150, y=200)
    label_correo = tk.Label(ventana_reg, text="Correo electrónico:")
    label_correo.place(x=50, y=230)
    entry_correo = tk.Entry(ventana_reg)
    entry_correo.place(x=150, y=230)
    label_password_reg = tk.Label(ventana_reg, text="Contraseña:")
    label_password_reg.place(x=50, y=260)
    entry_password_reg = tk.Entry(ventana_reg, show="*")
    entry_password_reg.place(x=150, y=260)
    label_confirmacion = tk.Label(ventana_reg, text="Confirmar contraseña:")
    label_confirmacion.place(x=50, y=290)
    entry_confirmacion = tk.Entry(ventana_reg, show="*")
    entry_confirmacion.place(x=150, y=290)
    # Crear un botón para registrar al nuevo usuario
    boton_registrar = tk.Button(ventana_reg, text="Registrar", command=registrar)
    boton_registrar.place(x=150, y=330)
 
# Crear una función para registrar un nuevo usuario de tipo catedratico
def registrar_Catedratico():
    # Obtener los datos ingresados por el usuario
    nombre = entry_nombre.get()
    apellido = entry_apellido.get()
    dpi = entry_dpi.get()
    usuario = entry_usuario_reg.get()
    password = entry_password_reg.get()
    confirmacion = entry_confirmacion.get()
    # Verificar que todos los campos estén llenos
    if nombre and apellido and dpi and usuario and password and confirmacion:
        # Verificar que la contraseña y la confirmación coincidan
        if password == confirmacion:
            # Encriptar la contraseña
            password = encriptar(password)
            # Abrir el archivo de datos en modo de abrir
            archivo = open("Base.txt", "a")
            # Escribir los datos del nuevo usuario en el archivo, separados por comas y con un salto de línea al final
            archivo.write(f"{usuario},{password},Catedratico,{nombre},{apellido},{dpi}\n")
            # Cerrar el archivo
            archivo.close()
            # Mostrar un mensaje de éxito
            messagebox.showinfo("Éxito", "Usuario registrado correctamente")
            # Cerrar la ventana de registro
            ventana_reg.destroy()
        else:
            # Mostrar un mensaje de error si las contraseñas no coinciden
            messagebox.showerror("Error", "Las contraseñas no coinciden")
    else:
        # Mostrar un mensaje de error si algún campo está vacío
        messagebox.showerror("Error", "Todos los campos son obligatorios")
        
# Crear una función para registrar un nuevo usuario de tipo catedratico
def ventana_Resgistro_Catedratico():    
    global ventana_reg, entry_nombre, entry_apellido, entry_dpi, entry_usuario_reg,entry_password_reg, entry_confirmacion 
    # Crear una nueva ventana para el registro
    ventana_reg = tk.Tk()
    ventana_reg.title("Registro_Profesor")
    ventana_reg.geometry("400x400")
    # Crear las etiquetas y las entradas para los datos del nuevo usuario
    label_nombre = tk.Label(ventana_reg, text="Nombre:")
    label_nombre.place(x=50, y=50)
    entry_nombre = tk.Entry(ventana_reg)
    entry_nombre.place(x=150, y=50)
    label_apellido = tk.Label(ventana_reg, text="Apellido:")
    label_apellido.place(x=50, y=80)
    entry_apellido = tk.Entry(ventana_reg)
    entry_apellido.place(x=150, y=80)
    label_dpi = tk.Label(ventana_reg, text="DPI:")
    label_dpi.place(x=50, y=110)
    entry_dpi = tk.Entry(ventana_reg)
    entry_dpi.place(x=150, y=110)
    label_usuario_reg = tk.Label(ventana_reg, text="Nombre de usuario:")
    label_usuario_reg.place(x=50, y=140)
    entry_usuario_reg = tk.Entry(ventana_reg)
    entry_usuario_reg.place(x=150, y=140)
    label_password_reg = tk.Label(ventana_reg, text="Contraseña:")
    label_password_reg.place(x=50, y=170)
    entry_password_reg = tk.Entry(ventana_reg, show="*")
    entry_password_reg.place(x=150, y=170)
    label_confirmacion = tk.Label(ventana_reg, text="Confirmar contraseña:")
    label_confirmacion.place(x=50, y=200)
    entry_confirmacion = tk.Entry(ventana_reg, show="*")
    entry_confirmacion.place(x=150, y=200)
    # Crear un botón para registrar al nuevo usuario
    boton_registrar = tk.Button(ventana_reg, text="Registro profesor", command=registrar_Catedratico)
    boton_registrar.place(x=150, y=250)

#se definio una clase llamada "Curso", representa y modela mi tipo de objeto 
    class Curso:
        def __init__(self, costo, horario, codigo, cupo, nombre_catedratico):
            self.costo = costo # Atributo para el costo del curso
            self.horario = horario # Atributo para el horario del curso
            self.codigo = codigo # Atributo para el código del curso
            self.cupo = cupo # Atributo para el cupo del curso
            self.nombre_catedratico = nombre_catedratico # Atributo para el nombre del catedrático
        
     # Método para devolver una cadena con la información del curso
    def str(self):
        return f"codigo: {self.codigo}\nCurso: {self.codigo}\nCosto: {self.costo}\nHorario: {self.horario}\nCupo: {self.cupo}\nNombre del catedrático: {self.nombre_catedratico}" 
    
    # Método para guardar la información del curso en un archivo de texto 
    def guardar(self):
        with open("Materia.txt", "a") as archivo: # Se abre el archivo en modo de escritura 
             # Se escribe la información del curso en el archivo
            archivo.write(f"codigo: {self.codigo}, Costo: {self.costo}, Horario: {self.horario}, Cupo: {self.cupo}, Nombre del catedratico: {self.nombre_catedratico}\n")  
 
    # Define una función llamada agregar 
    def agregar(self, costo, horario, codigo, cupo, nombre_catedratico):
    # Crea un nuevo objeto de la clase Curso con los valores de los parámetros
        nuevo_curso = Curso(costo, horario, codigo, cupo, nombre_catedratico)
    # Llama al método guardar del objeto nuevo_curso para escribir sus datos en el archivo
        nuevo_curso.guardar() 

    
    # Define una función llamada editar 
    def editar(self, costo, horario, codigo, cupo, nombre_catedratico):
        with open("Materia.txt", "r") as archivo:
            lineas = archivo.readlines()
    # Recorre la lista lineas con un bucle for usando la variable linea como elemento
        for linea in lineas:
        # Divide cada línea por el carácter de salto de línea y guarda el resultado en una lista llamada datos
            datos = linea.split("\n")# Convierte la línea en una lista de datos
        # Comprueba si el primer elemento de la lista datos es igual a la cadena del codigo
            if datos[0] == f"Curso: {codigo}":# Compara el código del curso con el parámetro
            # Asigna los nuevos valores a los atributos solo si son diferentes a los anteriores             
            # Comprueba si el segundo elemento de la lista datos es diferente a la cadena costo
             if datos[1] != f"Costo: {costo}":
                # Si es así, asigna el valor de la variable costo al atributo costo del objeto self
                self.costo = costo
            # Comprueba si el tercer elemento de la lista datos es diferente a la cadena Horarioro
             if datos[2] != f"Horario: {horario}":
                # Si es así, asigna el valor de la variable horario al atributo horario del objeto self
                self.horario = horario
            # Comprueba si el cuarto elemento de la lista datos es diferente a la cadena Cupo
             if datos[3] != f"Cupo: {cupo}":
                # Si es así, asigna el valor de la variable cupo al atributo cupo del objeto self
                self.cupo = cupo
            # Comprueba si el quinto elemento de la lista datos es diferente a la cadena Nombre del catedrático
             if datos[4] != f"Nombre del catedratico: {nombre_catedratico}":
                # Si es así, asigna el valor de la variable nombre_catedratico al atributo nombre_catedratico del objeto self
                self.nombre_catedratico = nombre_catedratico
             # Llama al método guardar del objeto self para escribir los nuevos datos en el archivo
            self.guardar()# Llama al método guardar para escribir los nuevos datos en el archivo

        
     # Define una función llamada eliminar 
    def eliminar(self, codigo): 
    # Abre un archivo llamado Materia.txt en modo de lectura y lo asigna a la variable archivo
        with open("Materia.txt", "r") as archivo:
        # Lee todas las líneas del archivo y las guarda en una lista llamada lineas
            lineas = archivo.readlines()
    # Recorre la lista lineas con un bucle for usando la variable i como índice
        for i in range(len(lineas)):
        # Divide cada línea por el carácter de salto de línea y guarda el resultado en una lista llamada datos
            datos = lineas[i].split("\n")
        # Comprueba si el primer elemento de la lista datos es igual a la cadena 
            if datos[0] == f"Curso: {self, codigo}":
            # Si es así, elimina la línea correspondiente de la lista lineas usando el operador del
                del lineas[i]
                self.guardar()
            # Rompe el bucle for usando la instrucción break
            break
        # Abre el mismo archivo en modo de escritura y lo asigna a la variable archivo
        with open("Materia.txt", "w") as archivo:
        # Recorre la lista lineas con otro bucle for usando la variable linea como elemento
            for linea in lineas:
            # Escribe cada línea en el archivo usando el método write
                archivo.write(linea)
    
    # Define una función llamada modificar 
    def modificar(self, costo, horario, codigo, cupo, nombre_catedratico):
        with open("Materia.txt", "r") as archivo:
        # Lee todas las líneas del archivo y las guarda en una lista llamada lineas
            lineas = archivo.readlines()
    # Recorre la lista lineas con un bucle for usando
        for linea in lineas:
        # Divide cada línea por el carácter de salto de línea y guarda el resultado en una lista llamada datos
            datos = linea.split("\n") # Convierte la línea en una lista de datos
        # Comprueba si el primer elemento de la lista datos es igual a la cadena "Curso: " seguida del valor de la variable codigo
            if datos[0] == f"Curso: {codigo}": # Compara el código del curso con el parámetro
    
     # Asigna los nuevos valores a los atributos solo si son diferentes a los anteriores
            # Comprueba si el segundo elemento de la lista datos es diferente a la cadena "Costo: " seguida del valor de la variable costo
             if datos[1] != f"Costo: {costo}":
                # Si es así, asigna el valor de la variable costo al atributo costo del objeto self
                self.costo = costo
            # Comprueba si el tercer elemento de la lista datos es diferente a la cadena "Horario: " seguida del valor de la variable horario
             if datos[2] != f"Horario: {horario}":
                # Si es así, asigna el valor de la variable horario al atributo horario del objeto self
                self.horario = horario
            # Comprueba si el cuarto elemento de la lista datos es diferente a la cadena "Cupo: " seguida del valor de la variable cupo
             if datos[3] != f"Cupo: {cupo}":
                # Si es así, asigna el valor de la variable cupo al atributo cupo del objeto self
                self.cupo = cupo
            # Comprueba si el quinto elemento de la lista datos es diferente a la cadena "Nombre del catedrático: " seguida del valor de la variable nombre_catedratico
             if datos[4] != f"Nombre del catedratico: {nombre_catedratico}":
                # Si es así, asigna el valor de la variable nombre_catedratico al atributo nombre_catedratico del objeto self
                self.nombre_catedratico = nombre_catedratico
            # Llama al método guardar del objeto self para escribir los nuevos datos en el archivo
             self.guardar() # Llama al método guardar para escribir los nuevos datos en el archivo

def ventana_cursos():
    ventana_cur= tk.Toplevel()  # Se crea una ventana para las caracteristicas del curso.
    ventana_cur.title("Ventana Cursos") 
    ventana_cur.geometry("500x500")

    # Creamos las etiquetas y las entradas para los datos de los cursos y las colocamos en la grilla
    etiqueta_costo = tk.Label(ventana_cur, text="Costo:") # Se crea una etiqueta para el costo
    etiqueta_costo.grid(row=0, column=0)# Se coloca la etiqueta en la grilla
    entrada_costo = tk.Entry(ventana_cur) # Se crea una entrada para el costo
    entrada_costo.grid(row=0, column=1) # Se coloca la entrada en la grilla

    etiqueta_horario = tk.Label(ventana_cur, text="Horario:") # Se crea una etiqueta para el horario
    etiqueta_horario.grid(row=1, column=0) # Se coloca la etiqueta en la grilla
    entrada_horario = tk.Entry(ventana_cur) # Se crea una entrada para el horario
    entrada_horario.grid(row=1, column=1) # Se coloca la entrada en la grilla

    etiqueta_codigo = tk.Label(ventana_cur, text="Código:") # Se crea una etiqueta para el codigo
    etiqueta_codigo.grid(row=2, column=0)  # Se coloca la etiqueta en la grilla
    entrada_codigo = tk.Entry(ventana_cur) # Se crea una entrada para el código
    entrada_codigo.grid(row=2, column=1) # Se coloca la entrada en la grilla

    etiqueta_cupo = tk.Label(ventana_cur, text="Cupo:") # Se crea una etiqueta para el cupo
    etiqueta_cupo.grid(row=3, column=0) # Se coloca la etiqueta en la grilla
    entrada_cupo = tk.Entry(ventana_cur) # Se crea una entrada para el cupo
    entrada_cupo.grid(row=3, column=1) # Se coloca la entrada en la grilla
      # Se crea una etiqueta para el nombre del catedrático
    etiqueta_nombre_catedratico = tk.Label(ventana_cur, text="Nombre del catedrático:") 
      # Se crea una etiqueta para el nombre del catedrático
    etiqueta_nombre_catedratico.grid(row=4, column=0) # Se coloca la etiqueta en la grilla
    entrada_nombre_catedratico = tk.Entry(ventana_cur)# Se crea una entrada para el nombre del catedrático
    entrada_nombre_catedratico.grid(row=4, column=1) # Se coloca la entrada en la grilla


    # Creamos los botones para agregar, editar, eliminar y modificar los cursos y les asignamos los comandos correspondientes a los métodos de la clase Curso
    # Para pasar los valores de las entradas a los métodos usamos el método get y la función lambda
      # Se crea un botón para agregar un curso
    boton_agregar = tk.Button(ventana_cur, text="Agregar", command=lambda: curso.agregar(entrada_costo.get(), entrada_horario.get(), entrada_codigo.get(), entrada_cupo.get(), entrada_nombre_catedratico.get())) 
    boton_agregar.grid(row=5, column=0) #Se coloca el botón en la grilla 
   
    # Se crea un botón para editar un curso
    boton_editar = tk.Button(ventana_cur, text="Editar", command=lambda: curso.editar(entrada_costo.get(), entrada_horario.get(), entrada_codigo.get(), entrada_cupo.get(), entrada_nombre_catedratico.get())) 
    boton_editar.grid(row=5, column=1) # Se coloca el botón en la grilla
     # Se crea un bo
     # tón para eliminar un curso
    boton_eliminar = tk.Button(ventana_cur, text="Eliminar", command=lambda: curso.eliminar(entrada_codigo.get()))
    boton_eliminar.grid(row=6, column=0) # Se coloca el botón en la grilla


    def lista_actualizar():   
    # Creamos una lista para mostrar los cursos que coincidan con el nombre del catedrático que se ingrese y la colocamos en la grilla
        lista_cursos = tk.Listbox(ventana_cur)
        lista_cursos.grid(row=8, columnspan=2) 
        with open("Materia.txt", "r") as archivo: # Se abre el archivo en modo de lectura
            lineas = archivo.readlines()# Se lee el contenido del archivo como una lista de líneas
    
            for linea in lineas: # Se recorre la lista de líneas
                 if entrada_nombre_catedratico.get() in linea:# Se verifica que el nombre del catedrático esté en la línea
                    lista_cursos.insert(tk.END, linea)# Se inserta la línea en la lista de cursos
    # Se crea un botón para editar un curso
    boton_Actulizar = tk.Button(ventana_cur, text="Actulizar", command= lista_actualizar) 
    boton_Actulizar.grid(row=6, column=1) # Se coloca el botón en la grilla
    
def ventana_cursos_profesor():
 
    ventana_curs= tk.Toplevel()  # Se crea una ventana para las caracteristicas del curso.
    ventana_curs.title("Ventana Cursos") 
    ventana_curs.geometry("500x500")

    # Creamos las etiquetas y las entradas para los datos de los cursos y las colocamos en la grilla
    etiqueta_costo = tk.Label(ventana_curs, text="Costo:") # Se crea una etiqueta para el costo
    etiqueta_costo.grid(row=0, column=0)# Se coloca la etiqueta en la grilla
    entrada_costo = tk.Entry(ventana_curs) # Se crea una entrada para el costo
    entrada_costo.grid(row=0, column=1) # Se coloca la entrada en la grilla

    etiqueta_horario = tk.Label(ventana_curs, text="Horario:") # Se crea una etiqueta para el horario
    etiqueta_horario.grid(row=1, column=0) # Se coloca la etiqueta en la grilla
    entrada_horario = tk.Entry(ventana_curs) # Se crea una entrada para el horario
    entrada_horario.grid(row=1, column=1) # Se coloca la entrada en la grilla

    etiqueta_codigo = tk.Label(ventana_curs, text="Código:") # Se crea una etiqueta para el codigo
    etiqueta_codigo.grid(row=2, column=0)  # Se coloca la etiqueta en la grilla
    entrada_codigo = tk.Entry(ventana_curs) # Se crea una entrada para el código
    entrada_codigo.grid(row=2, column=1) # Se coloca la entrada en la grilla

    etiqueta_cupo = tk.Label(ventana_curs, text="Cupo:") # Se crea una etiqueta para el cupo
    etiqueta_cupo.grid(row=3, column=0) # Se coloca la etiqueta en la grilla
    entrada_cupo = tk.Entry(ventana_curs) # Se crea una entrada para el cupo
    entrada_cupo.grid(row=3, column=1) # Se coloca la entrada en la grilla
      # Se crea una etiqueta para el nombre del catedrático
    etiqueta_nombre_catedratico = tk.Label(ventana_curs, text="Nombre del catedrático:") 
      # Se crea una etiqueta para el nombre del catedrático
    etiqueta_nombre_catedratico.grid(row=4, column=0) # Se coloca la etiqueta en la grilla
    entrada_nombre_catedratico = tk.Entry(ventana_curs)# Se crea una entrada para el nombre del catedrático
    entrada_nombre_catedratico.grid(row=4, column=1) # Se coloca la entrada en la grilla

    # Se crea un botón para editar un curso
    boton_editar = tk.Button(ventana_curs, text="Editar", command=lambda: curso.editar(entrada_costo.get(), entrada_horario.get(), entrada_codigo.get(), entrada_cupo.get(), entrada_nombre_catedratico.get())) 
    boton_editar.grid(row=5, column=1) # Se coloca el botón en la grilla

    def lista_actualizar_profesor():   
    # Creamos una lista para mostrar los cursos que coincidan con el nombre del catedrático que se ingrese y la colocamos en la grilla
        lista_cursos_pro = tk.Listbox( ventana_curs)
        lista_cursos_pro.grid(row=7, columnspan=2) 
        with open("Materia.txt", "r") as archivo: # Se abre el archivo en modo de lectura
            lineas = archivo.readlines()# Se lee el contenido del archivo como una lista de líneas
    
            for linea in lineas: # Se recorre la lista de líneas
                 if entrada_nombre_catedratico.get() in linea:# Se verifica que el nombre del catedrático esté en la línea
                    lista_cursos_pro.insert(tk.END, linea)# Se inserta la línea en la lista de cursos      
    # Se crea un botón para editar un curso
    boton_Actulizar_pro = tk.Button(ventana_curs, text="Actulizar", command= lista_actualizar_profesor) 
    boton_Actulizar_pro.grid(row=5, column=0) # Se coloca el botón en la grilla
    
# Crear la ventana principal para el inicio de sesión
ventana = tk.Tk()
ventana.title("Inicio de sesión")
ventana.geometry("300x200")
# Crear las etiquetas y las entradas para el nombre de usuario y la contraseña
label_usuario = tk.Label(ventana, text="Usuario:")
label_usuario.place(x=50, y=50)
entry_usuario = tk.Entry(ventana)
entry_usuario.place(x=100, y=50)
label_password = tk.Label(ventana, text="Contraseña:")
label_password.place(x=50, y=80)
entry_password = tk.Entry(ventana, show="*")
entry_password.place(x=100, y=80)
 
# Crear un botón para iniciar sesión
boton_iniciar = tk.Button(ventana, text="Iniciar sesión", command=validar)
boton_iniciar.place(x=100, y=120)
# Crear un botón para registrarse
boton_registrarse = tk.Button(ventana, text="Registrarse", command=ventana_registro)
boton_registrarse.place(x=100, y=150)

# Crear una función para abrir la ventana de administración
def ventana_admin():
    global ventana
    # Crear una nueva ventana para el administrador
    ventana_adm = tk.Tk()
    ventana_adm.title("Administración")
    ventana_adm.geometry("1000x600")
 
    # Crear un botón para registrarse
    boton_registrarse_profesor= tk.Button(ventana_adm, text="Registrar Profesor", command=ventana_Resgistro_Catedratico)
    boton_registrarse_profesor.place(x=350, y=0)

    boton_cursos = tk.Button(ventana_adm, text="Cursos", command=ventana_cursos)
    boton_cursos.pack()  
    
    def cerrar_sesion():
        global ventana # Usar la variable global de la ventana principal
        ventana.deiconify() # Mostrar la ventana principal
        ventana_adm.destroy() # Cerrar la ventana actual

    # Crear un botón para cerrar sesión en cada ventana
    boton_cerrar_sesion = tk.Button(ventana_adm, text="Cerrar sesión", command=cerrar_sesion)
    boton_cerrar_sesion.place(x=0, y=0) # Colocar el botón en una posición adecuada
    
curso = Curso(0, "", "", 0, "")
    
    
# Crear una función para abrir la ventana de catedrático
def ventana_catedratico():
    global ventana
    # Crear una nueva ventana para el catedrático
    ventana_cat = tk.Tk()
    ventana_cat.title("Catedrático")
    ventana_cat.geometry("1000x600")
     
    boton_cursos = tk.Button(ventana_cat, text="Cursos", command=ventana_cursos_profesor)
    boton_cursos.pack()  
    
    etiqueta_nombre = tk.Label(ventana_cat, text="Nombre") # Se crea una etiqueta para el nombre
    etiqueta_nombre.grid(row=0, column=0) # Se coloca la etiqueta en la grilla
 
    entrada_nombre = tk.Entry(ventana_cat) # Se crea una entrada para el nombre
    entrada_nombre.grid(row=0, column=1) # Se coloca
    
    def cerrar_sesion():
        global ventana # Usar la variable global de la ventana principal
        ventana.deiconify() # Mostrar la ventana principal
        ventana_cat.destroy() # Cerrar la ventana actual

    # Crear un botón para cerrar sesión en cada ventana
    boton_cerrar_sesion = tk.Button(ventana_cat, text="Cerrar sesión", command=cerrar_sesion)
    boton_cerrar_sesion.place(x=0, y=0) # Colocar el botón en una posición adecuada
    
curso = Curso(0, "", "", 0, "")
    
    

def ventana_estudiante():
    global ventana
    # Crear una nueva ventana para el estudiante
    ventana_est = tk.Tk()
    ventana_est.title("Estudiante")
    ventana_est.geometry("1000x600")

    lista_cursos = tk.Listbox(ventana_est) # Se crea una lista para mostrar los cursos
    lista_cursos.pack() # Se coloca la lista en la ventana

    with open("Materia.txt", "r") as archivo: # Se abre el archivo en modo de lectura
        lineas = archivo.readlines() # Se lee el contenido del archivo como una lista de líneas

    for linea in lineas: # Se recorre la lista de líneas
        lista_cursos.insert(tk.END, linea) # Se inserta la línea en la lista de cursos
        
    def cerrar_sesion():
        global ventana # Usar la variable global de la ventana principal
        ventana.deiconify() # Mostrar la ventana principal
        ventana_est.destroy() # Cerrar la ventana actual

    # Crear un botón para cerrar sesión en cada ventana
    boton_cerrar_sesion = tk.Button(ventana_est, text="Cerrar sesión", command=cerrar_sesion)
    boton_cerrar_sesion.place(x=0, y=0) # Colocar el botón en una posición adecuada
    
# Iniciar el bucle principal de la ventana
ventana.mainloop()

