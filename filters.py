#Cody Dill
#three filters with sound 

#RiseColorGlasses with fire sound
def FSimgOne():
  img = makePicture(pickAFile()) 
  sound = makeSound(pickAFile()) 
  pix = getPixels(img)
  for p in pix:
    r,g,b = getRed(p) * 1.1, getGreen(p) * .7, getBlue(p) * .7
    setRed(p,r)
    setGreen(p,g)
    setBlue(p,b)
  show(img)
  play(sound)

#Negative with Scream   
def FSimgTwo():
  #Grab HauntedHouse2 Jpeg
  img = makePicture(pickAFile())
  #Grab screamteast2 twice 
  img2 = makePicture(pickAFile())
  img3 = makePicture(pickAFile())
  #Haunted House noise  
  sound = makeSound(pickAFile())
  #Scream effect
  scream_sound = makeSound(pickAFile())
  pix = getPixels(img)
  for p in pix:
    r,g,b = 255 - getRed(p), 255 - getGreen(p), 255 - getBlue(p)
    setRed(p,r)
    setGreen(p,g)
    setBlue(p,b)
  #show(img) 
  play(sound)
  #copies scream into the windows
  newimage = copyInto(img2,img, 359,305)
  newimage2 = copyInto(img3,img,562,305) 
  #show(img)
  show(newimage2)
  play(scream_sound)
  
 
  
#Matrix     
def FSimgThree():
  img = makePicture(pickAFile()) 
  sound = makeSound(pickAFile())
  #show(img)
  pic = duplicatePicture(img)
  #width2 = getWidth(pic)
  #height2= getHeight(pic)
  width = getWidth(img)
  height = getHeight(img)
  foldPoint = height/2
  
  for y in xrange(0,foldPoint):   
    for x in xrange(width):
      currentPixel = getPixel(pic, x,(height-y) - 1)
      color = getColor(currentPixel)
      locatePixel = getPixel(pic,x,y)
      setColor(locatePixel, color)
  play(sound)
  shrink_height = height/2
  shrink_width = width/2
  #shrink2_height = height2/2
  #shrink2_width = width2/2
  
 # pic2 = makeEmptyPicture(shrink_width,shrink_height)
 # for x in xrange(0,width):
 #   for y in xrange(0,height):
 #     color = getColor(getPixel(img,x,y))
 #     locatePixel = getPixel(pic2, x/2,y/2)
 #     setColor(locatePixel,color)
  
 # pic3 = makeEmptyPicture(shrink_width,shrink_height)
 # for x in xrange(0,width):
 #   for y in xrange(0, height):
 #     color =getColor(getPixel(pic,x,y)
 #     locatePixel = getPixel(pic3,x/2,y/2)
 #     setColor(locatePixel,color)
          
  #show(pic2)
  #show(pic3)
  show(img)
  show(pic)
  
  
  
  
  
  
  
  
  
  