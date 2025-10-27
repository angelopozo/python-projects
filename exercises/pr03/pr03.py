import csv, os

class ScheduleRecord:
    def __init__(self, employee: str, day: str, check_in: int, check_out: int):
        self.employee = employee
        self.day = day
        self.check_in = check_in
        self.check_out = check_out

    def duration(self) -> int:
        return self.check_out - self.check_in

class Employee:
    def __init__(self, name):
        self.name = name
        self.records = []
    
    def add_record(self, record):
        self.records.append(record)
    
    def total_hours(self):
        return sum(record.duration() for record in self.records)
    
    def worked_days(self):
        days = {record.day for record in self.records}
        return len(days)
    
    def csv_row(self):
        return [self.name, self.worked_days(), self.total_hours()]

class ScheduleManager:
    def __init__(self, input_file):
        self.input_file = input_file
        self.employees = {}
        self.records = []
    
    def read_file(self):
        with open(self.input_file, newline='', encoding='utf-8') as f:
            reader = csv.reader(f, delimiter=';', quotechar='"')
            
            for row in reader:
                name, day, h_in, h_out = row
                check_in = int(h_in)
                check_out = int(h_out)
                
                record = ScheduleRecord(name, day, check_in, check_out)
                self.records.append(record)
                
                if name not in self.employees:
                    self.employees[name] = Employee(name)
                
                self.employees[name].add_record(record)
    
    def write_summary(self, output_file):
        with open(f'../data/pr03/{output_file}', 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            writer.writerow(['employee', 'worked_days', 'total_hours'])
            
            for employee in sorted(self.employees.values(), key=lambda e: e.name):
                writer.writerow(employee.csv_row())

def early_employees(records, reference_hour=8):
    early = {r.employee for r in records if r.check_in < reference_hour}
    
    with open('../data/pr03/early_employees.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(['employee', 'check_in_hour'])
        
        for employee in sorted(early):
            check_ins = {r.check_in for r in records if r.employee == employee and r.check_in < reference_hour}
            for check_in in sorted(check_ins):
                writer.writerow([employee, check_in])
    
    print(f"Early employees (before {reference_hour}:00): {sorted(early)}")
    print("File '../data/pr03/early_employees.csv' has been generated.")
    return early

def days_intersection(records):
    monday_employees = {r.employee for r in records if r.day.lower() == 'lunes'}
    friday_employees = {r.employee for r in records if r.day.lower() == 'viernes'}
    
    both_days = monday_employees & friday_employees
    
    with open('../data/pr03/two_days.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(['employee'])
        for employee in sorted(both_days):
            writer.writerow([employee])
    
    print(f"Employees who worked Monday AND Friday: {sorted(both_days)}")
    print("File '../data/pr03/two_days.csv' has been generated.")
    return both_days

def exclusive_employees(records):
    saturday_employees = {r.employee for r in records if r.day.lower() == 'sábado'}
    sunday_employees = {r.employee for r in records if r.day.lower() == 'domingo'}
    
    only_saturday = saturday_employees - sunday_employees
    
    print(f"Employees who worked Saturday but NOT Sunday: {sorted(only_saturday)}")
    print("Operation used: SET DIFFERENCE (saturday - sunday)")
    return only_saturday

def weekly_summary(records):
    employee_data = {}
    
    for record in records:
        if record.employee not in employee_data:
            employee_data[record.employee] = {
                'days': set(),
                'total_hours': 0
            }
        
        employee_data[record.employee]['days'].add(record.day)
        employee_data[record.employee]['total_hours'] += record.duration()
    
    with open('../data/pr03/weekly_summary.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(['employee', 'worked_days', 'total_hours'])
        
        for employee in sorted(employee_data.keys()):
            worked_days = len(employee_data[employee]['days'])
            total_hours = employee_data[employee]['total_hours']
            writer.writerow([employee, worked_days, total_hours])
    
    print("Weekly summary:")
    for employee in sorted(employee_data.keys()):
        days = len(employee_data[employee]['days'])
        hours = employee_data[employee]['total_hours']
        print(f"{employee}: {days} days, {hours} hours")
    
    print("File '../data/pr03/weekly_summary.csv' has been generated.")
    return employee_data

def duration_filter(records, minimum_hours=6):
    records_by_employee = {}
    for record in records:
        if record.employee not in records_by_employee:
            records_by_employee[record.employee] = []
        records_by_employee[record.employee].append(record)
    
    constant_employees = {
        employee 
        for employee, regs in records_by_employee.items() 
        if all(reg.duration() >= minimum_hours for reg in regs)
    }
    
    print(f"Employees who worked at least {minimum_hours} hours in ALL their shifts:")
    print(sorted(constant_employees))
    return constant_employees

def use_classes_for_management():
    manager = ScheduleManager('horarios.csv')
    manager.read_file()
    manager.write_summary('class_summary.csv')
    
    print("========== CLASS-BASED SUMMARY ==========")
    for employee in sorted(manager.employees.values(), key=lambda e: e.name):
        print(f"{employee.name}: {employee.worked_days()} days, {employee.total_hours()} hours")
    
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
            name, day, h_in, h_out = row
            check_in = int(h_in)
            check_out = int(h_out)
            record = ScheduleRecord(name, day, check_in, check_out)
            records.append(record)
    
    print(f"{len(records)} records have been read.\n")
    
    employees_by_day = {}
    for record in records:
        if record.day not in employees_by_day:
            employees_by_day[record.day] = set()
        employees_by_day[record.day].add(record.employee)
    
    long_shift_employees = {r.employee for r in records if r.duration() >= 8}
    
    total_hours = {}
    for record in records:
        total_hours.setdefault(record.employee, 0)
        total_hours[record.employee] += record.duration()
    
    while True:
        option = menu()
        
        if option == '1':
            print("\n========== EMPLOYEES BY DAY ==========")
            for day, employees in employees_by_day.items():
                print(f"{day}: {employees}")
        
        elif option == '2':
            print("\n========== EMPLOYEES WITH LONG SHIFTS ==========")
            print(f"Employees with 8+ hour shifts: {long_shift_employees}")
        
        elif option == '3':
            print("\n========== BASIC SUMMARY ==========")
            for employee, hours in sorted(total_hours.items()):
                print(f"{employee}: {hours} hours")
            
            with open('../data/pr03/hours_summary.csv', 'w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                writer.writerow(['employee', 'total_hours'])
                for employee, total in sorted(total_hours.items()):
                    writer.writerow([employee, total])
            
            print("File '../data/pr03/hours_summary.csv' has been generated.")
        
        elif option == '4':
            hour = input("Enter reference hour (default 8): ")
            ref_hour = int(hour) if hour.strip() else 8
            early_employees(records, ref_hour)
        
        elif option == '5':
            days_intersection(records)
        
        elif option == '6':
            exclusive_employees(records)
        
        elif option == '7':
            weekly_summary(records)
        
        elif option == '8':
            hours = input("Enter minimum hours per shift (default 6): ")
            min_hours = int(hours) if hours.strip() else 6
            duration_filter(records, min_hours)
        
        elif option == '9':
            use_classes_for_management()
        
        elif option == '0':
            print("Exiting the program.")
            break
        
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()