#######################
### Game Components ###
# 1: GameObject
# 2: Room
# 3: Game
#######################

# Class that creates game objects
class GameObject() :

  ## Initializing a GameObject ##
  def __init__(self, name, appearance, feel, smell) :

    self.name = name
    self.appearance = appearance
    self.feel = feel
    self.smell = smell
  
  ## Methods for GameObject ##

  # Returns a string describing the appearance of an object
  def look(self) :

    return f"You look at the {self.name}. {self.appearance}\n"

  # Returns a string describing the feeling of an object
  def touch(self) :

    return f"You touch the {self.name}. {self.feel}\n"

  # Returns a string describing the smell of an object
  def sniff(self) :

    return f"You sniff the {self.name}. {self.smell}\n"
  
# Class that creates the room of the game
class Room() :

  ## Initializing a Room ##
  def __init__(self, escape_code, game_objects) :

    self.escape_code = escape_code
    self.game_objects = game_objects

  ## Methods for Room ##

  # Checks to see if the code they have is the escape code
  def check_code(self, code) :

    return self.escape_code == code

  # Returns a list of all game object names in the room
  def get_game_object_names(self) :

    names = []
    for object in self.game_objects :
      names.append(object.name)
    return names

# Class that creates the game
class Game() :

  ## Initializing the Game ##
  def __init__(self) :

    self.attempts = 0
    objects = self.create_objects()
    self.room = Room(731, objects)

  # Creating and placing the game objects into the game
  def create_objects(self) :
    
    return [
      GameObject(
          "Sweater",
          "It's a blue sweater that had the number 12 stitched on it.",
          "Someone has unstitched the second number, leaving only the 1.",
          "The sweater smells of laundry detergent."),
        GameObject(
          "Chair", 
          "It's a wooden chair with only 3 legs.",
          "Someone had deliberately snapped off one of the legs.",
          "It smells like old wood."),
        GameObject(
          "Journal",
          "The final entry states that time should be hours then minutes then seconds (H-M-S).",
          "The cover is worn and several pages are missing.",
          "It smells like musty leather."),
        GameObject(
          "Bowl of soup", 
          "It appears to be tomato soup.",
          "It has cooled down to room temperature.",
          "You detect 7 different herbs and spices."),
        GameObject(
          "Clock", 
          "The hour hand is pointing towards the soup, the minute hand towards the chair, and the second hand towards the sweater.",
          "The battery compartment is open and empty.",
          "It smells of plastic."),
    ]
  
  # Runs main game loop
  def take_turn(self) :

    prompt = self.get_room_prompt()
    selection = int(input(prompt))
    if selection >= 1 and selection <= 5 :
      self.select_object(selection - 1)
      # Using recursion
      self.take_turn()
    else :
      is_code_correct = self.guess_code(selection)
      if is_code_correct :
        print("Congratulations, you win!")
      else :
        if self.attempts == 3 :
          print("Game over, you ran out of guesses. Better luck next time!")
        else :
          print(f"Incorrect, you have used {self.attempts}/3 attempts.\n")
          # Using recursion
          self.take_turn()

  # Return a prompt string asking the user to enter the escape code or select/interact with one of the game objects 
  def get_room_prompt(self) :

    prompt = "Enter the 3 digit lock code or choose an item to interact with:\n"
    names = self.room.get_game_object_names()
    index = 1

    for name in names :
      prompt += f"{index}: {name}\n"
      index += 1

    return prompt

  # Allows the user to select a chosen object
  def select_object(self, index) :

    selected_object = self.room.game_objects[index]
    prompt = self.get_object_interaction_string(selected_object.name)
    interaction = input(prompt)
    clue = self.interact_with_object(selected_object, interaction)
    print(clue)
  
  # Returns a prompt string asking the user which action they want to do on the object
  def get_object_interaction_string(self, name) :

    return f"How do you want to interact with the {name} ?\n1: Look\n2: Touch\n3: Smell\n"
  
  # Returns selected interaction with an object
  def interact_with_object(self, object, interaction) :

    if interaction == "1" :
      return object.look()
    elif interaction == "2" :
      return object.touch()
    elif interaction == "3" :
      return object.sniff()
    else :
      return
  
  def guess_code(self, code) :

    if self.room.check_code(code) :
      return True
    else :
      self.attempts += 1
      return False

game = Game()

game.take_turn()