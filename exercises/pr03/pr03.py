import csv, os

class ScheduleRecord:
    def __init__(self, employee: str, day: str, checkIn: int, checkOut: int):
        self.employee = employee
        self.day = day
        self.checkIn = checkIn
        self.checkOut = checkOut

    def duration(self) -> int:
        return self.checkOut - self.checkIn

class Employee:
    def __init__(self, name):
        self.name = name
        self.records = []
    
    def addRecord(self, record):
        self.records.append(record)
    
    def totalHours(self):
        return sum(record.duration() for record in self.records)
    
    def workedDays(self):
        days = {record.day for record in self.records}
        return len(days)
    
    def csvRow(self):
        return [self.name, self.workedDays(), self.totalHours()]

class ScheduleManager:
    def __init__(self, inputFile):
        self.inputFile = inputFile
        self.employees = {}
        self.records = []
    
    def readFile(self):
        with open(self.inputFile, newline='', encoding='utf-8') as f:
            reader = csv.reader(f, delimiter=';', quotechar='"')
            
            for row in reader:
                name, day, hIn, hOut = row
                checkIn = int(hIn)
                checkOut = int(hOut)
                
                record = ScheduleRecord(name, day, checkIn, checkOut)
                self.records.append(record)
                
                if name not in self.employees:
                    self.employees[name] = Employee(name)
                
                self.employees[name].addRecord(record)
    
    def writeSummary(self, outputFile):
        with open(f'../data/pr03/{outputFile}', 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            writer.writerow(['employee', 'worked_days', 'total_hours'])
            
            for employee in sorted(self.employees.values(), key=lambda e: e.name):
                writer.writerow(employee.csvRow())

def earlyEmployees(records, referenceHour=8):
    early = {r.employee for r in records if r.checkIn < referenceHour}
    
    with open('../data/pr03/early_employees.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(['employee', 'check_in_hour'])
        
        for employee in sorted(early):
            checkIns = {r.checkIn for r in records if r.employee == employee and r.checkIn < referenceHour}
            for checkIn in sorted(checkIns):
                writer.writerow([employee, checkIn])
    
    print(f"Early employees (before {referenceHour}:00): {sorted(early)}")
    print("File '../data/pr03/early_employees.csv' has been generated.")
    return early

def daysIntersection(records):
    mondayEmployees = {r.employee for r in records if r.day.lower() == 'lunes'}
    fridayEmployees = {r.employee for r in records if r.day.lower() == 'viernes'}
    
    bothDays = mondayEmployees & fridayEmployees
    
    with open('../data/pr03/two_days.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(['employee'])
        for employee in sorted(bothDays):
            writer.writerow([employee])
    
    print(f"Employees who worked Monday AND Friday: {sorted(bothDays)}")
    print("File '../data/pr03/two_days.csv' has been generated.")
    return bothDays

def exclusiveEmployees(records):
    saturdayEmployees = {r.employee for r in records if r.day.lower() == 'sábado'}
    sundayEmployees = {r.employee for r in records if r.day.lower() == 'domingo'}
    
    onlySaturday = saturdayEmployees - sundayEmployees
    
    print(f"Employees who worked Saturday but NOT Sunday: {sorted(onlySaturday)}")
    print("Operation used: SET DIFFERENCE (saturday - sunday)")
    return onlySaturday

def weeklySummary(records):
    employeeData = {}
    
    for record in records:
        if record.employee not in employeeData:
            employeeData[record.employee] = {
                'days': set(),
                'total_hours': 0
            }
        
        employeeData[record.employee]['days'].add(record.day)
        employeeData[record.employee]['total_hours'] += record.duration()
    
    with open('../data/pr03/weekly_summary.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(['employee', 'worked_days', 'total_hours'])
        
        for employee in sorted(employeeData.keys()):
            workedDays = len(employeeData[employee]['days'])
            totalHours = employeeData[employee]['total_hours']
            writer.writerow([employee, workedDays, totalHours])
    
    print("Weekly summary:")
    for employee in sorted(employeeData.keys()):
        days = len(employeeData[employee]['days'])
        hours = employeeData[employee]['total_hours']
        print(f"{employee}: {days} days, {hours} hours")
    
    print("File '../data/pr03/weekly_summary.csv' has been generated.")
    return employeeData

def durationFilter(records, minimumHours=6):
    recordsByEmployee = {}
    for record in records:
        if record.employee not in recordsByEmployee:
            recordsByEmployee[record.employee] = []
        recordsByEmployee[record.employee].append(record)
    
    constantEmployees = {
        employee 
        for employee, regs in recordsByEmployee.items() 
        if all(reg.duration() >= minimumHours for reg in regs)
    }
    
    print(f"Employees who worked at least {minimumHours} hours in ALL their shifts:")
    print(sorted(constantEmployees))
    return constantEmployees

def useClassesForManagement():
    manager = ScheduleManager('horarios.csv')
    manager.readFile()
    manager.writeSummary('class_summary.csv')
    
    print("========== CLASS-BASED SUMMARY ==========")
    for employee in sorted(manager.employees.values(), key=lambda e: e.name):
        print(f"{employee.name}: {employee.workedDays()} days, {employee.totalHours()} hours")
    
    print("File '../data/pr03/class_summary.csv' has been generated.")

def menu():
    print("\n========== SCHEDULE ANALYSIS PROGRAM ==========")
    print("1) Show employees by day")
    print("2) Employees with long shifts (8+ hours)")
    print("3) Generate hours summary")
    print("4) Early employees")
    print("5) Days intersection (Monday and Friday)")
    print("6) Exclusive employees (Saturday not Sunday)")
    print("7) Weekly summary")
    print("8) Duration filter")
    print("9) Use classes for management")
    print("0) Exit")
    return input("Choose an option: ")

def main():
    if not os.path.exists('../data/pr03'):
        os.makedirs('../data/pr03')
    
    records = []
    
    with open('horarios.csv', newline='', encoding='utf-8') as f:
        reader = csv.reader(f, delimiter=';', quotechar='"')
        for row in reader:
            name, day, hIn, hOut = row
            checkIn = int(hIn)
            checkOut = int(hOut)
            record = ScheduleRecord(name, day, checkIn, checkOut)
            records.append(record)
    
    print(f"{len(records)} records have been read.\n")
    
    employeesByDay = {}
    for record in records:
        if record.day not in employeesByDay:
            employeesByDay[record.day] = set()
        employeesByDay[record.day].add(record.employee)
    
    longShiftEmployees = {r.employee for r in records if r.duration() >= 8}
    
    totalHours = {}
    for record in records:
        totalHours.setdefault(record.employee, 0)
        totalHours[record.employee] += record.duration()
    
    while True:
        option = menu()
        
        if option == '1':
            print("\n========== EMPLOYEES BY DAY ==========")
            for day, employees in employeesByDay.items():
                print(f"{day}: {employees}")
        
        elif option == '2':
            print("\n========== EMPLOYEES WITH LONG SHIFTS ==========")
            print(f"Employees with 8+ hour shifts: {longShiftEmployees}")
        
        elif option == '3':
            print("\n========== BASIC SUMMARY ==========")
            for employee, hours in sorted(totalHours.items()):
                print(f"{employee}: {hours} hours")
            
            with open('../data/pr03/hours_summary.csv', 'w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                writer.writerow(['employee', 'total_hours'])
                for employee, total in sorted(totalHours.items()):
                    writer.writerow([employee, total])
            
            print("File '../data/pr03/hours_summary.csv' has been generated.")
        
        elif option == '4':
            hour = input("Enter reference hour (default 8): ")
            refHour = int(hour) if hour.strip() else 8
            earlyEmployees(records, refHour)
        
        elif option == '5':
            daysIntersection(records)
        
        elif option == '6':
            exclusiveEmployees(records)
        
        elif option == '7':
            weeklySummary(records)
        
        elif option == '8':
            hours = input("Enter minimum hours per shift (default 6): ")
            minHours = int(hours) if hours.strip() else 6
            durationFilter(records, minHours)
        
        elif option == '9':
            useClassesForManagement()
        
        elif option == '0':
            print("Exiting the program.")
            break
        
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()