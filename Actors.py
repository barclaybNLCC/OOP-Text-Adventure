
#maybe use a builder?
class Actor:
  name=""
  inventory=[]
  healthPoints=0
  stats = {
    "Strength": 0,
    "Dexterity": 0,
    "Constitution": 0,
    "Intelligence": 0,
    "Widsom":0,
    "Charisma":0
  }

class ItemsManager:
  items={}

  def take(self, place, actor):
    if self.place in self.items.keys():
      item = self.items.pop(place)
      print(item)
      actor.inventory.append(item)
      print("you have aquired "+ item)
    else:
      print("there's nothing to take")

  def search(self): 
    print("You search the "+self.place)
    if self.place in self.items.keys():
      for place in self.items.keys():
        if self.place == place:
          print("You find " + self.items.get(place))
          print()
          if input("Will you take it? (yes/no)")== "yes":
            self.take()
    else:
      print("You didn't find anything")

class player(Actor):
  position=[1,1]
  Map=[]
  
  place=Map[position[0]][position[1]].lower().strip()
  
  def go(self, direction):
    if direction == 'north' and self.position[0]-1>-1:
      self.position[0]-=1
      print("you travel north")
    elif direction == 'south' and self.position[0]+1<3:
      self.position[0]+=1
      print("you travel south")
    elif direction == 'east' and self.position[1]+1<3:
      self.position[1]+=1
      print("you travel east")
    elif direction == 'west' and self.position[0]-1>-1:
      self.position[1]-=1
      print("you travel west")
    else:
      print("I can't do that")
    self.place=Map[self.position[0]][self.position[1]].strip()

class Enemy(Actor):
  pass

  
class NPC(Actor):
  dialogueFilename=""
  def __init__(self, name):
    #set name and filename
    self.name = name
    self.dialogueFilename=self.name+"Dialogue"
    
    #create a path object
    path = Path.path(self.dialogueFilename)
    print("test")
    if not path.is_file():
      with open(self.dialogueFilename + ".txt","w") as f:
          f.write("TODO-write dialogue")
    else:
      pass
