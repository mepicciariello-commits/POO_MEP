from modelos.cliente import Cliente
from modelos.turno import Turno


class GestorTurnos:
    def __init__(self, archivo_csv):
        self.archivo_csv = archivo_csv
        self.clientes = {}
        self.turnos = {}
        self.ultimo_id_turno = 0
        self.cargar_desde_csv()

    def registrar_cliente(self, dni, nombre, apellido, telefono, email):
        if dni in self.clientes:
            return None, "El cliente ya existe en el sistema."
        nuevo = Cliente(dni, nombre, apellido, telefono, email)
        self.clientes[dni] = nuevo
        return nuevo, ""

    def obtener_cliente(self, dni):
        if dni in self.clientes:
            return self.clientes[dni]
        return None

    def existe_turno_mismo_horario(self, servicio, fecha_hora):
        ids = list(self.turnos.keys())
        i = 0
        while i < len(ids):
            turno = self.turnos[ids[i]]
            if turno.servicio == servicio and turno.fecha_hora == fecha_hora and turno.estado == "ACTIVO":
                return True
            i = i + 1
        return False

    def registrar_turno(self, dni, servicio, fecha_hora):
        cliente = self.obtener_cliente(dni)
        if cliente is None:
            return None, "El cliente no está registrado."
        if self.existe_turno_mismo_horario(servicio, fecha_hora):
            return None, "Ya existe un turno activo en ese horario para ese servicio."
        self.ultimo_id_turno = self.ultimo_id_turno + 1
        turno = Turno(self.ultimo_id_turno, cliente, servicio, fecha_hora)
        self.turnos[self.ultimo_id_turno] = turno
        self.guardar_en_csv()
        return turno, ""

    def listar_turnos(self):
        return list(self.turnos.values())

    def obtener_turno(self, id_turno):
        if id_turno in self.turnos:
            return self.turnos[id_turno]
        return None

    def modificar_turno(self, id_turno, nuevo_servicio, nueva_fecha_hora):
        turno = self.obtener_turno(id_turno)
        if turno is None:
            return "El turno no existe."
        if self.existe_turno_mismo_horario(nuevo_servicio, nueva_fecha_hora):
            return "Ya existe un turno activo en ese horario para ese servicio."
        turno.servicio = nuevo_servicio
        turno.fecha_hora = nueva_fecha_hora
        self.guardar_en_csv()
        return ""

    def cancelar_turno(self, id_turno):
        turno = self.obtener_turno(id_turno)
        if turno is None:
            return "El turno no existe."
        turno.estado = "CANCELADO"
        self.guardar_en_csv()
        return ""

    def turnos_por_cliente(self, dni):
        resultado = []
        ids = list(self.turnos.keys())
        i = 0
        while i < len(ids):
            turno = self.turnos[ids[i]]
            if turno.cliente.dni == dni:
                resultado.append(turno)
            i = i + 1
        return resultado

    def turnos_por_fecha(self, fecha_texto):
        resultado = []
        ids = list(self.turnos.keys())
        i = 0
        while i < len(ids):
            turno = self.turnos[ids[i]]
            if fecha_texto in turno.fecha_hora:
                resultado.append(turno)
            i = i + 1
        return resultado

    def guardar_en_csv(self):
        try:
            archivo = open(self.archivo_csv, "w", encoding="utf-8")
            encabezado = "id_turno,dni,nombre,apellido,telefono,email,servicio,fecha_hora,estado\n"
            archivo.write(encabezado)
            ids = list(self.turnos.keys())
            i = 0
            while i < len(ids):
                turno = self.turnos[ids[i]]
                cliente = turno.cliente
                linea = (
                    str(turno.id_turno)
                    + "," + cliente.dni
                    + "," + cliente.nombre
                    + "," + cliente.apellido
                    + "," + cliente.telefono
                    + "," + cliente.email
                    + "," + turno.servicio
                    + "," + turno.fecha_hora
                    + "," + turno.estado
                    + "\n"
                )
                archivo.write(linea)
                i = i + 1
            archivo.close()
        except Exception:
            pass

    def cargar_desde_csv(self):
        self.turnos = {}
        self.clientes = {}
        self.ultimo_id_turno = 0
        try:
            archivo = open(self.archivo_csv, "r", encoding="utf-8")
            lineas = archivo.readlines()
            archivo.close()
            i = 1
            while i < len(lineas):
                linea = lineas[i].strip()
                if linea != "":
                    partes = linea.split(",")
                    if len(partes) >= 9:
                        id_turno = int(partes[0])
                        dni = partes[1]
                        nombre = partes[2]
                        apellido = partes[3]
                        telefono = partes[4]
                        email = partes[5]
                        servicio = partes[6]
                        fecha_hora = partes[7]
                        estado = partes[8]
                        if dni in self.clientes:
                            cliente = self.clientes[dni]
                        else:
                            cliente = Cliente(dni, nombre, apellido, telefono, email)
                            self.clientes[dni] = cliente
                        turno = Turno(id_turno, cliente, servicio, fecha_hora, estado)
                        self.turnos[id_turno] = turno
                        if id_turno > self.ultimo_id_turno:
                            self.ultimo_id_turno = id_turno
                i = i + 1
        except FileNotFoundError:
            self.turnos = {}
            self.clientes = {}
            self.ultimo_id_turno = 0
        except Exception:
            self.turnos = {}
            self.clientes = {}
            self.ultimo_id_turno = 0
