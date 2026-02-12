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

def remove_member(names, ranks, divs, ids):

       try:
            remove_id = int(input("Enter Crew ID to remove: "))
        except ValueError:
            print("Invalid ID. Must be a number.")
        return

    if remove_id not in ids:
        print("No crew member found with that ID.")
        return

    index = ids.index(remove_id)

    print("\n⚠ Crew Member Found:")
    print(f"Name: {names[index]}")
    print(f"Rank: {ranks[index]}")
    print(f"Division: {divs[index]}")
    print(f"ID: {ids[index]}")

    confirm = input("\nConfirm removal? (y/n): ").strip().lower()

    if confirm == "y":
        names.pop(index)
        ranks.pop(index)
        divs.pop(index)
        ids.pop(index)
        print("🚀 Crew member successfully removed from the fleet.")
    else:
        print("Removal cancelled.")#
def update_rank(names, ranks, divs, ids):
    
    print("\n=== RANK MODIFICATION TERMINAL ===")

    try:
            crew_id = int(input("Enter Crew ID: "))
    except ValueError:
            print("Invalid ID. Must be numeric.")
    return

    if crew_id not in ids:
            print("Crew ID not found in system.")
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

new_rank = input("\nEnter new rank: ").strip()

 if new_rank not in valid_ranks:
        print("Invalid rank selection.")
    
        return

confirm = input(f"Confirm promotion/demotion to {new_rank}? (y/n): ").strip().lower()

if confirm == "y":
        ranks[index] = new_rank
        print("🟢 Rank successfully updated.")
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

        print(f"\n=== Crew in {division_query.title()} Division ===")

        found = False

        for i in range(len(divs)):
            if divs[i].lower() == division_query:
                print(f"{ids[i]} - {names[i]} ({ranks[i]})")
                found = True

        if not found:
            print("No crew members found in that division.")     