def makeList():
  list = []
  for i in range(0, 9):
    file = pickAFile()
    pic = makePicture(file)
    list.append(pic) 
    
  return list

#pictures are added to empty list
listOfPictures = []
listOfPictures = makeList()

#opens the pictures in the list
for i in range(0, 9):
  show(listOfPictures[i])
  
  
  
width = getWidth(listOfPictures[0])
height = getHeight(listOfPictures[0])

newPic = makeEmptyPicture(width, height)

piclist1 = getPixels(listOfPictures[0])
piclist2 = getPixels(listOfPictures[1])
piclist3 = getPixels(listOfPictures[2])
piclist4 = getPixels(listOfPictures[3])
piclist5 = getPixels(listOfPictures[4])
piclist6 = getPixels(listOfPictures[5])
piclist7 = getPixels(listOfPictures[6])
piclist8 = getPixels(listOfPictures[7])
piclist9 = getPixels(listOfPictures[8])
piclistNewPic = getPixels(newPic)

for i in range(0, width*height):
  newRed = []
  newGreen = []
  newBlue = []
  
  pixel = piclist1[i]
  
  newRed.append(getRed(pixel))
  newGreen.append(getGreen(pixel))
  newBlue.append(getBlue(pixel))
  
  pixel = piclist2[i]
  newRed.append(getRed(pixel))
  newGreen.append(getGreen(pixel))
  newBlue.append(getBlue(pixel))
  
  pixel = piclist3[i]
  newRed.append(getRed(pixel))
  newGreen.append(getGreen(pixel))
  newBlue.append(getBlue(pixel))
  
  pixel = piclist4[i]
  newRed.append(getRed(pixel))
  newGreen.append(getGreen(pixel))
  newBlue.append(getBlue(pixel))
  
  pixel = piclist5[i]
  newRed.append(getRed(pixel))
  newGreen.append(getGreen(pixel))
  newBlue.append(getBlue(pixel))
  
  pixel = piclist6[i]
  newRed.append(getRed(pixel))
  newGreen.append(getGreen(pixel))
  newBlue.append(getBlue(pixel))
  
  pixel = piclist7[i]
  newRed.append(getRed(pixel))
  newGreen.append(getGreen(pixel))
  newBlue.append(getBlue(pixel))
  
  pixel = piclist8[i]
  newRed.append(getRed(pixel))
  newGreen.append(getGreen(pixel))
  newBlue.append(getBlue(pixel))
  
  pixel = piclist9[i]
  newRed.append(getRed(pixel))
  newGreen.append(getGreen(pixel))
  newBlue.append(getBlue(pixel))
  
  newRed.sort()
  newGreen.sort()
  newBlue.sort()
  
  setRed(piclistNewPic[i], newRed[4])
  setBlue(piclistNewPic[i], newBlue[4])
  setGreen(piclistNewPic[i], newGreen[4])
  
  
show(newPic)
