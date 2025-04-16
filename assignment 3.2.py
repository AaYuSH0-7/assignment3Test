# A simple Requisition System that allows staff to submit requisitions, approve/reject them, and view statistics.

counter = 1000  # Global counter for requisition IDs

class RequisitionSystem:
    def __init__(self):
        # Initialize the system with empty requisitions and counters
        self.requisitions = []
        self.approved = 0
        self.pending = 0
        self.not_approved = 0

    #  This method handles input collection for staff details
    def staff_info(self):
        date = input("Enter the date (DD/MM/YYYY): ")
        staff_id = input("Enter the Staff ID: ")
        name = input("Enter the Staff Name: ")
        return date, staff_id, name

    # This method handles collecting multiple items and calculating the total
    def requisitions_details(self):
        items = []
        total = 0
        while True:
            item = input("Enter item (or 'done'): ")
            if item.lower() == 'done':
                break
            try:
                price = float(input("Enter price: "))
                items.append((item, price))
                total += price
            except ValueError:
                print("Invalid price. Try again.")
        return items, total

    #  This logic checks whether a requisition is auto-approved or pending
    def requisition_approval(self, total):
        return "Approved" if total < 500 else "Pending"

    #  Main method to submit a requisition
    def create_requisition(self):
        global counter
        date, staff_id, name = self.staff_info()
        items, total = self.requisitions_details()
        status = self.requisition_approval(total)

        if status == "Approved":
            ref = staff_id + str(counter)
            self.approved += 1
        else:
            ref = "N/A"
            self.pending += 1

        self.requisitions.append({
            'id': counter,
            'date': date,
            'staff_id': staff_id,
            'name': name,
            'items': items,
            'total': total,
            'status': status,
            'ref': ref
        })
        counter += 1  # Update global counter

    #  This method allows responses to pending requisitions
    def respond_requisition(self):
        for requisition in self.requisitions:
            if requisition['status'] == "Pending":
                print(f"\nRequisition {requisition['id']} for {requisition['name']} is pending.")
                choice = input("Approve or Not approved? ").lower()
                if choice == 'approve':
                    requisition['status'] = "Approved"
                    requisition['ref'] = requisition['staff_id'] + str(requisition['id'])
                    self.approved += 1
                    self.pending -= 1
                elif choice == 'not approved':
                    requisition['status'] = "Not approved"
                    requisition['ref'] = "N/A"
                    self.not_approved += 1
                    self.pending -= 1
                else:
                    print("Invalid choice. Skipping.")

    # Displays all submitted requisitions with full details
    def display_requisitions(self):
        for requisition in self.requisitions:
            print("\n=== Requisition Details ===")
            print(f"Date: {requisition['date']}")
            print(f"Staff ID: {requisition['staff_id']}")
            print(f"Staff Name: {requisition['name']}")
            print(f"Requisition ID: {requisition['id']}")
            print(f"Total: ${requisition['total']:.2f}")
            print(f"Status: {requisition['status']}")
            print(f"Approval Reference: {requisition['ref']}")

    #  Display summary statistics
    def requisition_statistics(self):
        print("\n=== Requisition Statistics ===")
        print(f"Total Requisitions: {len(self.requisitions)}")
        print(f"Approved: {self.approved}")
        print(f"Pending: {self.pending}")
        print(f"Not Approved: {self.not_approved}")


# Main program loop: handles user interaction
rs = RequisitionSystem()
while True:
    print("\n--- Requisition System Menu ---")
    print("1. Submit Requisition")
    print("2. Display Requisitions")
    print("3. Respond to Pending Requisitions")
    print("4. Show Statistics")
    print("5. Exit")

    choice = input("Choose an option: ")

    if choice == '1':
        rs.create_requisition()
    elif choice == '2':
        rs.display_requisitions()
    elif choice == '3':
        rs.respond_requisition()
    elif choice == '4':
        rs.requisition_statistics()
    elif choice == '5':
        print("Exiting Requisition System.")
        break
    else:
        print("Invalid choice. Please try again.")
