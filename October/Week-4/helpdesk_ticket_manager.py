class SupportTicket:
    def __init__(self, ticket_id, customer, issue):
        self.ticket_id = ticket_id
        self.customer = customer
        self.issue = issue
        self.status = "Open"

    def close_ticket(self):
        if self.status == "Closed":
            print(f"Ticket {self.ticket_id} is already closed.")
            return

        self.status = "Closed"
        print(f"Ticket {self.ticket_id} has been closed.")

    def display_ticket(self):
        print(f"Ticket ID: {self.ticket_id}")
        print(f"Customer: {self.customer}")
        print(f"Issue: {self.issue}")
        print(f"Status: {self.status}")
        print("-" * 30)


class Helpdesk:
    def __init__(self):
        self.tickets = {}
        self.next_ticket_id = 1001

    def create_ticket(self, customer, issue):
        if not customer.strip() or not issue.strip():
            raise ValueError("Customer and issue cannot be empty.")

        ticket = SupportTicket(
            self.next_ticket_id,
            customer,
            issue
        )

        self.tickets[self.next_ticket_id] = ticket

        print(f"Ticket created: {self.next_ticket_id}")
        self.next_ticket_id += 1

        return ticket

    def find_ticket(self, ticket_id):
        return self.tickets.get(ticket_id)

    def close_ticket(self, ticket_id):
        ticket = self.find_ticket(ticket_id)

        if ticket is None:
            print(f"Ticket {ticket_id} was not found.")
            return

        ticket.close_ticket()

    def display_all_tickets(self):
        if not self.tickets:
            print("No support tickets available.")
            return

        for ticket in self.tickets.values():
            ticket.display_ticket()


# Create a helpdesk
helpdesk = Helpdesk()

# Create support tickets
helpdesk.create_ticket(
    "Alex",
    "Cannot connect to Wi-Fi"
)

helpdesk.create_ticket(
    "Sam",
    "Laptop is running slowly"
)

helpdesk.create_ticket(
    "Jordan",
    "Password reset required"
)

print("\n--- All Support Tickets ---")
helpdesk.display_all_tickets()

print("\n--- Closing a Ticket ---")
helpdesk.close_ticket(1001)

print("\n--- Searching for a Ticket ---")
ticket = helpdesk.find_ticket(1002)

if ticket is not None:
    ticket.display_ticket()

print("\n--- Testing an Unknown Ticket ---")
helpdesk.close_ticket(9999)