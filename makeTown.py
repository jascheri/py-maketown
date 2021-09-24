import random
#global variables
houseBase = 100;
brown = makeColor(139,69,19)

def drawHouse(house, origin, scale):
    x = origin[0]
    y = origin[1]
    size = int(houseBase*scale)
    brickStep = int(size*.1)
    doorScale = int(size*.2)
   
    # Deocrate the body with bricks
    stagger = false
    for _y in range(y, y+size, brickStep):
      for _x in range(x, x+size, brickStep*2):
        # if the x position is at the start and this is a staggered row
        if (_x == x) and (stagger == true):
          makeBrick(house,_x, _y, brickStep, true)
        # else if the x position is at the last position and this is a staggered row
        elif (_x + brickStep*2 == x+size) and (stagger == true): 
         makeBrick(house,_x+brickStep, _y, brickStep, true)        
         makeBrick(house,_x-brickStep, _y, brickStep, false)
        # else if stagger is true, offset the brick by half
        elif stagger == true:
         makeBrick(house, _x-brickStep, _y, brickStep, false)
        # else make a standard brick
        else:
         makeBrick(house, _x, _y, brickStep, false)
      if stagger == false:
        stagger = true
      else:
        stagger = false
    
    # Main body of house
    addRect(house,x,y,size,size)
    
    # Roof
    addLine(house,x+size,y,x+size/2,y-size/3)
    addLine(house,x,y,x+size/2,y-size/3)
    
    # Door
    addRectFilled(house,x+size/2 - int(doorScale/2),(y+size) - doorScale*2, doorScale, doorScale*2, brown)
    addRect(house,x+size/2 - int(doorScale/2),(y+size) - doorScale*2, doorScale, doorScale*2)
    
    # Windows
    addRectFilled(house,x + doorScale/2,y + doorScale,doorScale,doorScale, white)
    addRectFilled(house,x+size - doorScale - doorScale/2,y + doorScale,doorScale,doorScale, white)
    addRect(house,x + doorScale/2,y + doorScale,doorScale,doorScale)
    addRect(house,x+size - doorScale - doorScale/2,y + doorScale,doorScale,doorScale)
    #addRect(house,120,120,20,20)
    show(house)
    return(house)
  
# Make a brick for the house
# house    = the house/picture to add the brick to
# origin[] = the x and y positions for the house
def makeBrick(house, x, y, brickStep, stagger):
  brickW = brickStep*2
  brickH = brickStep
  if stagger == false:
    addRectFilled(house, x, y, brickW, brickH, red)
    addRect(house,x,y,brickW,brickH)
    
  else:
    addRectFilled(house, x, y, brickH, brickH, red)
    addRect(house,x,y,brickH,brickH)
      

def makeTown(width, height, houses):
  
  picture=makeEmptyPicture(width, height)
  ground = int(height*.35)
  
  # Color the sky and ground
  addRectFilled(picture, 0, 0, width, ground, cyan)
  addRectFilled(picture, 0, ground, width, height, green)
  
  runningX = 0
  row = 1
  for index in range(0,houses,1):
      if index == houses/2:
        row = 2
        runningX = 0
      houseX = runningX
      tempScale = random.randint(4,10)/10.00
      if row == 1:
        houseY = random.randint(ground, height-int(ground/2) - int(houseBase*tempScale))
      elif row == 2:
        houseY = random.randint(height-int(ground/2), height - int(houseBase*tempScale))
      runningX = runningX + int(houseBase*tempScale)+10
      origin = [houseX, houseY]
      print "House ", index, " at:", houseX, ",", houseY 
      drawHouse(picture,origin,tempScale)
      repaint(picture)

makeTown(1200, 600, 24)
  

