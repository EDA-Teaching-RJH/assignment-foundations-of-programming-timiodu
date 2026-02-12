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

