class Vehiculo:

    # Se crean los atributos del objeto
    def __init__(self, matricula, modelo):
        self.matricula = matricula
        self.modelo = modelo
        self.disponible = True

    # Se verifica si el vehiculo puede ser alquilado
    def alquilar(self):
        if self.disponible:
            self.disponible = False # Marca como alquilado el vehiculo
    
    # Se verifica si el vehiculo puede ser devuelto
    def devolver(self):
        if not self.disponible:
            self.disponible = True # Marca el vehiculo como devuelto

    # Metodo el cual devuelve como cadena y muestra por pantalla el valor del objeto
    def __str__(self):
        return f"Vehiculo (Matricula: {self.matricula}, Modelo: {self.modelo}, disponible: {self.disponible})"
    
class Concesionaria:

    # Se crea una lista la cual contendra los vehiculos
    def __init__(self):
        self.vehiculos = []

    # Metodo para agregar un vehiculo a la lista antes definida por el constructor
    def agregar_vehiculo(self, vehiculo):
        self.vehiculos.append(vehiculo)

    # Metodo el cual verifica si la matricula existe dentro de la concesionaria
    def alquilar_vehiculo(self, matricula):
        for vehiculo in self.vehiculos:
            if vehiculo.matricula == matricula:
                vehiculo.alquilar()

    # Metodo el cual verifica si la matricula existe dentro de la concesionaria
    def devolver_vehiculo(self, matricula):
        for vehiculo in self.vehiculos:
            if vehiculo.matricula == matricula:
                vehiculo.devolver()

    # Metodo el cual devuelve como cadena y muestra por pantalla los vehiculos de la concesionaria
    def __str__(self):
        return "\n".join(str(vehiculo) for vehiculo in self.vehiculos)
    

# Se ejecuta el programa
if __name__ == '__main__':

    ok = True
    concesionaria = Concesionaria()
    while ok:

        # El usuario debe elegir una opcion para continuar con el programa
        print("\nElija una opcion: ")
        print("\n1. Agregar vehiculo a la concesionaria.")
        print("\n2. Marcar un vehiculo como alquilado.")
        print("\n3. Devolver un vehiculo de un cliente a la concesionaria.")
        print("\n4. Salir del programa.")
        opcion = int(input(": "))

        # Esta opcion agrega un vehiculo a la concesionaria
        if opcion == 1:
            matricula = input("\nIngrese la matricula del vehiculo: ")
            modelo = input("Ingrese el modelo del vehiculo: ")
            concesionaria.agregar_vehiculo(Vehiculo(matricula, modelo))
            with open("vehiculosagregados.txt", "a") as f:
                f.write(f"Vehiculo (Matricula: {matricula}, Modelo: {modelo})\n")
        
        # Esta opcion marca un vehiculo como alquilado y lo arega a un archivo de vehiculos alquilados
        elif opcion == 2:
            matricula = input("Ingrese la matricula del vehiculo: ")
            encontrado = False
            for vehiculo in concesionaria.vehiculos:
                if matricula == vehiculo.matricula:
                    encontrado = True
                    if vehiculo.disponible:
                        vehiculo.alquilar()
                        with open("vehiculosalquilados.txt", "a") as f:
                            f.write(f"Vehiculo (Matricula: {matricula})\n")
                    else:
                        print("El vehículo ya está alquilado.")
                    break
            if not encontrado:
                print("La matrícula ingresada no existe dentro del sistema.")

        # Esta opcion devuelve un vehiculo de un cliente a la concesionaria y lo agrega a un archivo de vehiculos devueltos
        elif opcion == 3:
            matricula = input("Ingrese la matricula del vehiculo: ")
            encontrado = False
            for vehiculo in concesionaria.vehiculos:
                if matricula == vehiculo.matricula:
                    encontrado = True
                    if not vehiculo.disponible:
                        vehiculo.devolver()
                        with open("vehiculosdevueltos.txt", "a") as f:
                            f.write(f"Vehiculo (Matricula: {matricula})\n")
                    else:
                        print("El vehículo ya está disponible. No se puede devolver.")
                    break
            if not encontrado:
                print("La matrícula ingresada no existe dentro del sistema.")

        # Esta opcion finaliza el programa
        elif opcion == 4:
            print("!Saliendo del programa.")
            ok = False

        else:
            print("Error, no ingreso una opcion correcta")
    
    # Se agrega un resumen del programa de los vehiculos agregados y alquilados dentro de un archivo de la concesionaria
    with open("concesionaria.txt", "a") as f:
        f.write(str(concesionaria) + "\n")

    print(concesionaria)