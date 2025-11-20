from modelos.gestor_turnos import GestorTurnos


def mostrar_menu():
    print("")
    print("=== Sistema de Turnos - Peluquería ===")
    print("1. Registrar nuevo cliente")
    print("2. Solicitar turno")
    print("3. Listar turnos existentes")
    print("4. Modificar turno")
    print("5. Cancelar turno")
    print("6. Guardar datos en CSV / Recargar desde CSV")
    print("7. Filtrar turnos por cliente")
    print("8. Filtrar turnos por fecha")
    print("9. Salir")


def main():
    gestor = GestorTurnos("datos/turnos.csv")
    opcion = ""
    while opcion != "9":
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print("")
            print("--- Registrar nuevo cliente ---")
            dni = input("DNI: ")
            nombre = input("Nombre: ")
            apellido = input("Apellido: ")
            telefono = input("Teléfono: ")
            email = input("Email: ")
            cliente, error = gestor.registrar_cliente(dni, nombre, apellido, telefono, email)
            if error != "":
                print(error)
            else:
                print("Cliente registrado:")
                print(cliente)

        elif opcion == "2":
            print("")
            print("--- Solicitar turno ---")
            dni = input("DNI del cliente: ")
            servicio = input("Servicio: ")
            fecha_hora = input("Fecha y hora (ej: 2025-11-20 15:30): ")
            turno, error = gestor.registrar_turno(dni, servicio, fecha_hora)
            if error != "":
                print("No se pudo registrar el turno:")
                print(error)
            else:
                print("Turno registrado:")
                print(turno)

        elif opcion == "3":
            print("")
            print("--- Listado de turnos ---")
            turnos = gestor.listar_turnos()
            if len(turnos) == 0:
                print("No hay turnos cargados.")
            else:
                i = 0
                while i < len(turnos):
                    print(turnos[i])
                    i = i + 1

        elif opcion == "4":
            print("")
            print("--- Modificar turno ---")
            id_texto = input("ID de turno: ")
            try:
                id_turno = int(id_texto)
            except ValueError:
                print("ID inválido.")
                continue
            nuevo_servicio = input("Nuevo servicio: ")
            nueva_fecha = input("Nueva fecha y hora: ")
            error = gestor.modificar_turno(id_turno, nuevo_servicio, nueva_fecha)
            if error != "":
                print("No se pudo modificar el turno:")
                print(error)
            else:
                print("Turno modificado correctamente.")

        elif opcion == "5":
            print("")
            print("--- Cancelar turno ---")
            id_texto = input("ID de turno: ")
            try:
                id_turno = int(id_texto)
            except ValueError:
                print("ID inválido.")
                continue
            error = gestor.cancelar_turno(id_turno)
            if error != "":
                print("No se pudo cancelar el turno:")
                print(error)
            else:
                print("Turno cancelado correctamente.")

        elif opcion == "6":
            print("")
            print("1. Guardar dict actual en CSV")
            print("2. Recargar desde CSV")
            sub = input("Elija opción: ")
            if sub == "1":
                gestor.guardar_en_csv()
                print("Datos guardados en CSV.")
            elif sub == "2":
                gestor.cargar_desde_csv()
                print("Datos recargados desde CSV.")
            else:
                print("Opción inválida.")

        elif opcion == "7":
            print("")
            print("--- Filtrar turnos por cliente (DNI) ---")
            dni = input("DNI del cliente: ")
            turnos = gestor.turnos_por_cliente(dni)
            if len(turnos) == 0:
                print("No hay turnos para ese cliente.")
            else:
                i = 0
                while i < len(turnos):
                    print(turnos[i])
                    i = i + 1

        elif opcion == "8":
            print("")
            print("--- Filtrar turnos por fecha ---")
            fecha = input("Ingrese parte de la fecha: ")
            turnos = gestor.turnos_por_fecha(fecha)
            if len(turnos) == 0:
                print("No hay turnos para esa fecha.")
            else:
                i = 0
                while i < len(turnos):
                    print(turnos[i])
                    i = i + 1

        elif opcion == "9":
            print("Saliendo del sistema...")
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    main()
