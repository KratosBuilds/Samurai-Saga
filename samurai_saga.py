# Author: Ahsan Nelson
# Module Six Milestone - Samurai Adventure Game

# Dictionary linking rooms to directions
room_dict = {
    'Village': {'North': 'Bamboo Forest', 'East': 'Mountain Pass', 'South': 'River Crossing', 'West': 'Abandoned Dojo'},
    'Bamboo Forest': {'South': 'Village'},
    'Mountain Pass': {'West': 'Village'},
    'River Crossing': {'North': 'Village'},
    'Abandoned Dojo': {'East': 'Village'},
    'Tea House': {'East': 'Pagoda Courtyard'},
    'Pagoda Courtyard': {'West': 'Tea House', 'East': 'Final Shrine'},
    'Final Shrine': {'West': 'Pagoda Courtyard'}
}

# Starting room
current_room = 'Village'

# Gameplay loop
while current_room != 'exit':
    # Display current room
    print(f"\nYou are in the {current_room}.")
    print("Available directions:", ', '.join(room_dict.get(current_room, {}).keys()))
    print("Type 'go [direction]' to move or 'exit' to leave your quest.")

    # Get player input
    command = input(">> ").strip().title()

    # Handle exit command
    if command == 'Exit':
        current_room = 'exit'
        print("You leave the path of the samurai. Farewell.")
    
    # Handle movement command
    elif command.startswith('Go '):
        direction = command[3:]
        if direction in room_dict.get(current_room, {}):
            current_room = room_dict[current_room][direction]
            print(f"You travel {direction} to the {current_room}.")
        else:
            print("You cannot go that way.")
    
    # Handle invalid command
    else:
        print("Invalid command. Try 'go [direction]' or 'exit'.")

# End of game