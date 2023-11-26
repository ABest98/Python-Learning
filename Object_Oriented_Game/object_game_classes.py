#######################
### Game Components ###
# 1: GameObject
# 2: Room
# 3: Game
#######################

class GameObject() :

  ## Initializing a GameObject ##
  def __init__(self, name, appearance, feel, smell) :
    self.name = name
    self.appearance = appearance
    self.feel = feel
    self.smell = smell
  
  ## Methods for GameObject ##
  def look(self) :
    return f"You look at the {self.name}. {self.appearance}\n"

  def touch(self) :
    return f"You touch the {self.name}. {self.feel}\n"

  def sniff(self) :
    return f"You sniff the {self.name}. {self.smell}\n"
  

class Room() :

  def __init__(self) :
    print()