donations = []

def main_program():
    while True:
        print(" DONATION TRACKING SYSTEM MENU")
        print("1. Treasurer")
        print("2. Organization Leader")
        print("3. Exit System")

        choice = input("Enter role number (1-3): ")

        if choice == '1':
            treasurer_menu()
        elif choice == '2':
            leader_menu()
        elif choice == '3':
            print("Thank you for using the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

def treasurer_menu():
    while True:
        print("TREASURER MENU")
        print("1. Input Donor & Amount")
        print("2. Track Total Collected")
        print("3. Back to Role Selection")

        choice = input("Enter choice (1-3): ")

        if choice == '1':
            add_donation()
        elif choice == '2':
            monitor_funds_raised()
        elif choice == '3':
            break
        else:
            print("Invalid choice.")

def leader_menu():
    while True:
        print("LEADER MENU")
        print("1. View Donor List")
        print("2. Monitor Funds Raised")
        print("3. Back to Role Selection")

        choice = input("Enter choice (1-3): ")

        if choice == '1':
            view_donor_list()
        elif choice == '2':
            monitor_funds_raised()
        elif choice == '3':
            break
        else:
            print("Invalid choice.")

def add_donation():
    print("ADD NEW DONATION")
    donor = input("Enter Donor Name: ")
    try:
        amount = float(input("Enter Donation Amount: $"))
        
        new_donation = {'name': donor, 'amount': amount}
        donations.append(new_donation)
        
        print(f"Donation from {donor} for ${amount:.2f} saved.")
    except ValueError:
        print("Error: Please enter a valid number for the amount.")

def get_total():
    total = 0
    for donation in donations:
        total += donation['amount']
    return total

def monitor_funds_raised():
    total = get_total()
    print(f"Total Collected: ${total:.2f}")

def view_donor_list():
    print("DONOR LIST")
    if not donations:
        print("No donations recorded yet.")
        return
    
    for i, donation in enumerate(donations):
        print(f"Record {i+1}:{donation['name']}donated ${donation['amount']:.2f}")
    
main_program()