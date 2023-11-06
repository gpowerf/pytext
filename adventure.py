'''
************************************************************************
Text adventure template for Python
************************************************************************

This is not a full text adventure
it provides you with a template so 
that you can write your own adventure
using Python

I've created similar templates for Commodore Basic and XC=BASIC V2, 
see: https://github.com/gpowerf
************************************************************************

'''

# This is a text adventure template written in Python
# It follows a similar architecture as the XC=BASIC project
# https://github.com/gpowerf/XCBASICAdventureTemplate/blob/main/architecture.txt

# Import the modules that we need
import sys # For system functions such as exit
import json # For saving and loading data
import random # For generating random numbers

# Define some constants
MAX_INVENTORY = 10 # The maximum number of items that the player can carry
MAX_HEALTH = 100 # The maximum health of the player
SAVE_FILE = "save.json" # The name of the file where we save the game data

# Define some global variables
game_over = False # A flag to indicate if the game is over
current_room = None # The current room where the player is
inventory = [] # The list of items that the player has
health = MAX_HEALTH # The current health of the player

# Define some data structures to store the game data
# We use dictionaries to store key-value pairs of information
# We use lists to store multiple values of the same type

# A dictionary of commands and their synonyms
commands = {
    "look": ["look", "examine", "inspect", "see"],
    "go": ["go", "move", "walk", "travel"],
    "take": ["take", "get", "grab", "pick"],
    "drop": ["drop", "leave", "discard", "put"],
    "use": ["use", "apply", "activate", "employ"],
    "inventory": ["inventory", "items", "stuff", "bag"],
    "help": ["help", "hint", "guide", "assist"],
    "save": ["save", "store", "record", "keep"],
    "load": ["load", "restore", "resume", "retrieve"],
    "quit": ["quit", "exit", "stop", "end"]
}

# A dictionary of directions and their synonyms
directions = {
    "north": ["north", "n"],
    "south": ["south", "s"],
    "east": ["east", "e"],
    "west": ["west", "w"]
}

# A dictionary of rooms and their properties
rooms = {
    # Each room has a name, a description, a list of exits, and a list of items
    # Each exit has a direction and a destination room
    # Each item has a name, a description, and a flag to indicate if it is usable or not
    # Example:
    #   {
    #       name: "",
    #       description: "",
    #       exits: [
    #           {
    #               direction: "",
    #               destination: ""
    #           }
    #       ],
    #       items: [
    #           {
    #               name: "",
    #               description: "",
    #               usable: True or False
    #           }
    #       ]
    #   }
    
    # The starting room of the game
    "entrance": {
        name: "Entrance",
        description: """You are standing at the entrance of an ancient temple.
        You see a large wooden door with strange symbols carved on it.
        There is a torch on the wall next to the door.""",
        exits: [
            {
                direction: "north",
                destination: "hallway"
            }
        ],
        items: [
            {
                name: torch,
                description: """A torch that provides some light in the dark.
                It looks like it can be taken off the wall.""",
                usable: True
            }
        ]
        
        }
   

}


def look():
  """Describe the current room to the player."""
  print(current_room.description)

# Define other actions here, such as go(), take(), drop(), use(), inventory(), help(), save(), load(), and quit().

def parse_command(command):
  """Parse the command and determine the player's desired action.

  Args:
    command: The player's command.

  Returns:
    A tuple containing the action and parameters.
  """

  # Split the command into words.
  words = command.split()

  # Get the first word, which is the action.
  action = words[0].lower()

  # Get the rest of the words, which are the parameters.
  params = words[1:]

  # Return the action and parameters.
  return action, params

def game_loop():
  # Initialize the game state.
  player = Player()
  current_room = rooms["entrance"]

  # Start the game loop.
  while True:

    # Prompt the player to enter a command.
    command = input("> ")

    # Parse the command and determine the player's desired action.
    action, params = parse_command(command)

    # Execute the action and update the game state accordingly to  

