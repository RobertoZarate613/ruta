import tkinter as tk
from tkinter import messagebox

# Clase para representar un curso
class Curso:
    def __init__(self, costo, horario, codigo, cupo, nombre_catedratico):
        self.costo = costo # Atributo para el costo del curso
        self.horario = horario # Atributo para el horario del curso
        self.codigo = codigo # Atributo para el código del curso
        self.cupo = cupo # Atributo para el cupo del curso
        self.nombre_catedratico = nombre_catedratico # Atributo para el nombre del catedrático

    def __str__(self):
        return f"Curso: {self.codigo}\nCosto: {self.costo}\nHorario: {self.horario}\nCupo: {self.cupo}\nNombre del catedrático: {self.nombre_catedratico}" # Método para devolver una cadena con la información del curso

    def guardar(self):
        # Método para guardar la información del curso en un archivo de texto llamado base
        with open("base.txt", "a") as archivo: # Se abre el archivo en modo de escritura al final
            archivo.write(str(self) + "\n") # Se escribe la información del curso en el archivo

    def eliminar(self):
        # Método para eliminar la información del curso de un archivo de texto llamado base
        with open("base.txt", "r") as archivo: # Se abre el archivo en modo de lectura
            lineas = archivo.readlines() # Se lee el contenido del archivo como una lista de líneas

        with open("base.txt", "w") as archivo: # Se abre el archivo en modo de escritura
            for linea in lineas: # Se recorre la lista de líneas
                if self.codigo not in linea: # Se verifica que el código del curso no esté en la línea
                    archivo.write(linea) # Se escribe la línea en el archivo

# Función para crear la ventana del administrador
def ventana_admin():
    ventana_adm = tk.Tk() # Se crea un objeto de la clase Tk
    ventana_adm.title("Administración") # Se le asigna un título a la ventana
    ventana_adm.geometry("1000x600") # Se le asigna un tamaño a la ventana

    # Botón para crear un nuevo curso
    boton_crear = tk.Button(ventana_adm, text="Crear curso", command=crear_curso) # Se crea un botón con el texto "Crear curso" y se le asigna la función crear_curso como comando
    boton_crear.pack() # Se empaqueta el botón en la ventana

    # Botón para editar un curso existente
    boton_editar = tk.Button(ventana_adm, text="Editar curso", command=editar_curso) # Se crea un botón con el texto "Editar curso" y se le asigna la función editar_curso como comando
    boton_editar.pack() # Se empaqueta el botón en la ventana

    # Botón para eliminar un curso existente
    boton_eliminar = tk.Button(ventana_adm, text="Eliminar curso", command=eliminar_curso) # Se crea un botón con el texto "Eliminar curso" y se le asigna la función eliminar_curso como comando
    boton_eliminar.pack() # Se empaqueta el botón en la ventana

    # Botón para mostrar los cursos creados
    boton_mostrar = tk.Button(ventana_adm, text="Mostrar cursos", command=mostrar_cursos) # Se crea un botón con el texto "Mostrar cursos" y se le asigna la función mostrar_cursos como comando
    boton_mostrar.pack() # Se empaqueta el botón en la ventana

# Función para crear la ventana del catedrático
def ventana_catedratico():
    ventana_cat = tk.Tk() # Se crea un objeto de la clase Tk
    ventana_cat.title("Catedrático") # Se le asigna un título a la ventana
    ventana_cat.geometry("1000x600") # Se le asigna un tamaño a la ventana

    # Botón para editar un curso asignado
    boton_editar = tk.Button(ventana_cat, text="Editar curso", command=editar_curso_asignado) # Se crea un botón con el texto "Editar curso" y se le asigna la función editar_curso_asignado como comando
    boton_editar.pack() # Se empaqueta el botón en la ventana

# Función para crear la ventana del estudiante
def ventana_estudiante():
    ventana_est = tk.Tk() # Se crea un objeto de la clase Tk
    ventana_est.title("Estudiante") # Se le asigna un título a la ventana
    ventana_est.geometry("1000x600") # Se le asigna un tamaño a la ventana

    # Botón para asignarse a un curso
    boton_asignar = tk.Button(ventana_est, text="Asignarse a un curso", command=asignar_curso) # Se crea un botón con el texto "Asignarse a un curso" y se le asigna la función asignar_curso como comando
    boton_asignar.pack() # Se empaqueta el bot
    
    ////////////////////////////////////
    import tkinter as tk
from tkinter import messagebox

# Clase para representar un curso
class Curso:
    def __init__(self, costo, horario, codigo, cupo, nombre_catedratico):
        self.costo = costo
        self.horario = horario
        self.codigo = codigo
        self.cupo = cupo
        self.nombre_catedratico = nombre_catedratico

    def __str__(self):
        return f"Curso: {self.codigo}\nCosto: {self.costo}\nHorario: {self.horario}\nCupo: {self.cupo}\nNombre del catedrático: {self.nombre_catedratico}"

    def guardar(self):
        with open("base.txt", "a") as archivo:
            archivo.write(str(self) + "\n")

    @classmethod
    def obtener_cursos(cls):
        cursos = []
        with open("base.txt", "r") as archivo:
            lineas = archivo.readlines()
            for linea in lineas:
                partes = linea.strip().split('\n')
                costo = float(partes[1].split(': ')[1])
                horario = partes[2].split(': ')[1]
                codigo = partes[0].split(': ')[1]
                cupo = int(partes[3].split(': ')[1])
                nombre_catedratico = partes[4].split(': ')[1]
                cursos.append(cls(costo, horario, codigo, cupo, nombre_catedratico))
        return cursos

    @classmethod
    def eliminar_curso(cls, codigo):
        cursos = cls.obtener_cursos()
        cursos = [curso for curso in cursos if curso.codigo != codigo]
        with open("base.txt", "w") as archivo:
            for curso in cursos:
                archivo.write(str(curso) + "\n")

# Función para crear un nuevo curso
def crear_curso():
    costo = float(entry_costo.get())
    horario = entry_horario.get()
    codigo = entry_codigo.get()
    cupo = int(entry_cupo.get())
    nombre_catedratico = entry_catedratico.get()
    
    curso = Curso(costo, horario, codigo, cupo, nombre_catedratico)
    curso.guardar()
    messagebox.showinfo("Éxito", "Curso creado correctamente")

# Función para eliminar un curso
def eliminar_curso():
    codigo = entry_codigo.get()
    Curso.eliminar_curso(codigo)
    messagebox.showinfo("Éxito", "Curso eliminado correctamente")

# Función para mostrar los cursos
def mostrar_cursos():
    cursos = Curso.obtener_cursos()
    cursos_text = "\n\n".join([str(curso) for curso in cursos])
    messagebox.showinfo("Cursos", cursos_text)

# Crear ventana de administrador
def ventana_admin():
    ventana_adm = tk.Tk()
    ventana_adm.title("Administración")
    ventana_adm.geometry("600x400")

    label_costo = tk.Label(ventana_adm, text="Costo:")
    label_costo.pack()
    entry_costo = tk.Entry(ventana_adm)
    entry_costo.pack()

    label_horario = tk.Label(ventana_adm, text="Horario:")
    label_horario.pack()
    entry_horario = tk.Entry(ventana_adm)
    entry_horario.pack()

    label_codigo = tk.Label(ventana_adm, text="Código:")
    label_codigo.pack()
    entry_codigo = tk.Entry(ventana_adm)
    entry_codigo.pack()

    label_cupo = tk.Label(ventana_adm, text="Cupo:")
    label_cupo.pack()
    entry_cupo = tk.Entry(ventana_adm)
    entry_cupo.pack()

    label_catedratico = tk.Label(ventana_adm, text="Nombre del Catedrático:")
    label_catedratico.pack()
    entry_catedratico = tk.Entry(ventana_adm)
    entry_catedratico.pack()

    boton_crear = tk.Button(ventana_adm, text="Crear curso", command=crear_curso)
    boton_crear.pack()

    boton_eliminar = tk.Button(ventana_adm, text="Eliminar curso", command=eliminar_curso)
    boton_eliminar.pack()

    boton_mostrar = tk.Button(ventana_adm, text="Mostrar cursos", command=mostrar_cursos)
    boton_mostrar.pack()

# Iniciar la aplicación
if __name__ == "__main__":
    ventana_admin()
    tk.mainloop()


***********************
odrias terminar este programa con estas expecificaciones. ventana_admin: crear un boton "cursos" para agregar curso que te pidan estos datos: costo, horario, código, cupo y nombre del catedratico el admin podra  (agregar, editar, eliminar y modificar). Cada vez que se cree un nuevo
curso deberá de ser visible automáticamente por los estudiantes def ventana_estudiante(): en la página
de asignación de cursos y el catedratico def ventana_catedratico(): podra editar los cursos. crear un codigo en python utilizando programacion a objetos. utilizando estas librerias:
import tkinter as tk
from tkinter import messagebox. el programa tiene que hacer una interfaz. las def ventana_admin,estudiante y catedratico ya los tengo solo los pongo referencia de donde quiero que esten los botones,

////////////////////////
import tkinter as tk
from tkinter import messagebox

class Curso:
    def __init__(self, costo, horario, codigo, cupo, nombre_catedratico):
        self.costo = costo # Atributo para el costo del curso
        self.horario = horario # Atributo para el horario del curso
        self.codigo = codigo # Atributo para el código del curso
        self.cupo = cupo # Atributo para el cupo del curso
        self.nombre_catedratico = nombre_catedratico # Atributo para el nombre del catedrático

    def __str__(self):
        return f"Curso: {self.codigo}\nCosto: {self.costo}\nHorario: {self.horario}\nCupo: {self.cupo}\nNombre del catedrático: {self.nombre_catedratico}" # Método para devolver una cadena con la información del curso

    def guardar(self):
        # Método para guardar la información del curso en un archivo de texto llamado base
        with open("base.txt", "a") as archivo: # Se abre el archivo en modo de escritura al final
            archivo.write(str(self) + "\n") # Se escribe la información del curso en el archivo

    def eliminar(self):
        # Método para eliminar la información del curso de un archivo de texto llamado base
        with open("base.txt", "r") as archivo: # Se abre el archivo en modo de lectura
            lineas = archivo.readlines() # Se lee el contenido del archivo como una lista de líneas

        with open("base.txt", "w") as archivo: # Se abre el archivo en modo de escritura
            for linea in lineas: # Se recorre la lista de líneas
                if self.codigo not in linea: # Se verifica que el código del curso no esté en la línea
                    archivo.write(linea) # Se escribe la línea en el archivo

def ventana_admin():
    # Función para crear la ventana del administrador
    ventana = tk.Tk() # Se crea una ventana
    ventana.title("Ventana admin") # Se le pone un título
    ventana.geometry("500x500") # Se le da un tamaño

    boton_cursos = tk.Button(ventana, text="Cursos", command=ventana_cursos) # Se crea un botón para acceder a la ventana de cursos
    boton_cursos.pack() # Se coloca el botón en la ventana

    # Aquí puedes agregar más elementos a la ventana del administrador

    ventana.mainloop() # Se ejecuta el bucle principal de la ventana

def ventana_cursos():
    # Función para crear la ventana de cursos
    ventana = tk.Toplevel() # Se crea una ventana secundaria
    ventana.title("Ventana cursos") # Se le pone un título
    ventana.geometry("500x500") # Se le da un tamaño

    etiqueta_costo = tk.Label(ventana, text="Costo:") # Se crea una etiqueta para el costo
    etiqueta_costo.grid(row=0, column=0) # Se coloca la etiqueta en la grilla

    entrada_costo = tk.Entry(ventana) # Se crea una entrada para el costo
    entrada_costo.grid(row=0, column=1) # Se coloca la entrada en la grilla

    etiqueta_horario = tk.Label(ventana, text="Horario:") # Se crea una etiqueta para el horario
    etiqueta_horario.grid(row=1, column=0) # Se coloca la etiqueta en la grilla

    entrada_horario = tk.Entry(ventana) # Se crea una entrada para el horario
    entrada_horario.grid(row=1, column=1) # Se coloca la entrada en la grilla

    etiqueta_codigo = tk.Label(ventana, text="Código:") # Se crea una etiqueta para el código
    etiqueta_codigo.grid(row=2, column=0) # Se coloca la etiqueta en la grilla

    entrada_codigo = tk.Entry(ventana) # Se crea una entrada para el código
    entrada_codigo.grid(row=2, column=1) # Se coloca la entrada en la grilla

    etiqueta_cupo = tk.Label(ventana, text="Cupo:") # Se crea una etiqueta para el cupo
    etiqueta_cupo.grid(row=3, column=0) # Se coloca la etiqueta en la grilla

    entrada_cupo = tk.Entry(ventana) # Se crea una entrada para el cupo
    entrada_cupo.grid(row=3, column=1) # Se coloca la entrada en la grilla

    etiqueta_nombre_catedratico = tk.Label(ventana, text="Nombre del catedrático:") # Se crea una etiqueta para el nombre del catedrático
    etiqueta_nombre_catedratico.grid(row=4, column=0) # Se coloca la etiqueta en la grilla

    entrada_nombre_catedratico = tk.Entry(ventana) # Se crea una entrada para el nombre del catedrático
    entrada_nombre_catedratico.grid(row=4, column=1) # Se coloca la entrada en la grilla

    boton_agregar = tk.Button(ventana, text="Agregar", command=lambda: agregar_curso(entrada_costo.get(), entrada_horario.get(), entrada_codigo.get(), entrada_cupo.get(), entrada_nombre_catedratico.get())) # Se crea un botón para agregar un curso
    boton_agregar.grid(row=5, column=0) # Se coloca el botón en la grilla

    boton_editar = tk.Button(ventana, text="Editar", command=lambda: editar_curso(entrada_costo.get(), entrada_horario.get(), entrada_codigo.get(), entrada_cupo.get(), entrada_nombre_catedratico.get())) # Se crea un botón para editar un curso
    boton_editar.grid(row=5, column=1) # Se coloca el botón en la grilla

    boton_eliminar = tk.Button(ventana, text="Eliminar", command=lambda: eliminar_curso(entrada_codigo.get())) # Se crea un botón para eliminar un curso
    boton_eliminar.grid(row=6, column=0) # Se coloca el botón en la grilla

    boton_modificar = tk.Button(ventana, text="Modificar", command=lambda: modificar_curso(entrada_costo.get(), entrada_horario.get(), entrada_codigo.get(), entrada_cupo.get(), entrada_nombre_catedratico.get())) # Se crea un botón para modificar un curso
    boton_modificar.grid(row=6, column=1) # Se coloca el botón en la grilla

def agregar_curso(costo, horario, codigo, cupo, nombre_catedratico):
    # Función para agregar un curso al archivo base.txt
    curso = Curso(costo, horario, codigo, cupo, nombre_catedratico) # Se crea un objeto de la clase Curso con los datos ingresados
    curso.guardar() # Se llama al método guardar del objeto curso
    messagebox.showinfo("Información", "Curso agregado con éxito") # Se muestra un mensaje de información

def editar_curso(costo, horario, codigo, cupo, nombre_catedratico):
    # Función para editar un curso del archivo base.txt
    curso = Curso(costo, horario, codigo, cupo, nombre_catedratico) # Se crea un objeto de la clase Curso con los datos ingresados
    curso.eliminar() # Se llama al método eliminar del objeto curso
    curso.guardar() # Se llama al método guardar del objeto curso
    messagebox.showinfo("Información", "Curso editado con éxito") # Se muestra un mensaje de información

def eliminar_curso(codigo):
    # Función para eliminar un curso del archivo base.txt
    curso = Curso("", "", codigo, "", "") # Se crea un objeto de la clase Curso con el código ingresado
    curso.eliminar() # Se llama al método eliminar del objeto curso
    messagebox.showinfo("Información", "Curso eliminado con éxito") # Se muestra un mensaje de información

def modificar_curso(costo, horario, codigo, cupo, nombre_catedratico):
    # Función para modificar un curso del archivo base.txt
    curso = Curso(costo, horario, codigo, cupo, nombre_catedratico) # Se crea un objeto de la clase Curso con los datos ingresados
    curso.eliminar() # Se llama al método eliminar del objeto curso
    curso.guardar() # Se llama al método guardar del objeto curso
    messagebox.showinfo("Información", "Curso modificado con éxito") # Se muestra un mensaje de información

# Aquí puedes agregar las funciones para las ventanas de estudiante y catedrático

# Aquí puedes llamar a la función ventana_admin para iniciar el programa

/////////////////////////////////////
import tkinter as tk
from tkinter import messagebox

class Curso:
    def __init__(self, costo, horario, codigo, cupo, nombre_catedratico):
        self.costo = costo # Atributo para el costo del curso
        self.horario = horario # Atributo para el horario del curso
        self.codigo = codigo # Atributo para el código del curso
        self.cupo = cupo # Atributo para el cupo del curso
        self.nombre_catedratico = nombre_catedratico # Atributo para el nombre del catedrático

    def __str__(self):
        return f"Curso: {self.codigo}\nCosto: {self.costo}\nHorario: {self.horario}\nCupo: {self.cupo}\nNombre del catedrático: {self.nombre_catedratico}" # Método para devolver una cadena con la información del curso

    def guardar(self):
        # Método para guardar la información del curso en un archivo de texto llamado base
        with open("Curso.txt", "a") as archivo: # Se abre el archivo en modo de escritura al final
            archivo.write(str(self) + "\n") # Se escribe la información del curso en el archivo

    def eliminar(self):
        # Método para eliminar la información del curso de un archivo de texto llamado base
        with open("Curso.txt", "r") as archivo: # Se abre el archivo en modo de lectura
            lineas = archivo.readlines() # Se lee el contenido del archivo como una lista de líneas

        with open("Curso.txt", "w") as archivo: # Se abre el archivo en modo de escritura
            for linea in lineas: # Se recorre la lista de líneas
                if self.codigo not in linea: # Se verifica que el código del curso no esté en la línea
                    archivo.write(linea) # Se escribe la línea en el archivo

def ventana_admin():
    # Función para crear la ventana del administrador
    ventana = tk.Tk() # Se crea una ventana
    ventana.title("Ventana admin") # Se le pone un título
    ventana.geometry("500x500") # Se le da un tamaño

    boton_cursos = tk.Button(ventana, text="Cursos", command=ventana_cursos) # Se crea un botón para acceder a la ventana de cursos
    boton_cursos.pack() # Se coloca el botón en la ventana

    # Aquí puedes agregar más elementos a la ventana del administrador

    ventana.mainloop() # Se ejecuta el bucle principal de la ventana

def ventana_cursos():
    # Función para crear la ventana de cursos
    ventana = tk.Toplevel() # Se crea una ventana secundaria
    ventana.title("Ventana cursos") # Se le pone un título
    ventana.geometry("500x500") # Se le da un tamaño

    etiqueta_costo = tk.Label(ventana, text="Costo:") # Se crea una etiqueta para el costo
    etiqueta_costo.grid(row=0, column=0) # Se coloca la etiqueta en la grilla

    entrada_costo = tk.Entry(ventana) # Se crea una entrada para el costo
    entrada_costo.grid(row=0, column=1) # Se coloca la entrada en la grilla

    etiqueta_horario = tk.Label(ventana, text="Horario:") # Se crea una etiqueta para el horario
    etiqueta_horario.grid(row=1, column=0) # Se coloca la etiqueta en la grilla

    entrada_horario = tk.Entry(ventana) # Se crea una entrada para el horario
    entrada_horario.grid(row=1, column=1) # Se coloca la entrada en la grilla

    etiqueta_codigo = tk.Label(ventana, text="Código:") # Se crea una etiqueta para el código
    etiqueta_codigo.grid(row=2, column=0) # Se coloca la etiqueta en la grilla

    entrada_codigo = tk.Entry(ventana) # Se crea una entrada para el código
    entrada_codigo.grid(row=2, column=1) # Se coloca la entrada en la grilla

    etiqueta_cupo = tk.Label(ventana, text="Cupo:") # Se crea una etiqueta para el cupo
    etiqueta_cupo.grid(row=3, column=0) # Se coloca la etiqueta en la grilla

    entrada_cupo = tk.Entry(ventana) # Se crea una entrada para el cupo
    entrada_cupo.grid(row=3, column=1) # Se coloca la entrada en la grilla

    etiqueta_nombre_catedratico = tk.Label(ventana, text="Nombre del catedrático:") # Se crea una etiqueta para el nombre del catedrático
    etiqueta_nombre_catedratico.grid(row=4, column=0) # Se coloca la etiqueta en la grilla

    entrada_nombre_catedratico = tk.Entry(ventana) # Se crea una entrada para el nombre del catedrático
    entrada_nombre_catedratico.grid(row=4, column=1) # Se coloca la entrada en la grilla

    boton_agregar = tk.Button(ventana, text="Agregar", command=lambda: agregar_curso(entrada_costo.get(), entrada_horario.get(), entrada_codigo.get(), entrada_cupo.get(), entrada_nombre_catedratico.get())) # Se crea un botón para agregar un curso
    boton_agregar.grid(row=5, column=0) # Se coloca el botón en la grilla

    boton_editar = tk.Button(ventana, text="Editar", command=lambda: editar_curso(entrada_costo.get(), entrada_horario.get(), entrada_codigo.get(), entrada_cupo.get(), entrada_nombre_catedratico.get())) # Se crea un botón para editar un curso
    boton_editar.grid(row=5, column=1) # Se coloca el botón en la grilla

    boton_eliminar = tk.Button(ventana, text="Eliminar", command=lambda: eliminar_curso(entrada_codigo.get())) # Se crea un botón para eliminar un curso
    boton_eliminar.grid(row=6, column=0) # Se coloca el botón en la grilla

    boton_modificar = tk.Button(ventana, text="Modificar", command=lambda: modificar_curso(entrada_costo.get(), entrada_horario.get(), entrada_codigo.get(), entrada_cupo.get(), entrada_nombre_catedratico.get())) # Se crea un botón para modificar un curso
    boton_modificar.grid(row=6, column=1) # Se coloca el botón en la grilla

    lista_cursos = tk.Listbox(ventana) # Se crea una lista para mostrar los cursos
    lista_cursos.grid(row=7, columnspan=2) # Se coloca la lista en la grilla

    with open("base.txt", "r") as archivo: # Se abre el archivo en modo de lectura
        lineas = archivo.readlines() # Se lee el contenido del archivo como una lista de líneas

    for linea in lineas: # Se recorre la lista de líneas
        if entrada_nombre_catedratico.get() in linea: # Se verifica que el nombre del catedrático esté en la línea
            lista_cursos.insert(tk.END, linea) # Se inserta la línea en la lista de cursos

def ventana_estudiante():
    # Función para crear la ventana de estudiante
    ventana = tk.Toplevel() # Se crea una ventana secundaria
    ventana.title("Ventana estudiante") # Se le pone un título
    ventana.geometry("500x500") # Se le da un tamaño

    lista_cursos = tk.Listbox(ventana) # Se crea una lista para mostrar los cursos
    lista_cursos.pack() # Se coloca la lista en la ventana

    with open("base.txt", "r") as archivo: # Se abre el archivo en modo de lectura
        lineas = archivo.readlines() # Se lee el contenido del archivo como una lista de líneas

    for linea in lineas: # Se recorre la lista de líneas
        lista_cursos.insert(tk.END, linea) # Se inserta la línea en la lista de cursos

def ventana_catedratico():
    # Función para crear la ventana de catedrático
    ventana = tk.Toplevel() # Se crea una ventana secundaria
    ventana.title("Ventana catedrático") # Se le pone un título
    ventana.geometry("500x500") # Se le da un tamaño

    etiqueta_nombre = tk.Label(ventana, text="Nombre:") # Se crea una etiqueta para el nombre
    etiqueta_nombre.grid(row=0, column=0) # Se coloca la etiqueta en la grilla

    entrada_nombre = tk.Entry(ventana) # Se crea una entrada para el nombre
    entrada_nombre.grid(row=0, column=1) # Se coloca