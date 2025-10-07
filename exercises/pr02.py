hardcoded_schedules = {
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
        option = input("Choose an option (1-3): ").strip()

        match option:
            case '1':
                showRegisters()
            case '2':
                countEntries()
            case '3':
                print("Exiting the program.")
                break
            case _:
                print("Invalid option. Please try again.\n")

def showRegisters():
    print("\nEmployee Schedules:")
    
    for name, (in_hour, out_hour) in hardcoded_schedules.items():
        if (validateHour(in_hour) and validateHour(out_hour)):
            print(f"{name}: Entry at {in_hour}, Exit at {out_hour}")
        else:
            print(f"{name}: Invalid schedule ({in_hour} - {out_hour})");

def countEntries():
        name = input("Introduce the employee's name: ")
        
        while True:
            in_hour = input("Introduce the check-in hour (HH:MM): ")
            
            if (validateHour(in_hour)):
                break;
            else:
                print("Invalid hour. Please, try again.")
        
        while True:
            out_hour = input("Introduce the check-out hour (HH:MM): ")
            
            if (validateHour(out_hour) and to_minutes(out_hour) > to_minutes(in_hour)):
                break;
            else:
                print("Invalid hour. It must be a valid hour and later than the check-in time. Please, try again.")
        
        hardcoded_schedules[name] = (in_hour, out_hour)
        
        if(validateHour(in_hour) and validateHour(out_hour)):
            print(f"\nTotal employee entries: {len(hardcoded_schedules)}")

def to_minutes(hour: str) -> int:
    h, m = map(int, hour.split(':'))
    return h * 60 + m

def validateHour(hour: str) -> bool:
    try:
        h, m = map(int, hour.split(':'))
        if 0 <= h < 24 and 0 <= m < 60:
            return True
        else:
            return False
    except ValueError:
        return False

# ---------------------------------------------------------------------------
# 4) Punto de entrada
# ---------------------------------------------------------------------------
if __name__ == '__main__':
    # Consejo de depuración: descomenta las dos líneas siguientes para pausar en este punto
    # import debugpy
    # debugpy.breakpoint()
    menu()