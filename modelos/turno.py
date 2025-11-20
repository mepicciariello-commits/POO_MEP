
class Turno:
    def __init__(self, id_turno, cliente, servicio, fecha_hora, estado="ACTIVO"):
        self.id_turno = id_turno
        self.cliente = cliente
        self.servicio = servicio
        self.fecha_hora = fecha_hora
        self.estado = estado

    def __str__(self):
        return f"Turno {self.id_turno} - {self.servicio} - {self.fecha_hora} - Cliente: {self.cliente.nombre} {self.cliente.apellido} - Estado: {self.estado}"
