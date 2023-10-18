import tkinter as tk


class Curso:
    def __init__(self, costo, horario, codigo, cupo, nombre_catedratico):
        self.costo = costo 
        self.horario = horario 
        self.codigo = codigo 
        self.cupo = cupo 
        self.nombre_catedratico = nombre_catedratico 

    def str(self):
        return f"Curso: {self.codigo}\nCosto: {self.costo}\nHorario: {self.horario}\nCupo: {self.cupo}\nNombre del catedrático: {self.nombre_catedratico}" 
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

    ventana_cur= tk.Toplevel() 
    ventana_cur.title("Ventana Cursos") 
    ventana_cur.geometry("500x500")

    # Creamos las etiquetas y las entradas para los datos de los cursos y las colocamos en la grilla
    etiqueta_costo = tk.Label(ventana_cur, text="Costo:") 
    etiqueta_costo.grid(row=0, column=0)
    entrada_costo = tk.Entry(ventana_cur) 
    entrada_costo.grid(row=0, column=1)

    etiqueta_horario = tk.Label(ventana_cur, text="Horario:") 
    etiqueta_horario.grid(row=1, column=0) 
    entrada_horario = tk.Entry(ventana_cur) 
    entrada_horario.grid(row=1, column=1)

    etiqueta_codigo = tk.Label(ventana_cur, text="Código:") 
    etiqueta_codigo.grid(row=2, column=0) 
    entrada_codigo = tk.Entry(ventana_cur) 
    entrada_codigo.grid(row=2, column=1)

    etiqueta_cupo = tk.Label(ventana_cur, text="Cupo:") 
    etiqueta_cupo.grid(row=3, column=0) 
    entrada_cupo = tk.Entry(ventana_cur)
    entrada_cupo.grid(row=3, column=1)

    etiqueta_nombre_catedratico = tk.Label(ventana_cur, text="Nombre del catedrático:") 
    etiqueta_nombre_catedratico.grid(row=4, column=0) 
    entrada_nombre_catedratico = tk.Entry(ventana_cur)
    entrada_nombre_catedratico.grid(row=4, column=1) 

    # Creamos los botones para agregar, editar, eliminar y modificar los cursos y les asignamos los comandos correspondientes a los métodos de la clase Curso
    # Para pasar los valores de las entradas a los métodos usamos el método get y la función lambda
    boton_agregar = tk.Button(ventana_cur, text="Agregar", command=lambda: curso.agregar(entrada_costo.get(), entrada_horario.get(), entrada_codigo.get(), entrada_cupo.get(), entrada_nombre_catedratico.get())) 
    boton_agregar.grid(row=5, column=0)

    boton_editar = tk.Button(ventana_cur, text="Editar", command=lambda: curso.editar(entrada_costo.get(), entrada_horario.get(), entrada_codigo.get(), entrada_cupo.get(), entrada_nombre_catedratico.get())) 
    boton_editar.grid(row=5, column=1) 

    boton_eliminar = tk.Button(ventana_cur, text="Eliminar", command=lambda: curso.eliminar(entrada_codigo.get()))
    boton_eliminar.grid(row=6, column=0) 


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
    

ventana_adm = tk.Tk()
ventana_adm.title("Administración")
ventana_adm.geometry("1000x600")


boton_cursos = tk.Button(ventana_adm, text="Cursos", command=ventana_cursos)
boton_cursos.pack()

curso = Curso(0, "", "", 0, "")


ventana_adm.mainloop()
