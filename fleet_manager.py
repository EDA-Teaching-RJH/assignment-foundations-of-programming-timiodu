def init_database():

    names = ["Picard", "Riker", "Data", "Worf", "Crusher"]
    ranks = ["Captain", "Commander", "Lt. Commander", "Lieutenant", "Commander"]
    divisions = ["Command", "Command", "Operations", "Security", "Sciences"]
    ids = [1001, 1002, 1003, 1004, 1005]

    return names, ranks, divisions, ids


def display_menu():
    full_name = input("Enter your full name: ").strip()

    print("\n===== FLEET MANAGEMENT SYSTEM =====")
    print(f"Logged in as: {full_name}\n")

    options = [
        "Add Member",
        "Remove Member",
        "Update Rank",
        "Display Roster",
        "Search Crew",
        "Filter by Division",
        "Calculate Payroll",
        "Count Officers",
        "Exit"
    ]

    for i, option in enumerate(options, start=1):
        print(f"{i}. {option}")

    choice = input("\nSelect option: ").strip()
    return choice


def add_member(names, ranks, divs, ids):

    name = input("Enter name: ").strip()

    valid_ranks = ["Captain", "Commander", "Lt. Commander",
                   "Lieutenant", "Ensign"]

    rank = input("Enter rank: ").strip()

    if rank not in valid_ranks:
        print("Invalid rank.")
        return

    division = input("Enter division: ").strip()

    try:
        new_id = int(input("Enter unique ID number: "))
    except ValueError:
        print("ID must be a number.")
        return

    if new_id in ids:
        print("Error: ID already exists.")
        return

    names.append(name)
    ranks.append(rank)
    divs.append(division)
    ids.append(new_id)

    print("Crew member successfully added.")


def remove_member(names, ranks, divs, ids):

    try:
        remove_id = int(input("Enter Crew ID to remove: "))
    except ValueError:
        print("Invalid ID.")
        return

    if remove_id not in ids:
        print("No crew member found with that ID.")
        return

    index = ids.index(remove_id)

    print("\nCrew Member Found:")
    print(f"Name: {names[index]}")
    print(f"Rank: {ranks[index]}")
    print(f"Division: {divs[index]}")
    print(f"ID: {ids[index]}")

    confirm = input("Confirm removal? (y/n): ").strip().lower()

    if confirm == "y":
        names.pop(index)
        ranks.pop(index)
        divs.pop(index)
        ids.pop(index)
        print("Crew member removed.")
    else:
        print("Removal cancelled.")


def update_rank(names, ranks, divs, ids):

    print("\n=== RANK MODIFICATION TERMINAL ===")

    try:
        crew_id = int(input("Enter Crew ID: "))
    except ValueError:
        print("Invalid ID.")
        return

    if crew_id not in ids:
        print("Crew ID not found.")
        return

    index = ids.index(crew_id)

    print("\nCrew Member Located:")
    print(f"Name: {names[index]}")
    print(f"Current Rank: {ranks[index]}")
    print(f"Division: {divs[index]}")

    valid_ranks = [
        "Captain",
        "Commander",
        "Lt. Commander",
        "Lieutenant",
        "Ensign"
    ]

    print("\nAvailable Ranks:")
    for r in valid_ranks:
        print("-", r)

    new_rank = input("Enter new rank: ").strip()

    if new_rank not in valid_ranks:
        print("Invalid rank selection.")
        return

    confirm = input(f"Confirm change to {new_rank}? (y/n): ").strip().lower()

    if confirm == "y":
        ranks[index] = new_rank
        print("Rank successfully updated.")
    else:
        print("Update cancelled.")


def display_roster(names, ranks, divs, ids):

    if len(names) == 0:
        print("No crew members in database.")
        return

    print("\n===== STARFLEET CREW ROSTER =====")
    print("{:<6} {:<15} {:<15} {:<15}".format("ID", "Name", "Rank", "Division"))
    print("-" * 55)

    for i in range(len(names)):
        print("{:<6} {:<15} {:<15} {:<15}".format(
            ids[i], names[i], ranks[i], divs[i]
        ))


def search_crew(names, ranks, divs, ids):

    query = input("Enter name to search: ").strip().lower()
    found = False

    for i in range(len(names)):
        if query in names[i].lower():
            print("\nCrew Member Found:")
            print(f"ID: {ids[i]}")
            print(f"Name: {names[i]}")
            print(f"Rank: {ranks[i]}")
            print(f"Division: {divs[i]}")
            found = True

    if not found:
        print("No matching crew member found.")


def filter_by_division(names, ranks, divs, ids):

    division_query = input("Enter division to filter: ").strip().lower()
    found = False

    print(f"\n=== Crew in {division_query.title()} Division ===")

    for i in range(len(divs)):
        if divs[i].lower() == division_query:
            print(f"{ids[i]} - {names[i]} ({ranks[i]})")
            found = True

    if not found:
        print("No crew members found in that division.")


def calculate_payroll(ranks):

    salary_chart = {
        "Captain": 120000,
        "Commander": 95000,
        "Lt. Commander": 80000,
        "Lieutenant": 65000,
        "Ensign": 50000
    }

    total_payroll = 0

    for rank in ranks:
        total_payroll += salary_chart.get(rank, 0)

    print("\n=== PAYROLL REPORT ===")
    print(f"Total Officers: {len(ranks)}")
    print(f"Total Payroll: ${total_payroll:,}")


def count_officers(ranks):

    high_ranks = ["Captain", "Commander"]
    count = 0

    for rank in ranks:
        if rank in high_ranks:
            count += 1

    print("\n=== OFFICER ANALYSIS ===")
    print(f"High Ranking Officers: {count}")


def main():

    names, ranks, divs, ids = init_database()

    while True:

        choice = display_menu()

        if choice == "1":
            add_member(names, ranks, divs, ids)
        elif choice == "2":
            remove_member(names, ranks, divs, ids)
        elif choice == "3":
            update_rank(names, ranks, divs, ids)
        elif choice == "4":
            display_roster(names, ranks, divs, ids)
        elif choice == "5":
            search_crew(names, ranks, divs, ids)
        elif choice == "6":
            filter_by_division(names, ranks, divs, ids)
        elif choice == "7":
            calculate_payroll(ranks)
        elif choice == "8":
            count_officers(ranks)
        elif choice == "9":
            print("\nShutting down Fleet Management System...")
            break
        else:
            print("Invalid option. Please select 1-9.")


if __name__ == "__main__":
    main()