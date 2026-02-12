def shlawg_database():
    
    names = ["Picard", "Riker", "Data", "Worf", "Crusher"]
    ranks = ["Captain", "Commander", "Lt. Commander", "Lieutenant", "Commander"]
    divisions = ["Command", "Command", "Operations", "Security", "Sciences"]
    ids = [1001, 1002, 1003, 1004, 1005]

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
        print("Invalid rank. Must be one of:")
        for r in valid_ranks:
            print("-", r)
        return

        division = input("Enter division (Command/Operations/Security/Sciences): ").strip()

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

        print("Crew member successfully added.")#

