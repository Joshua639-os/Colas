class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self._size = 0

    def enqueue(self, element):
        new_node = Node(element)
        if self.rear is None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        self._size += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("La cola está vacía")
        temp = self.front
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        self._size -= 1
        return temp.value

    def front_value(self):
        if self.is_empty():
            raise IndexError("La cola está vacía")
        return self.front.value

    def is_empty(self):
        return self.front is None

    def size(self):
        return self._size


# Aplicación 1: Sistema de Gestión de Tareas
class TaskManager:
    def __init__(self):
        self.high_priority = Queue()
        self.normal_priority = Queue()

    def add_task(self, task, priority='normal'):
        if priority == 'high':
            self.high_priority.enqueue(task)
        else:
            self.normal_priority.enqueue(task)

    def process_task(self):
        if not self.high_priority.is_empty():
            return self.high_priority.dequeue()
        elif not self.normal_priority.is_empty():
            return self.normal_priority.dequeue()
        else:
            return "No hay tareas pendientes"


# Aplicación 2: Simulación de atención al cliente
class CustomerService:
    def __init__(self):
        self.vip_queue = Queue()
        self.regular_queue = Queue()

    def add_customer(self, customer, type='regular'):
        if type == 'VIP':
            self.vip_queue.enqueue(customer)
        else:
            self.regular_queue.enqueue(customer)

    def attend_customer(self):
        if not self.vip_queue.is_empty():
            return f"Atendiendo a cliente VIP: {self.vip_queue.dequeue()}"
        elif not self.regular_queue.is_empty():
            return f"Atendiendo a cliente Regular: {self.regular_queue.dequeue()}"
        else:
            return "No hay clientes en espera"

# Prueba del sistema de gestión de tareas
print("=== Gestión de Tareas ===")
task_manager = TaskManager()
task_manager.add_task("Revisión de servidor", "high")
task_manager.add_task("Enviar reportes", "normal")
task_manager.add_task("Actualizar base de datos", "high")

print(task_manager.process_task())  # Debería atender "Revisión de servidor"
print(task_manager.process_task())  # Debería atender "Actualizar base de datos"
print(task_manager.process_task())  # Debería atender "Enviar reportes"

# Prueba del sistema de atención al cliente
print("\n=== Atención al Cliente ===")
customer_service = CustomerService()
customer_service.add_customer("Cliente 1", "regular")
customer_service.add_customer("Cliente 2", "VIP")
customer_service.add_customer("Cliente 3", "regular")

print(customer_service.attend_customer())  # Debería atender a "Cliente 2" (VIP)
print(customer_service.attend_customer())  # Debería atender a "Cliente 1"
print(customer_service.attend_customer())  # Debería atender a "Cliente 3"
print(customer_service.attend_customer())  # No hay clientes en espera
