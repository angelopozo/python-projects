import os, json

def menu():
    if not os.path.exists('data/pr02.json'):
        with open('data/pr02.json', 'w', encoding='utf-8') as f:
            json.dump({}, f, ensure_ascii=False, indent=4)

    with open('data/pr02.json', 'r', encoding='utf-8') as f:
        schedules = json.load(f) 

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
                showRegisters(schedules)
            case '2':
                countEntries(schedules)
            case '3':
                print("Exiting the program.")
                break
            case _:
                print("Invalid option. Please try again.\n")

def showRegisters(schedules: dict):
    print("\nEmployee Schedules:")
    for name, (in_hour, out_hour) in schedules.items():
        if validateHour(in_hour) and validateHour(out_hour):
            print(f"{name}: Entry at {in_hour}, Exit at {out_hour}")
        else:
            print(f"{name}: Invalid schedule ({in_hour} - {out_hour})")

def countEntries(schedules: dict):
    name = input("Introduce the employee's name: ")

    while True:
        in_hour = input("Introduce the check-in hour (HH:MM): ")
        if validateHour(in_hour):
            break
        else:
            print("Invalid hour. It must be a valid hour. Please, try again.")

    while True:
        out_hour = input("Introduce the check-out hour (HH:MM): ")
        if validateHour(out_hour) and to_minutes(out_hour) > to_minutes(in_hour):
            break
        else:
            print("Invalid hour. It must be a valid hour and later than the check-in time. Please, try again.")

    schedules[name] = [in_hour, out_hour]
    
    with open('data/pr02.json', 'w', encoding='utf-8') as f:
        json.dump(schedules, f, ensure_ascii=False, indent=4)

    print(f"\nTotal employee entries: {len(schedules)}")

def to_minutes(hour: str) -> int:
    h, m = map(int, hour.split(':'))
    return h * 60 + m

def validateHour(hour: str) -> bool:
    try:
        h, m = map(int, hour.split(':'))
        return 0 <= h < 24 and 0 <= m < 60
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