import time
import random


def input_check(question: str, function, confirmation: str):  
  yes_no = input(question)

  if yes_no.lower() in ["n", "no"]:
    function()
  elif yes_no.lower() in ["y", "yes"]:
    print(confirmation)
    time.sleep(1)
  else:
    print("Invalid input. Please enter YES or NO.")
    input_check(question, function, confirmation)


def rules():
  print("INPUT GUIDE:")
  time.sleep(1)
  print("For yes or no questions, answer with y, n, yes, or no.")
  time.sleep(2)
  print("Capitalization does not matter.")
  time.sleep(3)
  print("For the dungeon, enter your movement direction with:")
  time.sleep(1)
  print("N for North, S for South, E for East, and W for West.")
  time.sleep(2)
  print("You may type stop or quit at any time to exit the game.")
  time.sleep(3)
  
#Defines the dungeon rooms and traversal rules
class Dungeon():
  def __init__(self):
    self.name = input('What is your name?\n')
    if self.name in ["quit", "stop"]:
      quit()
    self.holding_sword = False
    self.holding_shield = False
    self.x = 0
    self.y = 0
    self.done = False
    self.east = False
    self.west = False
    self.north = False
    self.south = False
    self.shield_room = True
    self.sword_room = True
    self.minotaur = True
    self.cookies = True
    
  #Inputs character name into strings automatically with {name}
  def print_msg(self, msg):
    print(msg.format(name=self.name))

  #Updates position then displays current room 
  def move(self,x=0,y=0):
    self.x += x
    self.y += y
    if (self.x,self.y) == (1,0):
      self.print_msg("{name} enters a spacious room.")
      time.sleep(1.5)
      print("There are {} lit candles in the room." .format(random.choice(range(2,14))))
      time.sleep(0.5)
      print('There are 2 ways you can go. North or East.')
      self.north = True
      self.south = False
      self.east = True
      self.west = False
      
    elif (self.x,self.y) == (1,1):
      self.print_msg("{name} enters another spacious room.")
      time.sleep(1.5)
      print("There are {} ghosts floating in the room." .format(random.choice(range(2,10))))
      time.sleep(0.5)
      print('There is a room to the West, the large room you started in to the South, and a smaller passageway to the North.')
      self.east = False
      self.south = True
      self.north = True
      self.west = True
      
    elif (self.x,self.y) == (1,2):
      self.print_msg("{name} enters a passageway.")
      time.sleep(1.5)
      print("There is a {} year old man. He greets you cheerily, and vanishes." .format(random.choice(range(20,100))))
      time.sleep(0.5)
      print('The passageway leads North and South.')
      self.east = False
      self.south = True
      self.north = True
      self.west = False
      
    elif (self.x,self.y) == (1,3):
      self.print_msg("{name} enters a corner room.")
      time.sleep(1.5)
      print("There are spoons on the walls. {} to be exact." .format(random.choice(range(100,1000))))
      time.sleep(0.5)
      print('There are passageways to the East and South.')
      self.east = True
      self.south = True
      self.north = False
      self.west = False
      
    elif (self.x,self.y) == (2,0):
      self.print_msg("{name} enters a small room.")
      time.sleep(1.5)
      print("There are {} bones on the floor, and a large unidentifiable mass blocking the East wall." .format(random.choice(range(2,14))))
      time.sleep(0.5)
      print('There are 2 ways you can go. North, or back West.')
      self.north = True
      self.south = False
      self.east = False
      self.west = True
      
    elif (self.x,self.y) == (2,1):
      self.print_msg("{name} enters a dungeon-like chamber.")
      time.sleep(1.5)
      print("There are {} strange runes on the walls." .format(random.choice(range(2,2000))))
      time.sleep(0.5)
      print('To your North is a blank wall. To the West is an ominous-looking locked door. A large window covers the East wall.')
      self.north = True
      self.south = True
      self.east = False
      if self.holding_sword:
        self.west = True
      else:
        self.west = False
        
    elif (self.x,self.y) == (2,2):
      self.print_msg("{name} slips through a hidden door.")
      time.sleep(1.5)
      print("There are {} skeletons on the cieling." .format(random.choice(range(2,5))))
      time.sleep(0.5)
      print("There is a window high up on the wall, letting a shaft of light fall in.") 
      time.sleep(1)
      if self.sword_room:
        print("In the center of the room is a sword on a pedestal.\n")
        time.sleep(.5)
        print("""
         />___________________________________
[--------[                                   /
[--------[ _________________________________/
         \>""")
        yes_no = input("Do you take it? \n")
        if yes_no.lower() in ["y", "yes"]:
          self.holding_sword = True
          self.sword_room = False
          print("You pick up the sword and give it a few swings. It feels nice.")
        elif yes_no.lower() in ["n", "no"]:
          print("You leave it be. You can always come back here later.")
        else:
          self.print_msg("Invalid input. {name} decides to grab the sword.")
          self.holding_sword = True
          self.sword_room = False
      else:
        print("There is nothing left to do here.")
      time.sleep(1)
      print("You may go back the way you came.")
      self.north = False
      self.south = True
      self.east = False
      self.west = False
      
    elif (self.x,self.y) == (2,-2):
      if self.cookies == True:
        self.print_msg("{name} fashions the horns of the Minotaur into a helmet.")
        self.minotaur = False
        time.sleep(1.5)
        print("There is a plate of warm cookies for you.")
        time.sleep(0.5)
        self.print_msg("{name} eats all the cookies.")
        self.cookies = False
        time.sleep(0.5)
      print("You made it to the end of the maze!")
      time.sleep(1)
      print("You can leave now to the South, if you wish.")
      self.north = True
      self.south = True
      self.east = False
      self.west = False
      
    elif (self.x,self.y) == (2,-1):
      self.print_msg("{name} enters a dark room.")
      time.sleep(1.5)
      if self.minotaur == True:
        print("There are is a Minotaur blocking the maze's exit (south).")
        print(""" 
     .      .                                              
     |\____/|                                              
    (\|----|/)                                             
     \ 0  0 /      
      |    |                                               
   ___/\../\____       
  /     --       \                                         
 /  \         /   \                                        
|    \___/___/(   |                                        
\   /|  }{   | \  )                                        
 \  ||__}{__|  |  |                                        
  \  |;;;;;;;\  \ / \_______                               
   \ /;;;;;;;;| [,,[|======'                               
     |;;;;;;/ |     /                                      
     ||;;|\   |                                            
     ||;;/|   /                                            
     \_|:||__|                                             
      \ ;||  /                                             
      |= || =|                                             
      |= /\ =|                                             
      /_/  \_\                """)
        time.sleep(0.5)
        
        self.west = False
        self.north = False
        if self.holding_shield == True:
          print("Your shield gives you some breathing room. You could turn back.")
          self.east = True
        elif self.holding_shield == False:
          print("You can't go back. The Minotaur would get to you before then.")
          self.east = False
        time.sleep(0.5)

        if self.holding_sword == True:
          print("Your sword could easily kill the Minotaur.")
          self.south = True
        elif self.holding_sword == False:
          print("You have no way to kill the Minotaur and escape.")
          self.south = False
        time.sleep(1)

        if self.south == False and self.north == False:
          time.sleep(1)
          print("You are unequipped, and the Minotaur runs at you. Very. Very. Fast. With its horns out.")
          time.sleep(3)
          print(""" 
        
 _____                        _____                
|  __ \                      |  _  |               
| |  \/ __ _ _ __ ___   ___  | | | |_   _____ _ __ 
| | __ / _` | '_ ` _ \ / _ \ | | | \ \ / / _ \ '__|
| |_\ \ (_| | | | | | |  __/ \ \_/ /\ V /  __/ |   
 \____/\__,_|_| |_| |_|\___|  \___/  \_/ \___|_|   
                                                   
                                                   
""")
          self.done = True
      else:
        print("The minotaur's remains are on the floor.")
        self.south = True
        self.east = True
        self.north = False
        self.west = True  
        
    elif (self.x, self.y) == (2,-3):
      self.print_msg("{name} escaped!")
      yes_no = input("Do you wish to play again?\n")
      if yes_no.lower() == "n" or yes_no.lower() == "no":
        self.print_msg("See you next time, {name}!")
        print(""" 
        
 _____                        _____                
|  __ \                      |  _  |               
| |  \/ __ _ _ __ ___   ___  | | | |_   _____ _ __ 
| | __ / _` | '_ ` _ \ / _ \ | | | \ \ / / _ \ '__|
| |_\ \ (_| | | | | | |  __/ \ \_/ /\ V /  __/ |   
 \____/\__,_|_| |_| |_|\___|  \___/  \_/ \___|_|   
                                                   
                                                   
""")
        self.done=True
      elif yes_no.lower() in ["y", "yes"]:
        self.x=0
        self.y=0
        run_game(self)
      else:
        print("Invalid input. Shutting down...")
        print(""" 
        
 _____                        _____                
|  __ \                      |  _  |               
| |  \/ __ _ _ __ ___   ___  | | | |_   _____ _ __ 
| | __ / _` | '_ ` _ \ / _ \ | | | \ \ / / _ \ '__|
| |_\ \ (_| | | | | | |  __/ \ \_/ /\ V /  __/ |   
 \____/\__,_|_| |_| |_|\___|  \___/  \_/ \___|_|   
                                                   
                                                   
""")
        self.done=True
        
    elif (self.x,self.y) == (2,3):
      self.print_msg("{name} enters a small passageway.")
      time.sleep(0.5)
      print("There are {} neodymium magnets on the ground." .format(random.choice(range(2,4))))
      time.sleep(1.5)
      print('You can only go East or West.')
      self.north = False
      self.south = False
      self.east = True
      self.west = True
      
    elif (self.x,self.y) == (3,3):
      self.print_msg("{name} enters another corner room.")
      time.sleep(0.5)
      print("There are {} layers of niobium foil on the wall to the north." .format(random.choice(range(2,4))))
      time.sleep(1.5)
      print('You can only go West or South.')
      self.north = False
      self.south = True
      self.east = False
      self.west = True
      
    elif (self.x,self.y) == (3,2):
      self.print_msg("{name} enters another passageway.")
      time.sleep(0.5)
      print("There are {} chunks of dubnium." .format(random.choice(range(3,14))))
      time.sleep(1.5)
      print('You can only go South or North.')
      self.north = True
      self.south = True
      self.east = False
      self.west = False
      
    elif (self.x,self.y) == (3,1):
      self.print_msg("{name} enters yet ANOTHER passageway.")
      time.sleep(1.5)
      print("Just kidding it's a room.")
      time.sleep(0.5)
      print("You can only go South or North. There's a painting of a sunrise on the East wall though.")
      self.north = True
      self.south = True
      self.east = False
      self.west = False
      
    elif (self.x,self.y) == (3,0):
      self.print_msg("{name} enters a small playgound.")
      time.sleep(1.5)
      print("There is nobody here. Strange.")
      time.sleep(0.5)
      print("You can only go South or North. There's a lazy detail on the floor though.")
      self.north = True
      self.south = True
      self.east = False
      self.west = False
      
    elif (self.x,self.y) == (3,-1):
      self.print_msg("{name} enters a thingamabobber... Oh wait it's a room.")
      time.sleep(1.5)
      print("There are 2 ways out..")
      time.sleep(0.5)
      print("To the North is a room, to the West is TREASURE!!!!!!!")
      time.sleep(1)
      print("Just kidding it's a room.")
      self.north = True
      self.south = False
      self.east = False
      self.west = True
      
    elif (self.x,self.y) == (0,1):
      self.print_msg("{name} walks through an archway.")
      time.sleep(1.5)
      print("There are no other doors in this room.")
      time.sleep(0.5)
      if self.shield_room:  
        print("""
   _________________________ 
  |<><><>     |  |    <><><>|
  |<>         |  |        <>|
  |           |  |          |
  |  (______ <\-/> ______)  |
  |  /_.-=-.\| " |/.-=-._\  | 
  |   /_    \(o_o)/    _\   |
  |    /_  /\/ ^ \/\  _\    |
  |      \/ | / \ | \/      |
  |_______ /((( )))\ _______|
  |      __\ \___/ /__      |
  |--- (((---'   '---))) ---|
  |           |  |          |
  |           |  |          |
  :           |  |          :     
  \<>        |  |       <>/      
    \<>       |  |      <>/       
    \<>      |  |     <>/       
      `\<>    |  |   <>/'         
        `\<>  |  |  <>/'         
          `\<>|  |<>/'         
            `-.  .-`           
              '--'         """)
        yes_no = input("There is a shield in this room. Do you take it?\n")
        if yes_no.lower() in ["y", "yes"]:
          self.holding_shield = True
          self.shield_room = False
          print("You pick up the shield. It fits comfortably on your arm.")
        elif yes_no.lower() in ["n", "no"]:
          print("You leave it be. You can always come back here later.")
        else:
          self.print_msg("Invalid input. {name} decides to take the shield.")
          self.holding_shield = True
          self.shield_room = False

      else:
        print("There is nothing else to do here.")
      time.sleep(1)
      print("You may go back the way you came.")
      self.north = False
      self.south = False
      self.east = True
      self.west = False
    
    else:
      print("Oh no! Something went wrong! (This room does not exist... yet.)\n")
      print("Send a screenshot of this message and these coordinates to the developers\nso we can figure out what went wrong!\n")
      print("{},{}" .format(self.x,self.y))
      self.done = True

      
def run_game(dungeon_obj):
  dungeon_obj.print_msg("{name} is in a room. There is only one way out. Do you leave?")
  yes_no = input()
  if yes_no.lower() in ["n", "no"]:
    dungeon_obj.print_msg("{name} wastes some time admiring the walls of the room.")
    time.sleep(3)
    dungeon_obj.print_msg("{name} decides to leave the room after all.")
    time.sleep(1)
    print("The door slams shut behind you.")
    time.sleep(1)
    dungeon_obj.move(x=1)
  elif yes_no.lower() in ["yes", "y"]:
    print("The door slams shut behind you.")
    time.sleep(1)
    dungeon_obj.move(x=1)
  elif yes_no.lower() in ["quit", "stop"]:
    dungeon_obj.done = True
  else:
    dungeon_obj.print_msg("Invalid input. {name} decides to leave the room.")
    time.sleep(1)
    print("The door slams shut behind you.")
    time.sleep(1)
    dungeon_obj.move(x=1)
  
  #Takes directional input while the game is marked as not completed
  while not dungeon_obj.done:
    direction = input()
    if direction.lower() == "n" and dungeon_obj.north:   
      dungeon_obj.print_msg("{name} goes North.")
      dungeon_obj.move(y=1)
    elif direction.lower() == "w" and dungeon_obj.west:
      dungeon_obj.print_msg("{name} goes West.")
      dungeon_obj.move(x=-1)
    elif direction.lower() == "s" and dungeon_obj.south:
      dungeon_obj.print_msg("{name} goes South.")
      dungeon_obj.move(y=-1)
    elif direction.lower() == "e" and dungeon_obj.east:
      dungeon_obj.print_msg("{name} goes East.")
      dungeon_obj.move(x=1)
    #For debugging, will display coordinates
    elif direction.lower() == "printw" and dungeon_obj.west:
      dungeon_obj.print_msg("{name} goes West.")
      dungeon_obj.move(x=-1)
      print("{},{}" .format(dungeon_obj.x,dungeon_obj.y))
    elif direction.lower() == "printn" and dungeon_obj.north:
      dungeon_obj.print_msg("{name} goes North.")
      dungeon_obj.move(y=1)
      print("{},{}" .format(dungeon_obj.x,dungeon_obj.y))
    elif direction.lower() == "printe" and dungeon_obj.east:
      dungeon_obj.print_msg("{name} goes East.")
      dungeon_obj.move(x=1)
      print("{},{}" .format(dungeon_obj.x,dungeon_obj.y))
    elif direction.lower() == "prints" and dungeon_obj.south:
      dungeon_obj.print_msg("{name} goes South.")
      dungeon_obj.move(y=-1)
      print("{},{}" .format(dungeon_obj.x,dungeon_obj.y))
    elif direction.lower() == "print":
      print("{},{}" .format(dungeon_obj.x,dungeon_obj.y))
    elif direction.lower() not in ['n', 's', 'e', 'w']:
      print("Invalid input.")
    elif direction.lower() in ["stop", "quit"]:
      print("Shutting down...")
      dungeon_obj.done = True
    else:
      print("You cannot go that way.")

#Code run on compile starts here
maze = Dungeon()
maze.print_msg("Welcome, {name}.")
time.sleep(1)
input_check("Do you know the rules?\n", rules, "Ok. Starting game...") 
run_game(maze)
