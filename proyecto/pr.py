import hashlib
import tkinter as tk
from tkinter import messagebox
import smtplib 

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
    # Abrir el archivo de datos
    archivo = open("Datos.txt", "r")
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
            archivo = open("Datos.txt", "a")
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
# Crear una función para abrir la ventana de registro
def ventana_registro():
    
    global ventana_reg, entry_nombre, entry_apellido, entry_dpi, entry_fecha, entry_telefono, entry_usuario_reg, entry_correo, entry_password_reg, entry_confirmacion 
    # Crear una nueva ventana para el registro
    ventana_reg = tk.Tk()
    ventana_reg.title("Registro")
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
            archivo = open("Datos.txt", "a")
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
    # Crear una nueva ventana para el administrador
    ventana_adm = tk.Tk()
    ventana_adm.title("Administración")
    ventana_adm.geometry("1000x6000")

      # Crear un botón para registrarse
    boton_registrarse_profesor= tk.Button(ventana_adm, text="Registrar Profesor", command=ventana_Resgistro_Catedratico)
    boton_registrarse_profesor.place(x=50, y=50)
       
# Crear una función para abrir la ventana de catedrático
def ventana_catedratico():
    # Crear una nueva ventana para el catedrático
    ventana_cat = tk.Tk()
    ventana_cat.title("Catedrático")
    ventana_cat.geometry("1000x600")

# Crear una función para abrir la ventana de estudiante
def ventana_estudiante():
    # Crear una nueva ventana para el estudiante
    ventana_est = tk.Tk()
    ventana_est.title("Estudiante")
    ventana_est.geometry("1000x600")


# Iniciar el bucle principal de la ventana
ventana.mainloop()

   boton_modificar = tk.Button(ventana_cur, text="Modificar", command=lambda: curso.modificar(entrada_costo.get(), entrada_horario.get(), entrada_codigo.get(), entrada_cupo.get(), entrada_nombre_catedratico.get())) 
    boton_modificar.grid(row=6, column=1) 
    //////////////////////////////////////////
    def lista_actualizar():   
    # Creamos una lista para mostrar los cursos que coincidan con el nombre del catedrático que se ingrese y la colocamos en la grilla
        lista_cursos = tk.Listbox(ventana_cur)
        lista_cursos.grid(row=14, columnspan=10) 
        with open("Materia.txt", "r") as archivo: # Se abre el archivo en modo de lectura
            lineas = archivo.readlines()# Se lee el contenido del archivo como una lista de líneas
    
            for linea in lineas: # Se recorre la lista de líneas
                 if entrada_nombre_catedratico.get() in linea:# Se verifica que el nombre del catedrático esté en la línea
                    lista_cursos.insert(tk.END, linea)# Se inserta la línea en la lista de cursos
                    print(linea) # Se imprime la línea en la consola
    # Se crea un botón para editar un curso
    boton_Actulizar = tk.Button(ventana_cur, text="Actulizar", command= lista_actualizar) 
    boton_Actulizar.grid(row=10, column=4) # Se coloca el botón en la grilla