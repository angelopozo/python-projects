import csv, os
from datetime import datetime, date

class Client:
    def __init__(self, id: int, name: str, email: str, registrationDate: str):
        self.id = id
        self.name = name
        self.email = email
        self.registrationDate = datetime.strptime(registrationDate, '%Y-%m-%d').date()
    
    def seniorityDays(self) -> int:
        return (date.today() - self.registrationDate).days
    
    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}, Email: {self.email}, Registered: {self.registrationDate}"

class Event:
    def __init__(self, id: int, name: str, eventDate: str, category: str, price: float):
        self.id = id
        self.name = name
        self.eventDate = datetime.strptime(eventDate, '%Y-%m-%d').date()
        self.category = category
        self.price = price
    
    def daysUntilEvent(self) -> int:
        delta = (self.eventDate - date.today()).days
        return delta if delta >= 0 else 0
    
    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}, Date: {self.eventDate}, Category: {self.category}, Price: ${self.price:.2f}"

class Sale:
    def __init__(self, id: int, clientId: int, eventId: int, saleDate: str, quantity: int):
        self.id = id
        self.clientId = clientId
        self.eventId = eventId
        self.saleDate = datetime.strptime(saleDate, '%Y-%m-%d').date()
        self.quantity = quantity
    
    def __str__(self):
        return f"ID: {self.id}, Client: {self.clientId}, Event: {self.eventId}, Date: {self.saleDate}, Qty: {self.quantity}"

def loadData():
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

def listTable(tableName: str, clients: dict, events: dict, sales: list):
    print(f"\n========== {tableName.upper()} ==========")
    
    if tableName.lower() == 'clients':
        if not clients:
            print("No clients found.")
            return
        for client in clients.values():
            print(client)
    
    elif tableName.lower() == 'events':
        if not events:
            print("No events found.")
            return
        for event in events.values():
            print(event)
    
    elif tableName.lower() == 'sales':
        if not sales:
            print("No sales found.")
            return
        for sale in sales:
            print(sale)
    
    else:
        print("Invalid table name. Use: clients, events, or sales")

def validateEmail(email: str) -> bool:
    return '@' in email and '.' in email.split('@')[1]

def addClient(clients: dict):
    print("\n========== ADD NEW CLIENT ==========")
    
    name = input("Enter client name: ").strip()
    
    while True:
        email = input("Enter client email: ").strip()
        if validateEmail(email):
            break
        print("Invalid email format. Please try again.")
    
    while True:
        regDate = input("Enter registration date (YYYY-MM-DD): ").strip()
        try:
            datetime.strptime(regDate, '%Y-%m-%d')
            break
        except ValueError:
            print("Invalid date format. Use YYYY-MM-DD")
    
    newId = max(clients.keys()) + 1 if clients else 1
    
    client = Client(newId, name, email, regDate)
    clients[newId] = client
    
    with open('../data/final/clients.csv', 'a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f, delimiter=';')
        if os.path.getsize('../data/final/clients.csv') == 0:
            writer.writerow(['id', 'name', 'email', 'registration_date'])
        writer.writerow([client.id, client.name, client.email, client.registrationDate])
    
    print(f"Client '{name}' added successfully with ID {newId}.")

def filterSalesByRange(sales: list):
    print("\n========== FILTER SALES BY DATE RANGE ==========")
    
    while True:
        startDateStr = input("Enter start date (YYYY-MM-DD): ").strip()
        try:
            startDate = datetime.strptime(startDateStr, '%Y-%m-%d').date()
            break
        except ValueError:
            print("Invalid date format. Use YYYY-MM-DD")
    
    while True:
        endDateStr = input("Enter end date (YYYY-MM-DD): ").strip()
        try:
            endDate = datetime.strptime(endDateStr, '%Y-%m-%d').date()
            if endDate >= startDate:
                break
            print("End date must be after or equal to start date.")
        except ValueError:
            print("Invalid date format. Use YYYY-MM-DD")
    
    filtered = [s for s in sales if startDate <= s.saleDate <= endDate]
    
    if not filtered:
        print(f"No sales found between {startDate} and {endDate}")
        return
    
    print(f"\nSales between {startDate} and {endDate}:")
    for sale in filtered:
        print(sale)
    print(f"\nTotal sales found: {len(filtered)}")

def statistics(clients: dict, events: dict, sales: list):
    print("\n========== STATISTICS ==========")
    
    if not sales:
        print("No sales data available.")
        return
    
    totalRevenue = sum(s.quantity * events[s.eventId].price for s in sales if s.eventId in events)
    print(f"Total revenue: ${totalRevenue:.2f}")
    
    revenueByEvent = {}
    for sale in sales:
        if sale.eventId in events:
            event = events[sale.eventId]
            revenue = sale.quantity * event.price
            revenueByEvent[event.name] = revenueByEvent.get(event.name, 0) + revenue
    
    print("\nRevenue by event:")
    for eventName, revenue in revenueByEvent.items():
        print(f"  {eventName}: ${revenue:.2f}")
    
    categories = {event.category for event in events.values()}
    print(f"\nEvent categories: {categories}")
    
    if events:
        upcomingEvents = [e for e in events.values() if e.daysUntilEvent() > 0]
        if upcomingEvents:
            nearest = min(upcomingEvents, key=lambda e: e.daysUntilEvent())
            print(f"\nNearest upcoming event: {nearest.name} in {nearest.daysUntilEvent()} days")
        else:
            print("\nNo upcoming events.")
    
    if events:
        prices = [event.price for event in events.values()]
        priceStats = (min(prices), max(prices), sum(prices) / len(prices))
        print(f"\nPrice statistics (min, max, avg): ${priceStats[0]:.2f}, ${priceStats[1]:.2f}, ${priceStats[2]:.2f}")

def exportReport(events: dict, sales: list):
    print("\n========== EXPORT REPORT ==========")
    
    reportData = {}
    for sale in sales:
        if sale.eventId in events:
            event = events[sale.eventId]
            revenue = sale.quantity * event.price
            
            if event.name not in reportData:
                reportData[event.name] = {
                    'tickets_sold': 0,
                    'total_revenue': 0,
                    'category': event.category
                }
            
            reportData[event.name]['tickets_sold'] += sale.quantity
            reportData[event.name]['total_revenue'] += revenue
    
    with open('../data/final/summary_report.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f, delimiter=';')
        writer.writerow(['event_name', 'category', 'tickets_sold', 'total_revenue'])
        
        for eventName, data in sorted(reportData.items()):
            writer.writerow([eventName, data['category'], data['tickets_sold'], f"{data['total_revenue']:.2f}"])
    
    print("Report exported to '../data/final/summary_report.csv'")
    print("\nSummary:")
    for eventName, data in sorted(reportData.items()):
        print(f"  {eventName}: {data['tickets_sold']} tickets, ${data['total_revenue']:.2f} revenue")

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
    dataLoaded = False
    
    print("Welcome to the Event CRM System!")
    
    while True:
        option = menu()
        
        if option == '1':
            clients, events, sales = loadData()
            dataLoaded = True
            print(f"\nData loaded: {len(clients)} clients, {len(events)} events, {len(sales)} sales")
        
        elif option == '2':
            if not dataLoaded:
                print("\nPlease load data first (option 1)")
            else:
                listTable('clients', clients, events, sales)
        
        elif option == '3':
            if not dataLoaded:
                print("\nPlease load data first (option 1)")
            else:
                listTable('events', clients, events, sales)
        
        elif option == '4':
            if not dataLoaded:
                print("\nPlease load data first (option 1)")
            else:
                listTable('sales', clients, events, sales)
        
        elif option == '5':
            if not dataLoaded:
                print("\nPlease load data first (option 1)")
            else:
                addClient(clients)
        
        elif option == '6':
            if not dataLoaded:
                print("\nPlease load data first (option 1)")
            else:
                filterSalesByRange(sales)
        
        elif option == '7':
            if not dataLoaded:
                print("\nPlease load data first (option 1)")
            else:
                statistics(clients, events, sales)
        
        elif option == '8':
            if not dataLoaded:
                print("\nPlease load data first (option 1)")
            else:
                exportReport(events, sales)
        
        elif option == '0':
            print("Exiting the program. Goodbye!")
            break
        
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()