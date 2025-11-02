# TextBasedGame.py
# Author: Ahsan N.

"""
Samurai Adventure Text-Based Game
Navigate rooms, collect items, and avoid the villain until you are ready!
Industry best practices are followed: clear variable names, modular code, inline comments, and function usage.
"""

def show_status(current_room, inventory, room_dict, item_dict):
    """
    Display the player's current status: room, inventory, and item in the room.
    """
    print(f"\nYou are in the {current_room}.")
    print(f"Inventory: {', '.join(inventory) if inventory else 'Empty'}")
    # Show item in current room, if any and not already collected
    item = item_dict.get(current_room, None)
    if item and item not in inventory:
        print(f"You see a {item} here.")
    print("Available directions:", ', '.join(room_dict[current_room].keys()))
    print("Commands: 'go [direction]', 'get [item]', or 'exit'.")

def show_commands():
    """
    Display the possible commands for the player.
    """
    print("Type 'go [direction]' (e.g., 'go North'), 'get [item]' (e.g., 'get Katana'), or 'exit' to quit.")

def main():
    # Map: rooms and their connections
    room_dict = {
        'Dojo Courtyard': {'North': 'Bamboo Forest', 'East': 'Cherry Blossom Grove'},
        'Bamboo Forest': {'South': 'Dojo Courtyard', 'East': 'Mountain Pass'},
        'Mountain Pass': {'West': 'Bamboo Forest', 'South': 'Samurai Armory'},
        'Samurai Armory': {'North': 'Mountain Pass', 'West': 'Ancient Library'},
        'Ancient Library': {'East': 'Samurai Armory', 'South': 'Tea House'},
        'Tea House': {'North': 'Ancient Library', 'East': 'Pagoda Courtyard'},
        'Cherry Blossom Grove': {'West': 'Dojo Courtyard', 'South': 'Pagoda Courtyard'},
        'Pagoda Courtyard': {'West': 'Tea House', 'North': 'Cherry Blossom Grove', 'East': 'Final Shrine'},
        'Final Shrine': {'West': 'Pagoda Courtyard'}
    }

    # Items placed in rooms
    item_dict = {
        'Bamboo Forest': 'Jade Amulet',
        'Mountain Pass': 'Healing Herbs',
        'Samurai Armory': 'Warrior’s Helmet',
        'Ancient Library': 'Ancient Scroll',
        'Tea House': 'Ceremonial Armor',
        'Cherry Blossom Grove': 'Sacred Katana'
    }
    # Villain room (no item)
    villain_room = 'Final Shrine'
    villain_name = 'Ronin Kuro'

    # Required items to win
    required_items = set(item_dict.values())

    # Player state
    current_room = 'Dojo Courtyard'
    inventory = []

    print("Welcome to the Samurai Adventure!")
    show_commands()

    # Main gameplay loop
    while True:
        show_status(current_room, inventory, room_dict, item_dict)
        command = input(">> ").strip()

        # Normalize input
        command_lower = command.lower()

        # Exit command
        if command_lower == 'exit':
            print("You leave the path of the samurai. Farewell.")
            break

        # Movement command
        elif command_lower.startswith('go '):
            direction = command[3:].strip().capitalize()
            if direction in room_dict[current_room]:
                current_room = room_dict[current_room][direction]
                print(f"You travel {direction} to the {current_room}.")
                # Check for villain
                if current_room == villain_room:
                    if set(inventory) >= required_items:
                        print(f"\nYou confront {villain_name} in the {villain_room} with all sacred items!")
                        print("With your power restored, you defeat the villain and restore honor!")
                        print("Congratulations! You WIN!")
                        break
                    else:
                        print(f"\nYou confront {villain_name} in the {villain_room} unprepared...")
                        print("Defeated by the villain, your quest ends in failure.")
                        print("Game Over. You LOSE.")
                        break
            else:
                print("You cannot go that way.")

        # Get item command
        elif command_lower.startswith('get '):
            item_name = command[4:].strip()
            item_in_room = item_dict.get(current_room, None)
            if item_in_room and item_name.lower() == item_in_room.lower() and item_in_room not in inventory:
                inventory.append(item_in_room)
                print(f"You picked up the {item_in_room}!")
                # Optionally: remove item from room_dict (not needed, as inventory check suffices)
                # Check win condition after pickup (optional: if all items collected, give a message)
                if set(inventory) == required_items and current_room == villain_room:
                    print(f"\nYou confront {villain_name} in the {villain_room} with all sacred items!")
                    print("With your power restored, you defeat the villain and restore honor!")
                    print("Congratulations! You WIN!")
                    break
            elif item_in_room and item_in_room in inventory:
                print("You have already collected this item.")
            else:
                print("No such item here to get.")

        # Invalid command
        else:
            print("Invalid command. Try again.")
            show_commands()

if __name__ == "__main__":
    main()