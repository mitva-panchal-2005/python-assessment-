import datetime

rentals = {}  
late_fee_per_day = 10  



def rent_book():
    customer = input("Enter customer name: ").strip()
    book_title = input("Enter book title: ").strip()
    
    try:
        rental_days = int(input("Enter number of days to rent: "))
    except ValueError:
        print("Invalid input! Number of days must be an integer.")
        return
    
    rental_date = datetime.date.today()
    return_date = rental_date + datetime.timedelta(days=rental_days)

    
    rentals[customer] = {
        "book_title": book_title,
        "rental_date": rental_date,
        "return_date": return_date
    }

    print("\n✅ Book rented successfully!")
    print(f"Customer: {customer}")
    print(f"Book: {book_title}")
    print(f"Rented on: {rental_date}")
    print(f"Expected return: {return_date}\n")


def return_book():
    customer = input("Enter customer name: ").strip()

    if customer not in rentals:
        print("❌ No rental record found for this customer!\n")
        return

    details = rentals[customer]
    actual_return_date = datetime.date.today()

    
    late_days = (actual_return_date - details["return_date"]).days
    late_fee = late_fee_per_day * late_days if late_days > 0 else 0

    
    print("\n📖 --- Rental Receipt --- 📖")
    print(f"Customer: {customer}")
    print(f"Book: {details['book_title']}")
    print(f"Rented on: {details['rental_date']}")
    print(f"Expected return: {details['return_date']}")
    print(f"Returned on: {actual_return_date}")
    print(f"Late fee: ₹{late_fee}")
    print("---------------------------\n")

    
    del rentals[customer]


def show_rentals():
    if not rentals:
        print("📚 No active rentals.\n")
        return

    print("\n📚 Active Rentals:")
    for customer, details in rentals.items():
        print(f"- {customer} | Book: {details['book_title']} | Due: {details['return_date']}")
    print()



def main():
    while True:
        print("=== RentTrack Library System ===")
        print("1. Rent a Book")
        print("2. Return a Book")
        print("3. Show Active Rentals")
        print("4. Exit")

        choice = input("Enter choice (1-4): ")

        if choice == "1":
            rent_book()
        elif choice == "2":
            return_book()
        elif choice == "3":
            show_rentals()
        elif choice == "4":
            print("👋 Exiting RentTrack. Goodbye!")
            break
        else:
            print("❌ Invalid choice! Please try again.\n")



if __name__ == "_main_":
    main()