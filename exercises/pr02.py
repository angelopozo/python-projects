schedules = {
    'María':  ('08:32', '16:12'),
    'Juan':   ('09:59', '17:44'),
    'Lucía':  ('07:10', '15:25'),
    'Diego':  ('10:15', '18:05'),
    'Ana':    ('08:50', '14:38'),
    'Raúl':   ('12:03', '20:22'),
    'Sofía':  ('11:06', '19:47'),
    'Carlos': ('06:09', '14:11'),
    'Elena':  ('13:29', '21:37'),
    'Luis':   ('09:12', '17:13'),
    'Marta':  ('10:47', '18:55'),
    'Javier': ('08:08', '16:30'),
    'Carmen': ('07:45', '15:50'),
    'Pedro':  ('12:20', '20:15'),
    'Laura':  ('11:35', '19:05'),
    'Sergio': ('06:34', '14:47'),
    'Isabel': ('13:22', '21:09'),
    'Alberto':('09:37', '17:24'),
    'Nuria':  ('10:40', '18:11'),
}


def menu():
    """
    Menú principal repetitivo (bucle while) para elegir acciones:
    1) Mostrar registros
    2) Contar entradas
    3) Salir
    """
    while True:
        print("========== MENÚ ==========")
        print("1) Show registers")
        print("2) Count entries")
        print("3) Exit")
        opcion = input("Choose an option (1-3): ").strip()

        if opcion == '1':
            showRegisters()
        elif opcion == '2':
            countEntries()
        elif opcion == '3':
            print("Exiting the program.")
            break
        else:
            print("Invalid option. Please try again.\n")


def showRegisters():
    print("\nEmployee Schedules:")
    
    for name, (in_hour, out_hour) in schedules.items():
        if (validateHour(in_hour) and validateHour(out_hour)):
            print(f"{name}: Entry at {in_hour}, Exit at {out_hour}")
            
def countEntries():
    print(f"\nTotal employee entries: {len(schedules)}")


def validateHour(hour):
    try:
        h, m = map(int, hour.split(':'))
        if 0 <= h < 24 and 0 <= m < 60:
            return True
        else:
            return False
    except:
        return False
# ---------------------------------------------------------------------------
# 4) Punto de entrada
# ---------------------------------------------------------------------------
if __name__ == '__main__':
    # Consejo de depuración: descomenta las dos líneas siguientes para pausar en este punto
    # import debugpy
    # debugpy.breakpoint()
    menu()