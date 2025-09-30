schedules = {
    'María':  ('08', '16'),
    'Juan':   ('09', '17'),
    'Lucía':  ('07', '15'),
    'Diego':  ('10', '18'),
    'Ana':    ('08', '14'),
    'Raúl':   ('12', '20'),
    'Sofía':  ('11', '19'),
    'Carlos': ('06', '14'),
    'Elena':  ('13', '21'),
    'Luis':   ('09', '17'),
    'Marta':  ('10', '18'),
    'Javier': ('08', '16'),
    'Carmen': ('07', '15'),
    'Pedro':  ('12', '20'),
    'Laura':  ('11', '19'),
    'Sergio': ('06', '14'),
    'Isabel': ('13', '21'),
    'Alberto':('09', '17'),
    'Nuria':  ('10', '18'),
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
        print(f"{name}: Entry at {in_hour}:00, Exit at {out_hour}:00")
        
def countEntries():
    print(f"\nTotal employee entries: {len(schedules)}")

# ---------------------------------------------------------------------------
# 4) Punto de entrada
# ---------------------------------------------------------------------------
if __name__ == '__main__':
    # Consejo de depuración: descomenta las dos líneas siguientes para pausar en este punto
    # import debugpy
    # debugpy.breakpoint()
 
    menu()
 