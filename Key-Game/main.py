def show_start_screen():
  print("Welcome to the Adventure!")
  print("Enter 'help' to show a list of commands.")

def show_help():
  print("Available commands:")
  print("  go [direction]")
  print("  get [item]")
  print("  use [item]")
  print("  look")
  print("  inventory")
  print("  quit")

def show_end_screen():
  print("Thank you for playing the Adventure!")

def main():
  show_start_screen()

  # Set up the game state
  current_room = "outside"
  inventory = []

  while True:
    # Get the player's input
    command = input("> ").lower().strip()

    if command == "help":
      show_help()
    elif command == "go north":
      if current_room == "outside":
        current_room = "inside"
        print("You go inside.")
      else:
        print("You can't go that way.")
    elif command == "go south":
      if current_room == "inside":
        current_room = "outside"
        print("You go outside.")
      else:
        print("You can't go that way.")
    elif command == "get key":
      if current_room == "outside" and "key" not in inventory:
        inventory.append("key")
        print("You pick up the key.")
      else:
        print("You can't do that.")
    elif command == "use key":
      if "key" in inventory:
        inventory.remove("key")
        print("You unlock the door.")
      else:
        print("You don't have the key.")
    elif command == "look":
      if current_room == "outside":
        print("You are standing outside a locked door. There is a key on the ground.")
      else:
        print("You are inside a room.")
    elif command == "inventory":
      print("You are carrying:")
      for item in inventory:
        print(" - " + item)
    elif command == "quit":
      break
    else:
      print("I don't understand.")

  show_end_screen()

main()
