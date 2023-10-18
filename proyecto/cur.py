# Importamos la librería Tkinter
from tkinter import *

# Creamos una clase para la ventana principal
class Principal:
    # Inicializamos la ventana con el constructor
    def __init__(self):
        # Creamos una instancia de Tk
        self.raiz = Tk()
        # Le ponemos un título a la ventana
        self.raiz.title("Ventana principal")
        # Creamos tres botones para acceder a las ventanas de admin, estudiante y profesor
        self.boton_admin = Button(self.raiz, text="Admin", command=self.abrir_admin)
        self.boton_admin.pack(side="left")
        self.boton_estudiante = Button(self.raiz, text="Estudiante", command=self.abrir_estudiante)
        self.boton_estudiante.pack(side="left")
        self.boton_profesor = Button(self.raiz, text="Profesor", command=self.abrir_profesor)
        self.boton_profesor.pack(side="left")
        # Iniciamos el bucle principal de la ventana
        self.raiz.mainloop()

    # Definimos un método para abrir la ventana del administrador
    def abrir_admin(self):
        # Creamos una nueva ventana con Toplevel
        self.admin = Toplevel(self.raiz)
        # Creamos una instancia de la clase Admin y le pasamos la nueva ventana como argumento
        self.ventana_admin = Admin(master=self.admin)

    # Definimos un método para abrir la ventana del estudiante
    def abrir_estudiante(self):
        # Creamos una nueva ventana con Toplevel
        self.estudiante = Toplevel(self.raiz)
        # Creamos una instancia de la clase Estudiante y le pasamos la nueva ventana como argumento
        self.ventana_estudiante = Estudiante(master=self.estudiante)

    # Definimos un método para abrir la ventana del profesor
    def abrir_profesor(self):
        # Creamos una nueva ventana con Toplevel
        self.profesor = Toplevel(self.raiz)
        # Creamos una instancia de la clase Profesor y le pasamos la nueva ventana como argumento
        self.ventana_profesor = Profesor(master=self.profesor)

# Creamos una clase para la ventana del administrador
class Admin:
    # Inicializamos la ventana con el constructor
    def __init__(self, master=None):
        # Creamos un frame dentro de la ventana
        self.frame = Frame(master)
        # Colocamos el frame en la ventana
        self.frame.pack()
        # Le ponemos un título a la ventana
        master.title("Ventana del administrador")
        # Creamos un botón para crear cursos
        self.boton_crear = Button(self.frame, text="Crear curso", command=self.crear_curso)
        # Colocamos el botón en el frame
        self.boton_crear.pack()

    # Definimos un método para crear cursos
    def crear_curso(self):
        # Creamos una nueva ventana con Toplevel
        self.nueva = Toplevel(self.frame)
        # Le ponemos un título a la nueva ventana
        self.nueva.title("Crear curso")
        # Creamos las etiquetas y las entradas de texto para los datos del curso
        self.etiqueta_costo = Label(self.nueva, text="Costo:")
        self.etiqueta_costo.grid(row=0, column=0)
        self.entrada_costo = Entry(self.nueva)
        self.entrada_costo.grid(row=0, column=1)
        self.etiqueta_horario = Label(self.nueva, text="Horario:")
        self.etiqueta_horario.grid(row=1, column=0)
        self.entrada_horario = Entry(self.nueva)
        self.entrada_horario.grid(row=1, column=1)
        self.etiqueta_codigo = Label(self.nueva, text="Código:")
        self.etiqueta_codigo.grid(row=2, column=0)
        self.entrada_codigo = Entry(self.nueva)
        self.entrada_codigo.grid(row=2, column=1)
        self.etiqueta_cupo = Label(self.nueva, text="Cupo:")
        self.etiqueta_cupo.grid(row=3, column=0)
        self.entrada_cupo = Entry(self.nueva)
        self.entrada_cupo.grid(row=3, column=1)
        self.etiqueta_catedratico = Label(self.nueva, text="Catedrático:")
        self.etiqueta_catedratico.grid(row=4, column=0)
        self.entrada_catedratico = Entry(self.nueva)
        self.entrada_catedratico.grid(row=4, column=1)

        # Creamos los botones para guardar o cancelar el curso
        self.boton_guardar = Button(self.nueva, text="Guardar", fg="green", command=self.guardar_curso)
        self.boton_guardar.grid(row=5, column=0)
        self.boton_cancelar = Button(self.nueva, text="Cancelar", fg="red", command=self.nueva.destroy)
        self.boton_cancelar.grid(row=5, column=1)

    # Definimos un método para guardar el curso en el archivo de texto
    def guardar_curso(self):
        # Obtenemos los valores de las entradas de texto
        costo = self.entrada_costo.get()
        horario = self.entrada_horario.get()
        codigo = self.entrada_codigo.get()
        cupo = self.entrada_cupo.get()
        catedratico = self.entrada_catedratico.get()
        # Abrimos el archivo de texto en modo de escritura al final (append)
        with open("Materia.txt", "a") as archivo:
            # Escribimos los datos del curso en el archivo separados por comas
            archivo.write(f"{costo},{horario},{codigo},{cupo},{catedratico}\n")
        # Cerramos la ventana de crear curso
        self.nueva.destroy()

# Creamos una clase para la ventana del estudiante
class Estudiante:
    # Inicializamos la ventana con el constructor
    def __init__(self, master=None):
        # Creamos un frame dentro de la ventana
        self.frame = Frame(master)
        # Colocamos el frame en la ventana
        self.frame.pack()
        # Le ponemos un título a la ventana
        master.title("Ventana del estudiante")
        # Creamos una lista vacía para guardar los cursos
        self.cursos = []
        # Llamamos al método para leer los cursos del archivo de texto
        self.leer_cursos()
        
         # Creamos una etiqueta para mostrar el título de la página
        if len(self.cursos) > 0:
            # Si hay cursos disponibles, mostramos el título "Cursos disponibles"
            self.etiqueta_titulo = Label(self.frame, text="Cursos disponibles")
        else:
            # Si no hay cursos disponibles, mostramos el título "No hay cursos disponibles"
            self.etiqueta_titulo = Label(self.frame, text="No hay cursos disponibles")
         # Colocamos la etiqueta en el frame
            self.etiqueta_titulo.pack()

         # Creamos un bucle for para mostrar los datos de cada curso en el frame
        for curso in self.cursos:
             # Creamos una etiqueta con el formato: Código - Horario - Costo - Cupo - Catedrático
             self.etiqueta_curso = Label(self.frame, text=f"{curso[2]}