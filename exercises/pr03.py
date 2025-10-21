import csv

def menu():
    print("=== PROGRAMA DE ANÁLISIS DE HORARIOS ===")
    print("1. Mostrar empleados por día")
    print("2. Empleados con turnos largos (8+ horas)")
    print("3. Generar resumen de horas")
    print("4. Empleados madrugadores")
    print("5. Intersección de días (lunes y viernes)")
    print("6. Empleados exclusivos (sábado no domingo)")
    print("7. Resumen semanal")
    print("8. Filtrado por duración")
    print("9. Usar clases para gestión")
    print("0. Salir")
    return input("Seleccione una opción: ")

def earlierEmployees(registers, reference_hour=8):
    print(f"Encuentra empleados que comienzan antes de la hora de referencia {reference_hour}:00")
    earliers = set()
    earliers_register = []

    for register in registers:
        if register.check_in < reference_hour:
            earliers.add(register.employee)
            earliers_register.append((register.employee, register.check_in))

    with open('data/pr03/earliers.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(['employee', 'check_in'])

        for employee in sorted(earliers):
            checksIn = [r.check_in for r in registers if r.employee == employee and r.check_in < reference_hour]
            for checkIn in sorted(set(checksIn)):
                writer.writerow([employee, checkIn])

    print(f"Empleados madrugadores (antes de las {reference_hour}:00): {sorted(earliers)}")
    print("Archivo 'earliers.csv' generado")
    return earliers

def intersectionDays(registers):
    print("Calcula empleados que trabajaron tanto lunes como viernes")
    monday_employees = {r.employee for r in registers if r.day.lower() == 'lunes'}
    friday_employees = {r.employee for r in registers if r.day.lower() == 'viernes'}

    both_days_employees = monday_employees & friday_employees

    with open('data/pr03/inTwoDays.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(['employee'])
        for employee in sorted(both_days_employees):
            writer.writerow([employee])

    print(f"Empleados que trabajaron lunes Y viernes: {sorted(both_days_employees)}")
    print("Archivo 'inTwoDays.csv' generado")
    return both_days_employees

def exclusiveEmployees(registers):
    print("Empleados que trabajaron sábado pero NO domingo")
    employees_saturday = {r.employee for r in registers if r.day.lower() == 'sábado'}
    employees_sunday = {r.employee for r in registers if r.day.lower() == 'domingo'}

    just_saturday_employees = employees_saturday - employees_sunday

    print(f"Empleados que trabajaron sábado pero NO domingo: {sorted(just_saturday_employees)}")
    print("Operación utilizada: DIFERENCIA DE CONJUNTOS (sabado - domingo)")
    return just_saturday_employees

def weeklySummary(registers):
    print("Calcula días trabajados y horas totales por empleado")
    employees_data = {}

    for register in registers:
        if register.employee not in employees_data:
            employees_data[register.employee] = {
                'days': set(),
                'total_hours': 0
            }

        employees_data[register.employee]['days'].add(register.day)
        employees_data[register.employee]['total_hours'] += register.duration()

    with open('data/pr03/weeklySummary.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(['employee', 'days_worked', 'total_hours'])

        for employee in sorted(employees_data.keys()):
            days_worked = len(employees_data[employee]['days'])
            total_hours = employees_data[employee]['total_hours']
            writer.writerow([employee, days_worked, total_hours])

    print("Resumen semanal generado en 'weeklySummary.csv'")
    for employee in sorted(employees_data.keys()):
        days = len(employees_data[employee]['days'])
        hours = employees_data[employee]['total_hours']
        print(f"{employee}: {days} días, {hours} horas")

    return employees_data

def filterByDuration(registers, min_hours=6):
    print(f"Empleados que trabajaron al menos {min_hours} horas en TODAS sus jornadas")
    registerByEmployee = {}
    for register in registers:
        if register.employee not in registerByEmployee:
            registerByEmployee[register.employee] = []
        registerByEmployee[register.employee].append(register)

    constant_employees = {
        employee
        for employee, registers in registerByEmployee.items()
        if all(register.duration() >= min_hours for register in registers)
    }

    print(f"Empleados que trabajaron al menos {min_hours} horas en TODAS sus jornadas:")
    print(sorted(constant_employees))
    return constant_employees

registers = []

class Employee:
    def __init__(self, name):
        self.name = name
        self.registers = []

    def addRegister(self, register):
        print(f"Añade un registro de horario al empleado {self.name}")
        self.registers.append(register)

    def totalHours(self):
        print(f"Calcula las horas totales trabajadas para {self.name}")
        return sum(register.duration() for register in self.registers)

    def workedDays(self):
        print(f"Obtiene el número de días distintos trabajados para {self.name}")
        days = {register.day for register in self.registers}
        return len(days)

    def csvRow(self):
        print(f"Devuelve una fila para el CSV de resumen para {self.name}")
        return [self.name, self.workedDays(), self.totalHours()]

class ScheduleManager:
    def __init__(self, input_file):
        self.input_file = input_file
        self.employees = {}
        self.registers = []

    def readFile(self):
        print("Lee el archivo de entrada y crea los registros")
        with open(self.input_file, newline='', encoding='utf-8') as f:
            reader = csv.reader(f, delimiter=',')
            next(reader)

            for row in reader:
                name, day, check_in, check_out = row
                check_in = int(check_in)
                check_out = int(check_out)

                register = RegisterManager(name, day, check_in, check_out)
                self.registers.append(register)

                if name not in self.employees:
                    self.employees[name] = Employee(name)

                self.employees[name].addRegister(register)

    def write_summary(self, output_file):
        print("Escribe el resumen en un archivo CSV")
        with open(f'data/pr03/{output_file}', 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            writer.writerow(['empleado', 'dias_trabajados', 'horas_totales'])

            for employee in sorted(self.employees.values(), key=lambda e: e.name):
                writer.writerow(employee.csvRow())

    def generate_summary(self):
        print("Genera el resumen utilizando clases")
        self.readFile()
        self.write_summary('classesSummary.csv')

        print("=== RESUMEN GENERADO CON CLASES ===")
        for employee in sorted(self.employees.values(), key=lambda e: e.name):
            print(f"{employee.name}: {employee.workedDays()} días, {employee.totalHours()} horas")

        print("Archivo 'classesSummary.csv' generado")

class RegisterManager:
    def __init__(self, employee: str, day: str, check_in: int, check_out: int):
        self.employee = employee
        self.day = day
        self.check_in = check_in
        self.check_out = check_out

    def duration(self) -> int:
        print(f"Devuelve la cantidad de horas trabajadas en este registro para {self.employee}")
        return self.check_out - self.check_in

with open('data/pr03.csv', newline='', encoding='utf-8') as f:
    reader = csv.reader(f, delimiter=',', quotechar='"')
    next(reader)
    for row in reader:
        name, day, check_in, check_out = row
        check_in = int(check_in)
        check_out = int(check_out)
        register = RegisterManager(name, day, check_in, check_out)
        registers.append(register)

print(f"Se han leído {len(registers)} registros")


employees_per_day = {}
for register in registers:
    if register.day not in employees_per_day:
        employees_per_day[register.day] = set()
    employees_per_day[register.day].add(register.employee)

for day, employees in employees_per_day.items():
    print(f"{day}: {employees}")

employees_long_shift = {r.employee for r in registers if r.duration() >= 8}
print(employees_long_shift)


total_hours = {}
for register in registers:
    total_hours.setdefault(register.employee, 0)
    total_hours[register.employee] += register.duration()

with open('data/pr03/scheduleSummary.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(['Empleado', 'Horas totales'])
    for employee, total in total_hours.items():
        writer.writerow([employee, total])

print("Se ha generado el fichero scheduleSummary.csv")


def main():
    print("Función principal que ejecuta el programa con menú interactivo")
    while True:
        option = menu()

        if option == '1':
            for day, employees in employees_per_day.items():
                print(f"{day}: {employees}")

        elif option == '2':
            print("Empleados con turnos de 8+ horas:", employees_long_shift)

        elif option == '3':
            print("Resumen básico generado en 'scheduleSummary.csv'")

        elif option == '4':
            hour = input("Ingrese hora de referencia (por defecto 8): ")
            hour_ref = int(hour) if hour.strip() else 8
            earlierEmployees(registers, hour_ref)

        elif option == '5':
            intersectionDays(registers)

        elif option == '6':
            exclusiveEmployees(registers)

        elif option == '7':
            weeklySummary(registers)

        elif option == '8':
            hours = input("Ingrese horas mínimas por jornada (por defecto 6): ")
            hours_min = int(hours) if hours.strip() else 6
            filterByDuration(registers, hours_min)

        elif option == '9':
            manager = ScheduleManager('data/pr03.csv')
            manager.generate_summary()

        elif option == '0':
            print("¡Hasta luego!")
            break
        
        else:
            print("Opción no válida")
        
if __name__ == "__main__":
    print(f"Se han leído {len(registers)} registros")
    
    print("\n=== EMPLEADOS POR DÍA ===")
    for day, employees in employees_per_day.items():
        print(f"{day}: {employees}")

    print(f"\n=== EMPLEADOS CON TURNOS LARGOS ===")
    print("Empleados con turnos de 8+ horas:", employees_long_shift)

    print(f"\n=== RESUMEN BÁSICO GENERADO ===")
    print("Se ha generado el fichero scheduleSummary.csv")
    
    print("\n" + "="*50)
    main()