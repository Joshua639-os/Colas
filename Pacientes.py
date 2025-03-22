from queue import Queue


class GestorPacientes:
    def __init__(self):
        self.critica = Queue()
        self.alta = Queue()
        self.baja = Queue()

    def agregar_paciente(self, nombre, gravedad):
        if gravedad == "critica":
            self.critica.put(nombre)
        elif gravedad == "alta":
            self.alta.put(nombre)
        elif gravedad == "baja":
            self.baja.put(nombre)
        else:
            print("Gravedad no válida. Use: critica, alta o baja.")

    def atender_paciente(self):
        if not self.critica.empty():
            return f"Atendiendo paciente crítico: {self.critica.get()}"
        elif not self.alta.empty():
            return f"Atendiendo paciente de gravedad: {self.alta.get()}"
        elif not self.baja.empty():
            return f"Atendiendo paciente de baja: {self.baja.get()}"
        else:
            return "No hay pacientes en espera."

    def mostrar_pacientes(self):
        return {
            "Critica": list(self.critica.queue),
            "Alta": list(self.alta.queue),
            "Baja": list(self.baja.queue)
        }


gestor = GestorPacientes()
gestor.agregar_paciente("Ana", "critica")
gestor.agregar_paciente("Luis", "baja")
gestor.agregar_paciente("Pedro", "alta")
gestor.agregar_paciente("Maria", "critica")

tipo_pacientes = gestor.mostrar_pacientes()
print("Pacientes en espera:", tipo_pacientes)

print(gestor.atender_paciente())
print(gestor.atender_paciente())
print(gestor.atender_paciente())
print(gestor.atender_paciente())
print(gestor.atender_paciente())
