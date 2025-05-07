class Item:
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price

    def total(self):
        return self.quantity * self.price


class Invoice:
    def __init__(self, invoice_id, customer_name):
        self.invoice_id = invoice_id
        self.customer_name = customer_name
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def calculate_total(self):
        return sum(item.total() for item in self.items)

    def display(self):
        print(f"\nInvoice ID: {self.invoice_id}")
        print(f"Customer: {self.customer_name}")
        print("Items:")
        for item in self.items:
            print(f"- {item.name}: {item.quantity} x {item.price} = {item.total()}")
        print(f"Total: {self.calculate_total()}\n")


class InvoiceSystem:
    def __init__(self):
        self.invoices = []

    def create_invoice(self):
        invoice_id = input("Enter invoice ID: ")
        customer_name = input("Enter customer name: ")
        invoice = Invoice(invoice_id, customer_name)

        while True:
            name = input("Item name (or 'done' to finish): ")
            if name.lower() == 'done':
                break
            try:
                quantity = int(input("Quantity: "))
                price = float(input("Price per unit: "))
            except ValueError:
                print("Invalid input. Try again.")
                continue

            item = Item(name, quantity, price)
            invoice.add_item(item)

        self.invoices.append(invoice)
        print("Invoice created.")

    def view_invoices(self):
        if not self.invoices:
            print("No invoices found.")
        for invoice in self.invoices:
            invoice.display()

    def menu(self):
        while True:
            print("\n--- Invoice Management System ---")
            print("1. Create Invoice")
            print("2. View Invoices")
            print("3. Exit")
            choice = input("Choose an option: ")

            if choice == '1':
                self.create_invoice()
            elif choice == '2':
                self.view_invoices()
            elif choice == '3':
                print("Exiting.")
                break
            else:
                print("Invalid choice.")


if __name__ == "__main__":
    system = InvoiceSystem()
    system.menu()
