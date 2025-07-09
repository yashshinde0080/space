import sys
import time

def typewriter(text, delay=0.03):
    """Prints text with a typewriter effect."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

# Game data
rooms = {
    'Bridge': {
        'description': "You are on the bridge of the starship 'Odyssey'.\nConsoles blink with stellar data. The captain's chair awaits.\nA large screen shows the silent expanse of deep space.",
        'exits': {'south': 'Engine Room', 'east': 'Living Quarters'},
        'items': ['logbook']
    },
    'Engine Room': {
        'description': "The air hums with the power of the ship's warp core.\nIt glows with a mesmerizing blue light. Pipes and conduits line the walls.",
        'exits': {'north': 'Bridge'},
        'items': []
    },
    'Living Quarters': {
        'description': "This is where the crew sleeps and relaxes.\nThere are several sleeping pods and a small recreational area.",
        'exits': {'west': 'Bridge', 'north': 'Cargo Bay'},
        'items': []
    },
    'Cargo Bay': {
        'description': "A vast, cavernous room filled with crates and containers.\nA strange, faint humming seems to come from one of the containers.",
        'exits': {'south': 'Living Quarters'},
        'items': ['Cosmic Key']
    }
}

# Player state
current_room = 'Bridge'
inventory = []

def show_intro():
    """Displays the game's introduction."""
    typewriter("**************************************")
    typewriter("*      SPACE ODYSSEY: THE GAME     *")
    typewriter("**************************************")
    typewriter("You are the last surviving crew member of the starship Odyssey.")
    typewriter("Your mission: Find the Cosmic Key to unlock the path back to Earth.")
    typewriter("Type 'help' for a list of commands.")
    print("\n" + "="*40 + "\n")


def show_status():
    """Displays the player's current status."""
    print(f"Location: {current_room}")
    typewriter(rooms[current_room]['description'])
    print("\nExits: " + ", ".join(rooms[current_room]['exits'].keys()))
    if rooms[current_room]['items']:
        print("You see: " + ", ".join(rooms[current_room]['items']))
    print("-" * 40)


def process_command(command):
    """Processes the player's command."""
    global current_room
    verb = command[0]

    if verb == 'quit':
        typewriter("See you, space cowboy...")
        sys.exit()

    elif verb == 'help':
        print("Commands:")
        print("  go [direction]  - Move to a new room (e.g., 'go north')")
        print("  look            - Examine your surroundings")
        print("  get [item]      - Pick up an item (e.g., 'get logbook')")
        print("  inventory       - Check your inventory")
        print("  quit            - Exit the game")

    elif verb == 'look':
        show_status()

    elif verb == 'inventory':
        if not inventory:
            print("Your inventory is empty.")
        else:
            print("You are carrying: " + ", ".join(inventory))

    elif verb == 'go':
        if len(command) < 2:
            print("Go where?")
            return
        direction = command[1]
        if direction in rooms[current_room]['exits']:
            current_room = rooms[current_room]['exits'][direction]
            show_status()
        else:
            print("You can't go that way.")

    elif verb == 'get':
        if len(command) < 2:
            print("Get what?")
            return
        item = command[1]
        if item in rooms[current_room]['items']:
            inventory.append(item)
            rooms[current_room]['items'].remove(item)
            print(f"You picked up the {item}.")
            if item == 'Cosmic Key':
                typewriter("\nYou found the Cosmic Key! A hidden panel on your wristband opens up.")
                typewriter("You insert the key. A starmap appears, showing a clear route back to Earth!")
                typewriter("\nCongratulations, you have won the game!", delay=0.05)
                sys.exit()
        else:
            print("You don't see that here.")

    else:
        print("Unknown command. Type 'help' for a list of commands.")


def main():
    """The main game loop."""
    show_intro()
    show_status()
    while True:
        try:
            command = input('> ').lower().strip().split()
            if command:
                process_command(command)
        except (EOFError, KeyboardInterrupt):
            print("\n")
            typewriter("Exiting game.")
            sys.exit()

if __name__ == '__main__':
    main()
