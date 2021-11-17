from pathlib import Path

#2d Array
Map=[
     ["forest ","beach ","sandcastle"],
     ["castle ","bridge","volcano   "],
     ["village","town  ","dragon's lair   "]
    ]

#draw the map
def drawMap():
  for row in Map:
    print("| ",end="")
    for column in row:
      print(column,end = " | ")
    print("\n")

drawMap()


items={
  "beach":"a book",
  "dragon's lair":"some treasure",
  "bridge":"a rock"
}


p1=player()
while True:
  text=input("\nyou find a "+p1.place+", what do you do?\n")
  tokens=text.split()
  
  if tokens[0]=='search':
    p1.search()
  elif tokens[0]=="go":
    p1.go(tokens[1])
  elif tokens[0]=="take":
    print("Take what? Try searching your surroundings (search)")