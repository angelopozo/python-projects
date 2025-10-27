import csv, os
from datetime import datetime, date

class Client:
    def __init__(self, id: int, name: str, email: str, registration_date: str):
        self.id = id
        self.name = name
        self.email = email
        self.registration_date = datetime.strptime(registration_date, '%Y-%m-%d').date()
    
    def seniority_days(self) -> int:
        return (date.today() - self.registration_date).days
    
    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}, Email: {self.email}, Registered: {self.registration_date}"

class Event:
    def __init__(self, id: int, name: str, event_date: str, category: str, price: float):
        self.id = id
        self.name = name
        self.event_date = datetime.strptime(event_date, '%Y-%m-%d').date()
        self.category = category
        self.price = price
    
    def days_until_event(self) -> int:
        delta = (self.event_date - date.today()).days
        return delta if delta >= 0 else 0
    
    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}, Date: {self.event_date}, Category: {self.category}, Price: ${self.price:.2f}"

class Sale:
    def __init__(self, id: int, client_id: int, event_id: int, sale_date: str, quantity: int):
        self.id = id
        self.client_id = client_id
        self.event_id = event_id
        self.sale_date = datetime.strptime(sale_date, '%Y-%m-%d').date()
        self.quantity = quantity
    
    def __str__(self):
        return f"ID: {self.id}, Client: {self.client_id}, Event: {self.event_id}, Date: {self.sale_date}, Qty: {self.quantity}"

def load_data():
    clients = {}
    events = {}
    sales = []
    
    try:
        with open('../data/final/clients.csv', newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f, delimiter=';')
            for row in reader:
                client = Client(int(row['id']), row['name'], row['email'], row['registration_date'])
                clients[client.id] = client
    except FileNotFoundError:
        print("Warning: clients.csv not found. Starting with empty client list.")
    
    try:
        with open('../data/final/events.csv', newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f, delimiter=';')
            for row in reader:
                event = Event(int(row['id']), row['name'], row['date'], row['category'], float(row['price']))
                events[event.id] = event
    except FileNotFoundError:
        print("Warning: events.csv not found. Starting with empty event list.")
    
    try:
        with open('../data/final/sales.csv', newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f, delimiter=';')
            for row in reader:
                sale = Sale(int(row['id']), int(row['client_id']), int(row['event_id']), 
                            row['sale_date'], int(row['quantity']))
                sales.append(sale)
    except FileNotFoundError:
        print("Warning: sales.csv not found. Starting with empty sales list.")
    
    return clients, events, sales

def list_table(table_name: str, clients: dict, events: dict, sales: list):
    print(f"\n========== {table_name.upper()} ==========")
    
    if table_name.lower() == 'clients':
        if not clients:
            print("No clients found.")
            return
        for client in clients.values():
            print(client)
    
    elif table_name.lower() == 'events':
        if not events:
            print("No events found.")
            return
        for event in events.values():
            print(event)
    
    elif table_name.lower() == 'sales':
        if not sales:
            print("No sales found.")
            return
        for sale in sales:
            print(sale)
    
    else:
        print("Invalid table name. Use: clients, events, or sales")

def validate_email(email: str) -> bool:
    return '@' in email and '.' in email.split('@')[1]

def add_client(clients: dict):
    print("\n========== ADD NEW CLIENT ==========")
    
    name = input("Enter client name: ").strip()
    
    while True:
        email = input("Enter client email: ").strip()
        if validate_email(email):
            break
        print("Invalid email format. Please try again.")
    
    while True:
        reg_date = input("Enter registration date (YYYY-MM-DD): ").strip()
        try:
            datetime.strptime(reg_date, '%Y-%m-%d')
            break
        except ValueError:
            print("Invalid date format. Use YYYY-MM-DD")
    
    new_id = max(clients.keys()) + 1 if clients else 1
    
    client = Client(new_id, name, email, reg_date)
    clients[new_id] = client
    
    with open('../data/final/clients.csv', 'a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f, delimiter=';')
        if os.path.getsize('../data/final/clients.csv') == 0:
            writer.writerow(['id', 'name', 'email', 'registration_date'])
        writer.writerow([client.id, client.name, client.email, client.registration_date])
    
    print(f"Client '{name}' added successfully with ID {new_id}.")

def filter_sales_by_range(sales: list):
    print("\n========== FILTER SALES BY DATE RANGE ==========")
    
    while True:
        start_date_str = input("Enter start date (YYYY-MM-DD): ").strip()
        try:
            start_date = datetime.strptime(start_date_str, '%Y-%m-%d').date()
            break
        except ValueError:
            print("Invalid date format. Use YYYY-MM-DD")
    
    while True:
        end_date_str = input("Enter end date (YYYY-MM-DD): ").strip()
        try:
            end_date = datetime.strptime(end_date_str, '%Y-%m-%d').date()
            if end_date >= start_date:
                break
            print("End date must be after or equal to start date.")
        except ValueError:
            print("Invalid date format. Use YYYY-MM-DD")
    
    filtered = [s for s in sales if start_date <= s.sale_date <= end_date]
    
    if not filtered:
        print(f"No sales found between {start_date} and {end_date}")
        return
    
    print(f"\nSales between {start_date} and {end_date}:")
    for sale in filtered:
        print(sale)
    print(f"\nTotal sales found: {len(filtered)}")

def statistics(clients: dict, events: dict, sales: list):
    print("\n========== STATISTICS ==========")
    
    if not sales:
        print("No sales data available.")
        return
    
    total_revenue = sum(s.quantity * events[s.event_id].price for s in sales if s.event_id in events)
    print(f"Total revenue: ${total_revenue:.2f}")
    
    revenue_by_event = {}
    for sale in sales:
        if sale.event_id in events:
            event = events[sale.event_id]
            revenue = sale.quantity * event.price
            revenue_by_event[event.name] = revenue_by_event.get(event.name, 0) + revenue
    
    print("\nRevenue by event:")
    for event_name, revenue in revenue_by_event.items():
        print(f"  {event_name}: ${revenue:.2f}")
    
    categories = {event.category for event in events.values()}
    print(f"\nEvent categories: {categories}")
    
    if events:
        upcoming_events = [e for e in events.values() if e.days_until_event() > 0]
        if upcoming_events:
            nearest = min(upcoming_events, key=lambda e: e.days_until_event())
            print(f"\nNearest upcoming event: {nearest.name} in {nearest.days_until_event()} days")
        else:
            print("\nNo upcoming events.")
    
    if events:
        prices = [event.price for event in events.values()]
        price_stats = (min(prices), max(prices), sum(prices) / len(prices))
        print(f"\nPrice statistics (min, max, avg): ${price_stats[0]:.2f}, ${price_stats[1]:.2f}, ${price_stats[2]:.2f}")

def export_report(events: dict, sales: list):
    print("\n========== EXPORT REPORT ==========")
    
    report_data = {}
    for sale in sales:
        if sale.event_id in events:
            event = events[sale.event_id]
            revenue = sale.quantity * event.price
            
            if event.name not in report_data:
                report_data[event.name] = {
                    'tickets_sold': 0,
                    'total_revenue': 0,
                    'category': event.category
                }
            
            report_data[event.name]['tickets_sold'] += sale.quantity
            report_data[event.name]['total_revenue'] += revenue
    
    with open('../data/final/summary_report.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f, delimiter=';')
        writer.writerow(['event_name', 'category', 'tickets_sold', 'total_revenue'])
        
        for event_name, data in sorted(report_data.items()):
            writer.writerow([event_name, data['category'], data['tickets_sold'], f"{data['total_revenue']:.2f}"])
    
    print("Report exported to '../data/final/summary_report.csv'")
    print("\nSummary:")
    for event_name, data in sorted(report_data.items()):
        print(f"  {event_name}: {data['tickets_sold']} tickets, ${data['total_revenue']:.2f} revenue")

def menu():
    print("\n========== EVENT CRM SYSTEM ==========")
    print("1) Load data")
    print("2) List clients")
    print("3) List events")
    print("4) List sales")
    print("5) Add new client")
    print("6) Filter sales by date range")
    print("7) Show statistics")
    print("8) Export summary report")
    print("0) Exit")
    return input("Choose an option: ").strip()

def main():
    if not os.path.exists('../data/final'):
        os.makedirs('../data/final')
    
    clients = {}
    events = {}
    sales = []
    data_loaded = False
    
    print("Welcome to the Event CRM System!")
    
    while True:
        option = menu()
        
        if option == '1':
            clients, events, sales = load_data()
            data_loaded = True
            print(f"\nData loaded: {len(clients)} clients, {len(events)} events, {len(sales)} sales")
        
        elif option == '2':
            if not data_loaded:
                print("\nPlease load data first (option 1)")
            else:
                list_table('clients', clients, events, sales)
        
        elif option == '3':
            if not data_loaded:
                print("\nPlease load data first (option 1)")
            else:
                list_table('events', clients, events, sales)
        
        elif option == '4':
            if not data_loaded:
                print("\nPlease load data first (option 1)")
            else:
                list_table('sales', clients, events, sales)
        
        elif option == '5':
            if not data_loaded:
                print("\nPlease load data first (option 1)")
            else:
                add_client(clients)
        
        elif option == '6':
            if not data_loaded:
                print("\nPlease load data first (option 1)")
            else:
                filter_sales_by_range(sales)
        
        elif option == '7':
            if not data_loaded:
                print("\nPlease load data first (option 1)")
            else:
                statistics(clients, events, sales)
        
        elif option == '8':
            if not data_loaded:
                print("\nPlease load data first (option 1)")
            else:
                export_report(events, sales)
        
        elif option == '0':
            print("Exiting the program. Goodbye!")
            break
        
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
